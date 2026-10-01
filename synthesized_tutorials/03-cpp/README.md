# Chapter 03 — Building "Hello World!" in C++

*Original content written for OSDev_Learning_Hub — walks through the real,
verified code in `Example_OS_Project/cpp/`.*

> **Read after Chapters 01 (C) and 02 (Rust).** The C chapter built the mental
> model; the Rust chapter showed a language policing memory. C++ sits **in
> between and past both**: it shares C's raw machine model, but layers on
> classes, namespaces, overloads, exceptions, and RTTI — features that *all*
> need runtime support you don't have on bare metal. This chapter is about
> exactly which C++ features die and why, and how `extern "C"` keeps your
> bootstrap talking to your compiler.

---

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

---

## Part A — C++ fundamentals for a systems programmer

If you know C, you know 80% of C++ on bare metal. The differences that matter
here are **classes/abstraction**, **overloading**, **name mangling**, and
**the runtime-hungry features** (exceptions, RTTI). Let's take each.

### A.1 — Classes are mostly "structs with functions, in a box"

The VGA driver in this kernel lives in a `namespace vga` with free functions —
a deliberately C-flavored design. But a class would work too, and it's C++'s
signature abstraction.

```cpp
// A plain-C approach (what this kernel uses): free functions + globals.
namespace vga {
    constexpr int WIDTH  = 80;
    constexpr int HEIGHT = 25;
    int row = 0, col = 0;
    void putchar(char c) { /* poke 0xB8000 */ }
}

// The class approach — same machine code, nicer encapsulation:
class VgaTerminal {
public:
    void putchar(char c) { /* poke 0xB8000, same as above */ }
    void write(const char* s) { while (*s) putchar(*s++); }
private:
    int row_ = 0, col_ = 0;      // only VgaTerminal's methods may touch these
};
```

A class doesn't cost any more machine code than a struct with functions — the
compiler resolves the `this` pointer to an ordinary hidden argument. The
*virtual* keyword is where runtime overhead creeps in (a vtable lookup per
call), which is why OS writers sometimes avoid `virtual` in hot paths. For a
kernel, either style works; this project uses `namespace` + `inline` to stay
minimal.

### A.2 — Overloading and the disaster it creates: name mangling

C++ lets you define several functions with the *same name* as long as they
differ in parameters:

```cpp
void write(int x);          // writes an integer
void write(const char* s);  // writes a string
```

The compiler needs to distinguish them at link time, so it **mangles** the
names into unique symbols. `void write(const char*)` becomes something like
`_Z5writePKc`, and `void write(int)` becomes `_Z5writei`. This is invisible in
normal development because you never call a C++ function from assembly — the
linker resolves everything.

**A kernel breaks that assumption.** `boot.s` does a plain `call kernel_main`.
If the C++ compiler mangles `kernel_main`, the exported symbol becomes
`_Z11kernel_mainv` and `boot.s` references a symbol that no longer exists →
**link error**. That's the entire C++-on-bare-metal problem in one sentence,
and `extern "C"` is the fix.

### A.3 — Exceptions and RTTI: features with a runtime price

Two C++ features silently assume a runtime that bare metal does not provide:

```cpp
// EXCEPTIONS need unwinding machinery: walk the stack, call destructors,
// find the matching catch. There's no OS to back that runtime, so with
// -fno-exceptions the compiler rejects try/throw/catch outright.
void foo(int x) {
    if (x <= 0)
        throw std::runtime_error("bad");   // ERROR under -fno-exceptions
}

// RTTI (dynamic_cast / typeid) needs per-class metadata + runtime support.
if (typeid(obj) == typeid(Derived))        // ERROR under -fno-rtti
    auto& d = dynamic_cast<Derived&>(obj); // ERROR under -fno-rtti
```

Neither is "a nice extra you can skip": they are *core* language features whose
support code lives in a runtime library. A kernel compiles them out entirely,
and the compiler then *enforces* that you don't use them. This is C++'s honest
answer to "what happens if my kernel hits an exception?" — it can't happen,
because exceptions don't exist in the freestanding build.

---

## The flow, in one picture

```mermaid
flowchart LR
    subgraph "boot.s (assembly)"
        A[Bootloader loads kernel<br/>at 1 MiB] --> B[Multiboot header<br/>0x1BADB002]
        B --> C[Set up 16 KiB stack<br/>movl $stack_top, esp]
    end
    C -- "call kernel_main" --> D[extern "C" kernel_main<br/>C linkage = unchanged name]
    D --> E[vga::clear]
    E --> F[vga::write Hello World!]
    F --> G[for ;;  spin forever]
    G --> H["g++ -fno-exceptions -fno-rtti<br/>-ffreestanding -m32 -nostdlib"]
```
The assembly on the left makes an ordinary `call` to the C++ function on the
right. That jump only resolves because `extern "C"` keeps the exported symbol
spelled exactly `kernel_main` — name-mangling would break the link.

---

## Part B — Reading the real `Example_OS_Project/cpp/kernel.c++`

Here is the actual `kernel.c++`, 65 lines, the whole kernel. Read it fully —
it is the C kernel plus the two C++-specific fixes we keep naming.

```cpp
// kernel.c++ — A minimal "Hello World!" OS kernel in C++.
//
// We deliberately use ONLY built-in C/C++ types (char, unsigned short)
// and NO standard headers: <cstdint> would pull in the C++ runtime
// headers, which are neither freestanding-safe nor available in a
// -m32 toolchain on most systems. On bare metal you bring your own.

#define VGA_SCREEN ((unsigned short*)0xB8000)

namespace vga {
    constexpr unsigned short WIDTH  = 80;
    constexpr unsigned short HEIGHT = 25;
    constexpr unsigned short COLOR  = 0x0F;  // white on black

    int row = 0;
    int col = 0;

    inline void putchar(char c) {
        if (c == '\n') { col = 0; row++; if (row >= HEIGHT) row = 0; return; }
        unsigned short* cell = VGA_SCREEN + (row * WIDTH + col);
        *cell = (unsigned short)((COLOR << 8) | (unsigned char)c);
        col++;
        if (col >= WIDTH) { col = 0; row++; if (row >= HEIGHT) row = 0; }
    }

    void write(const char* s) { while (*s) putchar(*s++); }

    void clear() {
        unsigned short* cell = VGA_SCREEN;
        for (int i = 0; i < WIDTH * HEIGHT; i++)
            cell[i] = (unsigned short)((COLOR << 8) | ' ');
        row = 0; col = 0;
    }
}

extern "C" void kernel_main() {
    vga::clear();
    vga::write("Hello World!\n");
    vga::write("Welcome to your very own operating system (C++ edition).\n");
    for (;;)
        ;
}
```

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

**A closer look at `extern "C"`:** it's a linkage specifier, not a language
change. It tells the compiler: "export this symbol using the C naming and
calling convention, don't mangle it, and don't apply overload resolution to
it." That is why you also use `extern "C"` when declaring a C library function
in C++ (`extern "C" int puts(const char*);`). Same mechanism, same reason.

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

---

## Part C — A guided walkthrough tied to the code

### C.1 — Build it and verify zero warnings

```bash
cd Example_OS_Project/cpp
make
# as --32 boot.s -o boot.o
# g++ -ffreestanding -fno-pie -m32 -nostdlib -fno-exceptions -fno-rtti -O2 \
#     -Wall -Wextra -c kernel.c++ -o kernel.o
# ld -m elf_i386 -T linker.ld -nostdlib -o kernel.bin boot.o kernel.o
```

The verified build for this chapter produces `cpp/kernel.bin` with **zero
warnings** under `-Wall -Wextra`. The moment you *remove* `-fno-exceptions`,
GCC starts emitting a lot of `_Unwind_*` and `__cxa_*` undefined-reference
errors at the link step — try it to see what the runtime you're omitting looks
like.

### C.2 — Prove `extern "C"` with `nm`

After building, inspect the exported symbol:

```bash
nm cpp/kernel.bin | grep kernel_main
# => 00108000 T kernel_main          ← exported UNDER ITS PLAIN NAME
```

Now comment out `extern "C"` (make it just `void kernel_main()`) and rebuild:

```bash
nm cpp/kernel.bin | grep kernel_main
# => (nothing)   — or you see _Z11kernel_mainv
# and the LINK fails: "undefined reference to `kernel_main'"
```

This one command makes the core C++ lesson tangible: `extern "C"` is the
difference between "links" and "undefined reference."

### C.3 — Boot it

```bash
make run     # qemu-system-i386 -kernel kernel.bin
```

You'll see `Hello World!` and the C++-edition welcome line — the same VGA
framebuffer read the C chapter documents, now delivered through a C++ entry
point.

### C.4 — Exercise: try `-fno-exceptions` removal, then a `namespace` variant

- **Experiment 1:** remove `-fno-exceptions` and add `throw 1;` somewhere —
  watch GCC emit `_Unwind_Resume` references you can't satisfy. This is the
  "runtime you don't have" made visible.
- **Experiment 2:** convert the `namespace vga` free-function driver into a
  `class Vga` with private `row_`/`col_` and `public` `putchar`/`write`/`clear`.
  It builds and boots identically — proving classes cost nothing on bare
  metal (only `virtual` does). This is a fun, safe experiment that deepens
  your feel for what C++ abstraction *is* at the machine level.

---

## Part D — Pitfalls, warnings, and C++-specific traps

These are the failures learners hit on the exact `cpp/` files:

```text
1. FORGETTING extern "C".
   → Link error: "undefined reference to `kernel_main'" (mangled to _Z...).
   Fix: extern "C" on the entry point (and on any C function you call).

2. USING try/throw/catch or dynamic_cast/typeid.
   → Compiler error under -fno-exceptions / -fno-rtti. That's by design:
     those features need a runtime you don't have.

3. #include <cstdint> or <string> or <iostream>.
   → Pulls in C++ runtime headers that aren't freestanding-safe and aren't
     present in a -m32 toolchain. Bring your own types.

4. OUTPUT_TYPE / g++ defaulting to 64-bit.
   → If you drop -m32, pointers jump to 8 bytes, the VGA cell arithmetic
     breaks, and kernel.bin won't boot in 32-bit QEMU. Keep -m32.

5. EXPECTING a constructor to run before kernel_main.
   → Global C++ objects with constructors need "static initialization"
     (the __crt0 / _init runtime) to run them. A bare kernel has NONE, so
     don't rely on global object construction before your entry point.

6. USING new/delete.
   → Both require an operator new that allocates memory. A kernel has no
     heap yet. Either provide a custom operator new (later chapters) or
     don't allocate. See heap-allocation / frame-allocator concepts.
```

### The two that surprise most people

**Global constructors don't run.** On a hosted C++ program, the runtime calls
constructors for every global object before `main`. A bare-metal kernel has
no such runtime — so `namespace vga { int row = 0; }` is fine (that's static
storage, zero-initialized), but a global `std::string` or a class with a real
constructor would be in an *unconstructed* state when `kernel_main` runs.
This is why kernel code sticks to POD (plain old data) globals.

**No `main`, no `new`, no `delete`.** C++'s `operator new` allocates from a
process heap that your kernel doesn't have. Until you build an allocator
(concept `heap-allocation`), the kernel simply doesn't allocate. That's a
*freedom*: it forces you to think about exactly where every byte of state
lives.

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

---

## Part E — C++ vs. C vs. Rust on this kernel

| Capability | C | C++ | Rust |
|-----------|----|----|------|
| Raw `0xB8000` write | free `VGA_MEMORY[i]` | free `*(VGA_SCREEN+i)` | requires `unsafe {}` |
| Entry point linkage | none needed (C names) | `extern "C"` | `#[no_mangle] extern "C"` + `-> !` |
| Exceptions | (not a C feature) | disabled via `-fno-exceptions` | unwinding via `panic="abort"` + `#[panic_handler]` |
| RTTI | n/a | disabled via `-fno-rtti` | n/a (traits, no RTTI) |
| Standard library | partial (`<stdint.h>` etc.) | mostly unavailable freestanding | `core` only (`no_std`) |
| Compiler flags | `-ffreestanding -m32` | adds `-fno-exceptions -fno-rtti` | attributes in source |

The through-line: **every language makes you explicitly disable or stub the
parts that assume an OS.** C does it with flags and by just not calling libc;
Rust does it with crate attributes and a panic handler; C++ does it with
`-fno-exceptions -fno-rtti`. Master that idea once and every future language
is just a different spelling of the same negotiation with the hardware.

---

## Part F — Peeling the Makefile apart (and the missing `binary` magic)

The `cpp/Makefile` is a compact, honest build script. Let's decode it line by
line so the toolchain stops being a mystery:

```make
AS      ?= as              # GNU assembler (or: nasm -f elf32)
CC      ?= gcc
CXX     ?= g++
LD      ?= ld

CFLAGS   = -ffreestanding -fno-pie -m32 -nostdlib -O2 -Wall -Wextra
CXXFLAGS = -ffreestanding -fno-pie -m32 -nostdlib -fno-exceptions \
           -fno-rtti -O2 -Wall -Wextra
ASFLAGS  = --32
LDFLAGS  = -m elf_i386 -T linker.ld -nostdlib

boot.o: boot.s
	$(AS) $(ASFLAGS) boot.s -o $@

kernel.o: kernel.c++
	$(CXX) -c kernel.c++ -o $@ $(CXXFLAGS)

kernel.bin: boot.o kernel.o linker.ld
	$(LD) $(LDFLAGS) -o $@ boot.o kernel.o

run: kernel.bin
	qemu-system-i386 -kernel kernel.bin
```

Three things make this read differently from a hosted build:

1. **`ASFLAGS = --32`** — even the assembler must target 32-bit, because the
   Multiboot v1 bootstrap runs in 32-bit protected mode. If `boot.o` were
   64-bit while `kernel.o` were 32-bit, the link would fail with a
   `file format not recognized` error.

2. **`?= ` (conditional assignment)** — lets you *override* the compiler from
   the command line, e.g. `make CXX=i686-elf-g++`. The OSDev community
   recommends building an actual [cross-compiler](../../GLOSSARY/cross-compiler.md "A compiler that builds code for a different CPU/OS than the one it runs on")
   (`i686-elf-g++`) for real hardware; on a normal Linux box you can use your
   system `g++` with `-m32` and boot the 32-bit ELF straight in QEMU. That's
   exactly what the Makefile's comment says.

3. **No `-o` / no format flag on the output** — `ld` with `-T linker.ld`
   produces an ELF because the linker script's `OUTPUT_FORMAT` (defaults to
   `elf32-i386` when `-m elf_i386`) governs it. The `.multiboot` section
   being first is what makes `grub-file --is-x86-multiboot` pass.

### Constructors and the static-init gap (worth its own callout)

A common C++ OSDev surprise is that **global object constructors never run**
before `kernel_main`. On a hosted binary, `__libc_start_main` / the CRT calls
`_init`, which runs constructors. A bare-metal kernel has none of that.

```cpp
// This global WILL NOT be constructed before kernel_main:
class Counter {
public:
    Counter() { value = 99; }    // depends on the runtime calling this
    int value;
};
Counter g_counter;               // if you read g_counter.value here,
                                 // it's uninitialized (not 99)!

// What kernels actually do instead: POD defaults are fine, because
// .bss is zero-initialized by the loader.
struct Pod { int value = 0; };   // value is reliably 0 after boot
Pod g_pod;
```

The fix for real kernels is a custom static-initialization pass (walk the
`.init_array` / `.ctors` section and call each constructor pointer) — covered
in depth by OSDev "C++ kernel" tutorials. For this "Hello World" chapter, the
rule is simple: **keep globals to POD types**, and you're safe.

### A quick "what to try next" ladder after Hello World C++

1. Provide a **global `operator new`/`operator delete`** backed by a trivial
   bump allocator — suddenly `new` works (see `frame-allocator` concept).
2. Add a **`static` class object** with a constructor and *manually* call it
   at the top of `kernel_main` to see the ordering problem firsthand.
3. Read the **`<cstdint>` vs built-in types** note again: when you outgrow
   `char`/`unsigned short`, bring in `stdint.h`-style types explicitly rather
   than relying on runtime headers.

> **Bridge to OS concepts:** C++ teaches the **link-time contract between
> your bootstrap and your kernel** — the exported symbol `boot.s` calls
> (concepts/01 **[bootloaders](../../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") and [Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002")**), the **memory layout** the
> linker demands so the kernel lands at 1 MiB (concepts/02), and **direct
> hardware I/O** through the [VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") at `0xB8000` (concepts/04). The
> `extern "C"` and freestanding flags are the language-specific price of
> talking to hardware with nothing underneath you.

---

## Watch and learn

Let The Cherno's series anchor the C++-specific mechanics, with a couple of
general memory videos in the mix. All are real and verified on YouTube.

<details class="video-embed">
<summary>▶ Watch: POINTERS in C++ (The Cherno)</summary>
<iframe src="https://www.youtube-nocookie.com/embed/DTxHyVn0ODg" title="POINTERS in C++ (The Cherno)" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>The Cherno's most-watched episode on what pointers are and how they point into memory — the same `unsigned short*` model your kernel uses to reach the VGA framebuffer at `0xB8000`.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: REFERENCES in C++ (The Cherno)</summary>
<iframe src="https://www.youtube-nocookie.com/embed/IzoFn3dfsPA" title="REFERENCES in C++ (The Cherno)" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>References vs. pointers and C-linkage-adjacent semantics, clarifying how the VGA driver's values pass around the namespace without copying.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: How the C++ Compiler Works (The Cherno)</summary>
<iframe src="https://www.youtube-nocookie.com/embed/3tIqpEmWMLI" title="How the C++ Compiler Works (The Cherno)" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>Exactly what name mangling is and why a C++ compiler renames `kernel_main` — the mechanism your `extern "C"` exists to defeat so `boot.s` can resolve the symbol.</p>
</details>
- [C++ full playlist (The Cherno)](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb) — The complete beginner series covering memory, arrays, and low-level details that underpin the freestanding C++ kernel.
<details class="video-embed">
<summary>▶ Watch: Pointers and dynamic memory — stack vs. heap (Jacob Sorber)</summary>
<iframe src="https://www.youtube-nocookie.com/embed/_8-ht2AKyH4" title="Pointers and dynamic memory - stack vs heap (Jacob Sorber)" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>Stack vs. heap crash course — the memory regions a freestanding C++ kernel owns directly and must manage itself, since there's no process heap to fall back on.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: Dynamic memory allocation in C — malloc calloc realloc free</summary>
<iframe src="https://www.youtube-nocookie.com/embed/xDVC3wKjS64" title="Dynamic memory allocation in C - malloc calloc realloc free" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>How heap allocation normally works in C/C++ — the machinery a kernel has to *recreate* (as an allocator) before `new`/`malloc` can mean anything on bare metal.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: Dynamic Memory Allocation | C Programming Tutorial</summary>
<iframe src="https://www.youtube-nocookie.com/embed/R0qIYWo8igs" title="Dynamic Memory Allocation | C Programming Tutorial" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>A friendly, visual walkthrough of malloc/calloc/realloc/free — exactly the API surface a future kernel allocator will emulate, and a great preview of the heap-allocation concept.</p>
</details>

> **Next-step map:** this kernel silences C++'s exceptions and RTTI but keeps
> the raw pointer model. The most rewarding next steps are (1) providing your
> own global `operator new`/`operator delete` once you've built a
> [frame allocator](../../GLOSSARY/frame-allocator.md "Kernel code that tracks and hands out physical memory frames") (concept `heap-allocation`), and (2) learning to call C
> from C++ with `extern "C"` (concept docs). When you're ready, the Rust and Go
> chapters show the same "negotiate with the runtime" dance from the opposite
> side.

---

## 🧪 Exercises & Projects

The C++ track showed a kernel can be written in modern C++ without paying for exceptions or RTTI. These exercises sharpen the C↔C++ seam (`extern "C"`), the static-init gap, and the power-of-two operator overloads you'd provide later. Prereq: the C++ build loop from this README.

### Graded exercises

**Easy**

- [ ] **E1. Rebuild the kernel from scratch, closed-book** (~20–40 min). Close this page
      and the reference. Recreate `C++`'s boot + kernel skeleton from memory:
      assembly that sets the stack and calls into the kernel, the kernel's VGA write, and
      the infinite loop. Build using the chapter's exact command sequence. If you stall,
      peek at [`Example_OS_Project`](../../Example_OS_Project/) only for the *toolchain
      flags*, not the code — then re-close it.
- [ ] **E2. Reproduce the five-step recipe in your words** (~20 min). Write (comments or a
      gist) the five steps — assemble, compile, link, ISO, boot — *in this language's*
      syntax. Note the one tool/flag that made this track different from C.
- [ ] **E3. Change the banner to prove ownership** (~20 min). Edit the kernel's message to
      a unique string, rebuild, boot in QEMU, and confirm your string in the output.
      This kills the "it's a template, not mine" feeling for good.

**Medium**

- [ ] **M1. Add a second color/attr** (~1 hr). Extend the VGA write beyond one
      color: print your banner in *bright green on black* and an error line in red on
      white. Practice the `C++` way of writing to a typed hardware pointer
      (whichever layer your track uses).
- [ ] **M2. Read the fault, don't guess** (~1 hr). Boot with `-d int,cpu_reset` and a
      deliberately broken kernel (e.g. no stack setup). Capture the fault, fix, re-run.
      Write a one-line "what a missing-stack fault looks like here" note.
- [ ] **M3. Deterministic build + clean tree** (~45 min). `make clean && make`, hash the
      `kernel.bin`, re-run, and confirm an identical hash. Then move your build to a second
      machine/VM and reproduce from the repo — proving your toolchain notes are complete.

- [ ] **M4. Exceptions off, defined behavior on** (~45 min). Confirm your kernel silences exceptions (`-fno-exceptions`) and *document* what happens if one is thrown. Then demonstrate a `nothrow new` path doesn't abort. Two sentences, then move on.

**Hard**

- [ ] **H1. Port a concept back in** (~3 hr). Take this language's hello-world kernel and
      add one subsystem from the concept chapters: a PIT timer ISR
      ([concept 03](../concepts/03-interrupts-and-the-idt.md)) or a frame allocator
      ([concept 02](../concepts/02-memory-management.md)). This proves the concepts are
      language-independent.
- [ ] **H2. Compare against C side-by-side** (~1.5 hr). Put your kernel's `C++`
      source next to `Example_OS_Project/c/kernel.c`. Annotate the *same logical steps*
      (stack, VGA write, loop) across both. Where did the language impose ceremony? Where
      did it save you a line?

### ⭐ Mini-project — Port the Example kernel to C++ and replace the C I/O seam

**Goal.** A C++ kernel where the low-level `extern "C"` seam is explicit and the
first piece of `runtime you own` (a global `operator new`) exists. **Estimated time:**
2–4 hr. **Prereq:** the C++ README + toolchain chapter.

1. **Scaffold.** A `kernel.c++` that boots: `extern "C"` `_start`, no exceptions/RTTI,
      entry in the linker script. Confirm `readelf -h` entry + `file` ELF class.
2. **Make the C seam visible.** If any concept requires C (like the hub's `boot.s`
      helpers), call it through a declared `extern "C"` block and comment *why* the linkage
      differs from normal C++ names.
3. **Own a `operator new`.** Once you trust the stack is valid, provide global
      `void* operator new(size_t)` returning addresses from a tiny bump allocator (no
      heap yet). Now `new` works in your kernel—without libc.
4. **Guard the static-init gap.** The README flagged that globals may not run their
      constructors before `_start` is safe. Write a small `.init_array`/constructor-runner
      in `_start` (call each function pointer) and a test: a global object whose ctor sets
      a marker that your banner reads. See it print the marker or none, then fix the runner
      to make it print.
5. **Safe-ish VGA.** Wrap the VGA buffer in a `TextBuffer` class (RAII, explicit `volatile`
      members) so `buf[0] = { 'H', GREEN_ON_BLACK };` is the API. Add `clear()` and a
      `print_int` helper.
6. **Add a concept.** Port the frame allocator from concept 02 *as a C++ class* with RAII
      ownership (allocate in a `Frame` object, free on destruction). Note how RAII changes
      the "don't forget to free" discipline vs. C.
7. **Reproduce.** `make clean && make` from a fresh clone; README must cover the
      constructor-runner + `extern "C"` notes.

*(Reference: [`Example_OS_Project/cpp/`](../../Example_OS_Project/cpp/) only when stuck.)*

**Checklist**

- [ ] closed-book kernel rebuild succeeds without the page open
- [ ] self-chosen banner string boots and is visible in QEMU
- [ ] at least one distinct color/attr customisation verified on screen
- [ ] `make clean && make` reproduces an identical `kernel.bin` hash
- [ ] second machine/VM reproduces the build from the repo alone
- [ ] a chosen concept (timer or allocator) is ported and boots

