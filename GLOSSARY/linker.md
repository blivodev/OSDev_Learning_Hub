<!-- Glossary page — Linker. Grounded in OSDev_Learning_Hub docs. -->

# Linker

> **[Back to glossary index](README.md)** · Category: Toolchain & build

The linker (`ld`) merges all your object files into a single kernel image and places it at a chosen memory address, controlled by a **linker script**.

## The short version
A kernel can't just be a bunch of `.o` files — it has to be one image sitting at a specific address (1 MiB) with a defined entry point. The linker does this gluing. Every kernel in this hub is linked with a `linker.ld` script that says *load at 1 MiB, put the Multiboot header first, entry point is `_start`*. The four-pillar tutorial calls it the skill of *"placing your kernel in memory."*

## Detailed explanation
When a normal `main()` returns, the OS cleans up. A kernel never returns and must be loaded at a *specific* address. GNU `ld` places sections in memory according to a linker script. The shared C/C++/Go script (`Example_OS_Project/c/linker.ld`) does:

```ld
ENTRY(_start)                     /* the entry point the bootloader jumps to */
SECTIONS {
    . = 1M;                       /* load the kernel at 1 MiB */
    .text BLOCK(4K) : ALIGN(4K) { *(.multiboot) *(.text) }
    .rodata BLOCK(4K) : ALIGN(4K) { *(.rodata) }
    .data  BLOCK(4K) : ALIGN(4K) { *(.data) }
    .bss   BLOCK(4K) : ALIGN(4K) { *(COMMON) *(.bss) *(.bootstrap_stack) }
}
```

The key idea documented in the file: `1 MiB` is the conventional place where bootloaders put kernels — below that is BIOS/reserved memory. The `.multiboot` section comes **first** so the magic header is at the very front of the image for the bootloader to find.

The link command pulls together the assembler output and compiler output into `kernel.bin`:

```bash
ld -m elf_i386 -T linker.ld -o kernel.bin boot.o kernel.o
```

`-m elf_i386` selects the 32-bit ELF output format, `-T linker.ld` points at the script, and all the C/C++ Makefiles add `-nostdlib` so nothing from the host runtime sneaks in.

```mermaid
flowchart LR
    BO[boot.o (assembler)] --> LD[ld -T linker.ld -m elf_i386]
    KO[kernel.o (compiler)] --> LD
    LD --> K[kernel.bin at 1 MiB, ELF]
```

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/c/linker.ld`, `cpp/linker.ld`, and `go/linker.ld` — three near-identical universal scripts shared by all GNU-as kernels.
- The link line appears in `c/Makefile`: `$(LD) $(LDFLAGS) -o $@ boot.o kernel.o` with `LDFLAGS = -m elf_i386 -T linker.ld -nostdlib`.
- `synthesized_tutorials/00-introduction/02-your-toolchain.md` §3 shows the linker script and calls `ld` one of the four pillars: *"You control where the kernel loads (1 MiB) via a linker script."*

## Watch / listen
[- How the C++ Linker Works - The Cherno](https://www.youtube.com/watch?v=H4s55GgAg0I) — symbol resolution and linking
- [OSDev Wiki — Linker Scripts](https://wiki.osdev.org/Linker_Scripts) — free, authoritative
- [OSDev Wiki — Bare Bones](https://wiki.osdev.org/Bare_Bones) — shows `ld` in a full boot
- [GNU ld manual — Linker Scripts](https://sourceware.org/binutils/docs/ld/Scripts.html) — official free docs

## Related terms
- [Assembler](assembler.md)
- [ELF](elf.md)
- [Multiboot](multiboot.md)
- [Cross-Compiler](cross-compiler.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
