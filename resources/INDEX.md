# Resources — Additional Material & Links

Curated list of free, beginner-friendly OS-development material beyond the primary per-path selections.

## Core learning (all free)
- **OSDev Wiki** — https://wiki.osdev.org — *the* community reference. Start with: Getting Started, Beginner Mistakes, Bare Bones, Meaty Skeleton, VGA font/graphics, [Interrupts](../GLOSSARY/interrupt.md "A hardware signal that makes the CPU run a registered handler"), [Paging](../GLOSSARY/paging.md "Translates virtual addresses to physical RAM via page tables").
- **OSDev Wiki — Meaty Skeleton** — https://wiki.osdev.org/Meaty_Skeleton — a clean project-structure template (kernel + libk split).
- **Little OS Book** — a concise, beginner-friendly guide to a minimal OS in C (small practical examples covering booting, interrupts, memory).
- **Baeldung: How to Start Building an OS** — https://www.baeldung.com/cs/building-os — good high-level orientation with links by language.

## By language (path folders reference these)
| Path | Resource | Link |
|------|----------|------|
| C | Operating Systems: From 0 to 1 | https://github.com/tuhdo/os01 |
| C | OSDev Bare Bones | https://wiki.osdev.org/Bare_Bones |
| C | James Molloy's Kernel Development Tutorials | http://www.jamesmolloy.co.uk/tutorial_html/ |
| C | BrokenThorn OS Dev Series | http://www.brokenthorn.com/Resources/OSDevIndex.html |
| C++ | OSDev Bare Bones (C++) | https://wiki.osdev.org/Bare_Bones |
| C++ | thor-os (C++ OS example) | https://github.com/wichtounet/thor-os |
| Rust | Writing an OS in Rust | https://os.phil-opp.com/ |
| Rust | OSDev Raspberry Pi Bare Bones (Rust) | https://wiki.osdev.org/Raspberry_Pi_Bare_Bones |
| Go | OSDev Go Bare Bones | https://wiki.osdev.org/Go_Bare_Bones |
| Go | eggos (Go unikernel) | https://github.com/alexflint/eggos |
| Go | go-dav-os | https://github.com/dmarro89/go-dav-os |
| C# | Cosmos OS | https://www.gocosmos.org/ / https://github.com/CosmosOS/Cosmos |
| Any | OSDev forums | https://forum.osdev.org/ |

## Hardware / manuals (free)
- **Intel 64 & IA-32 Architectures Software Developer's Manuals** — free PDF from Intel (Programmer's ref for [x86](../GLOSSARY/x86.md "The CPU architecture family this hub targets")).
- **OSDev wiki's "Resources" page** — hundreds of free datasheets & specs.

## Nice-to-know
- **[QEMU](../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing")** (emulator): https://www.qemu.org/
- **NASM** ([assembler](../GLOSSARY/assembler.md "Turns assembly language into machine-code object files")): https://www.nasm.us/
- **[GRUB](../GLOSSARY/grub.md "The free GNU bootloader that loads Multiboot kernels")** ([bootloader](../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it")): https://www.gnu.org/software/grub/
- **[Limine](../GLOSSARY/limine.md "A modern bootloader supporting Multiboot 2 and 64-bit kernels")** (modern [bootloader](../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") used by [Cosmos](../GLOSSARY/cosmos.md "An open-source C# operating-system kit") & Rust bootloader): https://limine-bootloader.org/


## Video resources

Curated YouTube playlists and single videos for visual learners, matched to the hub's paths.

- [Write Your Own 64-bit Operating System Kernel #1 - Boot code and multiboot header](https://www.youtube.com/watch?v=FkrpUaGThTQ) — David Callanan's series, a clean C/assembly kernel walkthrough for any path.
- [Write Your Own 64-bit Operating System Kernel #2 - Stack, long mode and printing using C code](https://www.youtube.com/watch?v=wz9CZBeXR6U) — continues into long mode, stack setup and printing.
- [Writing an OS in Rust - Part 1 - A Freestanding Rust Binary](https://www.youtube.com/watch?v=rH5jnbJ3tL4) — visual companion to the Rust `no_std` path (os.phil-opp.com).
- [1 - How to make an operating system from scratch](https://www.youtube.com/watch?v=rr-9w2gITDM) — a general OSdev-from-scratch walkthrough for beginners of any language.
- [GopherCon 2025: An Operating System in Go - Patricio Whittingslow](https://www.youtube.com/watch?v=SvsdVe1kgSU) — an OS-in-Go talk for the Go/Bare Bones path.
- [Cosmos Tutorial Part 1 - Setting Up And First Command!](https://www.youtube.com/watch?v=RTkeqkFzC3w) — the C#/Cosmos path in action.
- [How does an OS boot? //Source Dive// 001](https://www.youtube.com/watch?v=KkenLT8S9Hs) — Low Byte Productions on the boot process behind every kernel here.
- [QEMU/KVM for absolute beginners](https://www.youtube.com/watch?v=BgZHbCDFODk) — learn the emulator all paths boot their kernels in.
