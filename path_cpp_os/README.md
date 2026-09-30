# Path C — C++ → Operating System Development (Beginner)

A **free C++ OS-dev track** for when you already know a little C++.

## Primary Resource

### OSDev Wiki — Bare Bones (C++ variant)
- **Where:** https://wiki.osdev.org/Bare_Bones
- **License:** Open wiki (community-reviewed)
- **Local copy:** [`Bare_Bones_Cpp.md`](Bare_Bones_Cpp.md)
- **Why chosen:** The canonical free minimal-kernel tutorial, with an explicit C++ section. Writing a kernel in C++ is easy — you just give `kernel_main` [**C linkage**](../GLOSSARY/extern-c.md "C++ keyword giving a function C linkage so its name isn't mangled") (`extern "C"`) and compile with `-ffreestanding -fno-exceptions -fno-rtti`.
- **Key C++ specifics:**
  - `extern "C" void kernel_main()` — C linkage so the symbol name isn't mangled (the bootloader stub can call it).
  - Compile with `-ffreestanding -O2 -fno-exceptions -fno-rtti`.
  - Exceptions and RTTI are **not** available without runtime support — a great beginner lesson.

## What you'll build in this path
A minimal C++ kernel ([VGA text mode](../GLOSSARY/vga-text-mode.md "The 80x25 character display mode a minimal kernel writes to")) with an `extern "C"` entry point, booted by [GRUB](../GLOSSARY/grub.md "The free GNU bootloader that loads Multiboot kernels")/[Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002").

## Supporting material already in this hub
- Fully-commented minimal implementation → [`Example_OS_Project/cpp/`](../Example_OS_Project/cpp/)
- Synthesized consolidated beginner guide → [`synthesized_tutorials/03-cpp/`](../synthesized_tutorials/03-cpp/)

## Toolchain needed (see `Example_OS_Project/docs/setup.md`)
`g++` (i686-elf cross for real targets), `nasm`, `ld`, `make`, `qemu-system-x86_64`.
