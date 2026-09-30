# Chapter 03 — Building "Hello World!" in C++

*Original content written for OSDev_Learning_Hub — walks through the real,
verified code in `Example_OS_Project/cpp/`.*

## What you'll have at the end
An [ELF](../../GLOSSARY/elf.md "The executable format that lets a bootloader load your kernel") [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") that boots in [QEMU](../../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing") and prints:
```
Hello World!
Welcome to your very own operating system (C++ edition).
```
The C++ version looks a lot like the C one from Chapter 01 — same `boot.s`,
same `linker.ld`, same [VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") — but it teaches the **two things that
are actually different about C++ on bare metal**: how the [entry point](../../GLOSSARY/entry-point.md "The symbol (usually _start) the bootloader jumps to") keeps
`extern "C"` linkage so assembly can call it, and the compiler flags that
shut off C++ features (exceptions, RTTI) that would need a runtime you don't
have.

## The flow, in one picture

```mermaid
flowchart LR
    subgraph "boot.s (assembly)"
        A[Bootloader loads kernel<br/>at 1 MiB] --> B[Multiboot header<br/>0x1BADB002]
        B --> C[Set up 16 KiB stack<br/>movl $stack_top, esp]
    end
    C -- "call kernel_main" --> D[extern \"C\" kernel_main<br/>C linkage = unchanged name]
    D --> E[vga::clear]
    E --> F[vga::write Hello World!]
    F --> G[for ;;  spin forever]
```
The assembly on the left makes an ordinary `call` to the C++ function on the
right. That jump only resolves because `extern "C"` keeps the exported symbol
spelled exactly `kernel_main` — name-mangling would break the link.

## Step 1 — Same bootstrap, different entry point

`cpp/boot.s` is the *same* shared [Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002") bootstrap the C kernel uses
(it's literally shared across the C, C++ and Go kernels in this project).
One line matters for our story:

```nasm
movl $stack_top, %esp        ; point the stack at the top of our 16 KiB
call kernel_main              ; jump into the C++ kernel
```

`boot.s` calls a symbol named **`kernel_main`** — a plain, unterminated
identifier. If the C++ compiler is allowed to do its normal thing, it will
*mangle* every exported function name (turn `kernel_main` into something
like `_Z11kernel_mainv`), and `boot.s` would resolve to a symbol that no
longer exists. That's the whole C++ problem in a sentence.

## Step 2 — `extern "C"` so boot.s can call you

The fix lives in `cpp/kernel.c++`:

```cpp
extern "C" void kernel_main() {
    vga::clear();
    vga::write("Hello World!\n");
    vga::write("Welcome to your very own operating system (C++ edition).\n");

    for (;;)   // a kernel never returns
        ;
}
```

- **`extern "C"`** tells the compiler to give `kernel_main` **C linkage** —
  exported under its plain name, exactly what `boot.s` calls. Without it, C++
  name-mangling would break the link.
- `for (;;)` — like every kernel here, it never returns what C++ calls its
  *main*; there is no host to return to.

The VGA driver lives in a `namespace vga` so the symbol names stay tidy, but
that's ordinary C++ — the interesting part is the entry point.
`namespace vga` just groups `WIDTH`/`HEIGHT`/`COLOR` and the `putchar`,
`write`, `clear` helpers.

## Step 3 — Why `#define VGA_SCREEN`, not a constexpr

In C, you write `#define VGA_MEMORY ((unsigned short*)0xB8000)`. The C++ file
uses the same macro trick with a C++-flavored name:

```cpp
#define VGA_SCREEN ((unsigned short*)0xB8000)
```

Why not write the more "C++-idiomatic" version the comment warns about?

```cpp
constexpr unsigned short* screen = (unsigned short*)0xB8000;  // won't work
```

Two C++ rules get in the way:

1. **`constexpr` allows only constant expressions.** The address `0xB8000`
   doesn't fit in an `unsigned short` (that type tops out at 65535!), so you
   can't even squeeze it into a plain `constexpr unsigned short`. It needs a
   *pointer*, and...
2. **`constexpr` + `reinterpret_cast` is not allowed.** Turning an integer
   literal into a memory address requires a cast that the language classifies
   as a runtime reinterpretation — you cannot `reinterpret_cast` inside a
   `constexpr` context. There is no legal way to write `0xB8000 as a constexpr
   pointer`.

So we fall back to the preprocessor macro exactly like the C kernel — a plain
text substitution that happens *before* the compiler ever sees it, sidestepping
both rules. The compiler still optimizes the resulting pointer arithmetic
into directly addressing `0xB8000`.

The actual write is identical to C — a VGA cell is `[color<<8 | char]`:

```cpp
unsigned short* cell = VGA_SCREEN + (row * WIDTH + col);
*cell = (unsigned short)((COLOR << 8) | (unsigned char)c);
```

## Step 4 — Freestanding flags: silencing the runtime you don't have

The build in `cpp/Makefile`:

```make
CXX      ?= g++
CXXFLAGS = -ffreestanding -fno-pie -m32 -nostdlib \
           -fno-exceptions -fno-rtti -O2 -Wall -Wextra
ASFLAGS  = --32
LDFLAGS  = -m elf_i386 -T linker.ld -nostdlib
```

Most of these you met in the C chapter (`-ffreestanding`, `-fno-pie`, `-m32`,
`-nostdlib`). C++ adds two that have no C equivalent:

- **`-fno-exceptions`** — C++ `try`/`throw`/`catch` rely on an *unwinding
  runtime* that walks the stack and calls destructors. Bare metal has no OS
  to back that runtime, so we compile it out and the language forbids
  exception keywords.
- **`-fno-rtti`** — Run-Time Type Information (`dynamic_cast`, `typeid`)
  needs per-class metadata and runtime support that also doesn't exist on a
  freestanding kernel. Shut it off too.

Both are "you can't use this, so stop pretending you can" flags — the compiler
stops generating the code paths that would have to call the missing runtime.
You also compile with **no standard headers**: the commented header of
`kernel.c++` notes that even `<cstdint>` would pull in C++ runtime headers
that are neither freestanding-safe nor present in a `-m32` toolchain. On bare
metal you bring your own types (`char`, `unsigned short`).

The link step is the C one verbatim:

```make
$(LD) -m elf_i386 -T linker.ld -nostdlib -o kernel.bin boot.o kernel.o
```

## Step 5 — Build & run

```bash
make            # assembles boot.s, compiles kernel.c++, links kernel.bin
make run        # boots kernel.bin in QEMU (qemu-system-i386)
make iso        # optional: a bootable GRUB ISO via grub-mkrescue
```

## Verification

What was actually verified for this language:

- `cpp/kernel.bin` **builds** (`as --32 boot.s -o boot.o`, then
  `g++ -ffreestanding -fno-pie -m32 -nostdlib -fno-exceptions -fno-rtti -O2
  -Wall -Wextra -c kernel.c++`, then the `ld` link) with **zero warnings**
  under `-Wall -Wextra`.
- The produced `kernel.bin` is a **32-bit i386 ELF** with the `.multiboot`
  header of the shared `boot.s` — the same bootstrap that was confirmed as a
  valid [Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002") v1 kernel for the C edition, now carrying the C++ entry point.
- Booting it in QEMU prints `Hello World!` plus the C++-edition welcome line
  (the same VGA framebuffer read which the C chapter documents).

> **Bridge to OS concepts:** C++ teaches the **link-time contract between
> your bootstrap and your kernel** — the exported symbol `boot.s` calls
> (concepts/01 **[bootloaders](../../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") and [Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002")**), the **memory layout** the
> linker demands so the kernel lands at 1 MiB (concepts/02), and **direct
> hardware I/O** through the [VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") at `0xB8000` (concepts/04). The
> `extern "C"` and freestanding flags are the language-specific price of
> talking to hardware with nothing underneath you.

---

## Watch and learn

- [POINTERS in C++ (The Cherno)](https://www.youtube.com/watch?v=DTxHyVn0ODg) — The Cherno's most-watched episode on what pointers are and how they point into memory — the same `unsigned short*` model your kernel uses to reach the VGA framebuffer at `0xB8000`.
- [REFERENCES in C++ (The Cherno)](https://www.youtube.com/watch?v=IzoFn3dfsPA) — References vs. pointers and C-linkage-adjacent semantics, clarifying how the VGA driver's values pass around the namespace without copying.
- [How the C++ Compiler Works (The Cherno)](https://www.youtube.com/watch?v=3tIqpEmWMLI) — Exactly what name mangling is and why a C++ compiler renames `kernel_main` — the mechanism your `extern "C"` exists to defeat so `boot.s` can resolve the symbol.
- [C++ full playlist (The Cherno)](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb) — The complete beginner series covering memory, arrays, and low-level details that underpin the freestanding C++ kernel.
