# Path A — C → Operating System Development (Beginner)

The **most beginner-friendly, free C OS-dev track** we selected.

## Primary Resources

### 1. Operating Systems: From 0 to 1 — Doh Tu (tuhdo)
- **Where:** https://github.com/tuhdo/os01 | https://tuhdo.github.io/os01/
- **License:** Free (GitHub-distributed book)
- **Local copy:** [`Operating_Systems_From_0_to_1.pdf`](Operating_Systems_From_0_to_1.pdf)
- **Why chosen:** The single best free book that bootstraps a self-learner from *assembler + C* all the way to *linking/loading a bare-metal x86_64 kernel* in pure C — no standard library, no runtime. Famous, well-regarded (13k+ GitHub stars), text-heavy with diagrams.
- **What it teaches:** Linux dev environment + low-level tools, [x86](../GLOSSARY/x86.md "The CPU architecture family this hub targets") assembly in depth, [ELF](../GLOSSARY/elf.md "The executable format that lets a bootloader load your kernel"), program structure, debugging bare metal with **GDB + [QEMU](../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing")**, linking/loading on x86_64 in pure C.

### 2. OSDev Wiki — Bare Bones (C)
- **Where:** https://wiki.osdev.org/Bare_Bones
- **License:** Open wiki (community-reviewed, CC/GFDL-style)
- **Local copy:** [`Bare_Bones_C.md`](Bare_Bones_C.md)
- **Why chosen:** The canonical, community-reviewed minimal-kernel tutorial for absolute beginners. 32-bit [x86](../GLOSSARY/x86.md "The CPU architecture family this hub targets") kernel booted by **[GRUB](../GLOSSARY/grub.md "The free GNU bootloader that loads Multiboot kernels") + [Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002")**, with the standard VGA text-mode driver. Uses GCC `-ffreestanding`.

## What you'll build in this path
A minimal kernel that prints **"Hello World!"** to the VGA text-mode framebuffer at `0xB8000`, booted by [GRUB](../GLOSSARY/grub.md "The free GNU bootloader that loads Multiboot kernels")/[Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002").

## Supporting material already in this hub
- Fully-commented minimal implementation → [`Example_OS_Project/c/`](../Example_OS_Project/c/)
- Synthesized consolidated beginner guide → [`synthesized_tutorials/01-c/`](../synthesized_tutorials/01-c/)

## Toolchain needed (see `Example_OS_Project/docs/setup.md`)
`gcc` (i686-elf cross for real targets; x86_64 native for QEMU test), `nasm`, `ld`, `make`, `qemu-system-x86_64`, `xorriso` (for ISO).
