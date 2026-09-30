<!-- Glossary page — Assembler. Grounded in OSDev_Learning_Hub docs. -->

# Assembler

> **[Back to glossary index](README.md)** · Category: Toolchain & build

An assembler is a tool that turns assembly language (human-readable mnemonics) into machine-code object files the linker can combine.

## The short version
When a PC powers on, the CPU runs the first instructions with **no stack and no C runtime** — so the very first file of every kernel here is a small assembly bootstrap. The assembler converts that `boot.s` into `boot.o`. This hub uses the GNU assembler (`as`), so you do **not** need NASM installed; the same `boot.s` is shared by the C, C++, and Go kernels.

## Detailed explanation
The bare-metal boot story is assembly because the first steps are raw and simple: emit the Multiboot header bytes exactly, reserve a stack, and jump into the high-level kernel. In `Example_OS_Project/c/boot.s` (shared unmodified by the C, C++ and Go kernels), the `.multiboot` section declares the header fields from the Multiboot spec:

```
.set MAGIC,    0x1BADB002        /* the Multiboot magic number */
.set FLAGS,    ALIGN | MEMINFO   /* ALIGN=1<<0, MEMINFO=1<<1 → 0x3 */
.set CHECKSUM, -(MAGIC + FLAGS)
```
then `.long MAGIC / .long FLAGS / .long CHECKSUM` emit those 12 bytes at the front of the image so bootloader and QEMU recognize it.

It also reserves a `16 KiB` bootstrap stack (`.skip 16384`) because the CPU boots with an undefined stack pointer, sets `esp`/`ebp` to its top, and calls `kernel_main`. If that function ever returns, it executes `cli` then `hlt` and loops forever — a kernel never returns.

The four-pillar table in `02-your-toolchain.md` positions the assembler first: *"Turns boot.s assembly into machine-code object files… You write 30-50 lines of assembly for the boot entry + Multiboot header."*

```mermaid
flowchart LR
    S[boot.s assembly] --> AS[as --32]
    AS --> O[boot.o object]
    O --> LD[ld -T linker.ld]
    LD --> K[kernel.bin]
```

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/c/boot.s` — the universal Multiboot bootstrap, shared by C, C++ and Go (documented in its header: *"THIS FILE IS SHARED BY THE C, C++ AND GO KERNELS"*).
- `Example_OS_Project/go/boot.s` — the same file plus Go-runtime stub symbols `__go_register_gc_roots` and `__go_runtime_error` as empty functions.
- Build line in `c/Makefile`: `$(AS) --32 boot.s -o boot.o` where `AS ?= as`.

## Watch / listen
- [OSDev Wiki — Assembly](https://wiki.osdev.org/Assembly) — free, authoritative
- [OSDev Wiki — NASM](https://wiki.osdev.org/NASM) — if you prefer NASM syntax

## Related terms
- [Linker](linker.md)
- [Multiboot](multiboot.md)
- [Kernel](kernel.md)
- [x86](x86.md)
- [Cross-Compiler](cross-compiler.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
