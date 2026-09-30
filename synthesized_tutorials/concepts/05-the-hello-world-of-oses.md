# Concept — The "Hello World of OSes" Recipe

*Original content written for OSDev_Learning_Hub.*

Every beginner OS in every language follows the **same five steps**. If you understand these, you can read any "bare bones" tutorial in any language and immediately know where you are.

## The recipe

```mermaid
flowchart TD
    A[1. Bootstrap stub in assembly] --> B[2. Multiboot header 0x1BADB002]
    B --> C[3. Provide a stack]
    C --> D[4. Call kernel_main / _start]
    D --> E[5. Write to 0xB8000 and halt]
```

| Step | Language-indep. concept | Language file |
|------|-------------------------|---------------|
| 1 | Entry point + CPU setup | `boot.s` (assembler) |
| 2 | Multiboot magic `0x1BADB002` | `boot.s` (in `.multiboot` section) |
| 3 | A 16 KiB stack so calls work | `boot.s` |
| 4 | The C/rust/go/etc. entry | `kernel.c` / `main.rs` / `kernel.go` |
| 5 | Write "Hello World!" to `0xB8000` | the kernel source |

## Why every language needs the same boot.s

The CPU boots into a primitive state: **no stack, real mode, nothing set up**. That setup *must* be done in assembly, because your high-level language's compiler has no idea a stack doesn't exist yet. So even the Rust tutorial uses a tiny bit of assembly (or the `bootloader` crate which bundles it).

Here's the universal bootstrap that powers the C, C++ and Go kernels in `Example_OS_Project`:

```nasm
; boot.s — the universal Multiboot bootstrap
section .multiboot
align 4
    dd 0x1BADB002          ; magic   (0x1BADB002)
    dd 0x03                ; flags   (ALIGN | MEMINFO)
    dd -(0x1BADB002 + 0x03); checksum

section .bss
align 16
stack_bottom:
    resb 16384             ; 16 KiB stack
stack_top:

section .text
global _start
_start:
    mov esp, stack_top     ; (1) give the CPU a stack
    mov ebp, stack_top     ; (2) frame pointer, for sanity
    extern kernel_main
    call kernel_main       ; (3) jump to the high-level kernel
    cli
    hlt                    ; (4) halt forever — kernel never returns
.loop:
    jmp .loop
```

> `dd` in NASM emits a 4-byte value. The three `dd`s ARE the Multiboot header.

## The same recipe, five languages

| Language | Your "kernel_main" | How it prints | Skip-able if... |
|----------|--------------------|---------------|-----------------|
| **C** | `void kernel_main(void)` | writes to `0xB8000` | — (the reference) |
| **C++** | `extern "C" void kernel_main()` | same, via `0xB8000` | you know C++ basics |
| **Rust** | `pub extern "C" fn _start()` | `0xB8000` via `unsafe` | you know Rust basics |
| **Go** | `func Main()` | via `terminal.go` | you know Go basics |
| **C#** | `Kernel.Run()` (Cosmos) | `Console.Write` | you know C# basics |

The **point**: OS concepts are language-agnostic. Switch languages and you switch *syntax* and *build flags* — not the ideas.

## The one true test
Whatever language you choose, your final command looks like this:

```bash
make run-c        # or run-cpp, run-rust, run-go
```

and QEMU pops up a black window with:

```
Hello World!
```

![Screenshot]: Add a QEMU screenshot showing "Hello World!" in white-on-black.

If that works, **you have written an operating system.** Everything from here — paging, interrupts, scheduling, filesystems — is adding features to an OS that already boots.

> **Now go build it:** the five language walkthroughs in `01-c/` → `05-csharp/`, with real code in [`Example_OS_Project/`](../../Example_OS_Project/).
