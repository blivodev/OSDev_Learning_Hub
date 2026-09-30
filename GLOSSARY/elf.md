<!-- Glossary page — ELF. Grounded in OSDev_Learning_Hub docs. -->

# ELF

> **[Back to glossary index](README.md)** · Category: Toolchain & build

ELF (Executable and Linkable Format) is the standard file format for compiled binaries on Unix-like systems — and the format this hub's kernels are built and booted in.

## The short version
Every C, C++, and Rust kernel here is produced as an **ELF** file. ELF stores your code, read-only data, initialized data, and BSS in named sections (`.text`, `.rodata`, `.data`, `.bss`) that the linker script arranges, and it records the entry point (`_start`) and the load address. The format is what lets a bootloader or QEMU load your kernel at a chosen address (1 MiB) and jump to the right place.

## Detailed explanation
When `gcc -c kernel.c` produces `kernel.o` and `ld -T linker.ld` produces `kernel.bin`, both are ELF files. An ELF file has a header, program headers, and section headers. The sections relevant to a kernel are exactly the ones the linker script names:

| Section | Contents |
|---------|----------|
| `.multiboot` | the Multiboot header (magic `0x1BADB002`) — must be first |
| `.text` | executable machine code |
| `.rodata` | read-only constants (string literals) |
| `.data` | initialized global data |
| `.bss` | uninitialized data (stack, buffers) — takes no space on disk |
| `.bootstrap_stack` | the 16 KiB stack reserved in `boot.s` |

The linker assembles these sections *in the order and at the addresses the linker script dictates*, so the in-memory ELF-image starts with the magic header. When you run `qemu-system-i386 -kernel myos.bin`, QEMU's built-in loader uses the ELF program headers to place the kernel at 1 MiB and reads the entry point, then jumps to `_start`.

The Rust kernel also produces an ELF from the bare-metal target (`x86_64-unknown-none`). Building `cargo build --target x86_64-unknown-none` yields an ELF at `target/.../example_os_rust` — that's the freestanding kernel ELF before the bootloader crate wraps it into a disk image.

```mermaid
flowchart LR
    OBJ[.o ELF files] --> LD[linker.ld]
    LD --> BIN[kernel.bin — ELF at 1 MiB]
    BIN --> Q[QEMU -kernel loads ELF]
```

## Why it matters here (OSDev_Learning_Hub)
- The C Makefiles build *"kernel.bin (a Multiboot bootable ELF)"* — see `Example_OS_Project/c/Makefile` and `cpp/Makefile` (`LDFLAGS = -m elf_i386` requests ELF output).
- `Example_OS_Project/rust/README.md`: `cargo build --target x86_64-unknown-none` ⟹ *"freestanding ELF"*.
- The linker script `linker.ld` explicitly places the `.multiboot` section first — see `Example_OS_Project/c/linker.ld`.

## Watch / listen
- [OSDev Wiki — ELF](https://wiki.osdev.org/ELF) — free, authoritative
- [Wikipedia — Executable and Linkable Format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) — free overview

## Related terms
- [Linker](linker.md)
- [Assembler](assembler.md)
- [Multiboot](multiboot.md)
- [Cross-Compiler](cross-compiler.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
