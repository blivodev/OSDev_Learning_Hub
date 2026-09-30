# GLOSSARY MASTER TERM LIST — authoritative slugs, tooltips, and which doc grounds each term

This file is the single source of truth for the glossary. Every term below
must get its own Markdown page in this `GLOSSARY/` directory, named `<slug>.md`.
Do NOT rename these slugs — the docs link to them. Each page follows
`GLOSSARY/_template.md`.

Format of each row:  `slug` | `Term (as it appears in docs)` | `one-line tooltip (shown on hover)`

## Boot & firmware
- `bios` | Basic Input/Output System (BIOS) | "The firmware stored on the motherboard that starts the machine and finds a bootloader"
- `uefi` | Unified Extensible Firmware Interface (UEFI) | "Modern replacement for BIOS; boots into 64-bit long mode natively"
- `firmware` | Firmware | "Software permanently stored on the motherboard that runs first at power-on"
- `bootloader` | Bootloader | "A small program that loads your kernel into memory and jumps to it"
- `multiboot` | Multiboot | "The protocol that lets a standard bootloader load any kernel; magic 0x1BADB002"
- `entry-point` | Entry point | "The symbol (usually _start) the bootloader jumps to when your kernel starts"
- `real-mode` | Real mode | "The 16-bit CPU mode the x86 starts in, with no memory protection"
- `protected-mode` | Protected mode | "The 32-bit CPU mode Multiboot v1 loads kernels into"
- `long-mode` | Long mode | "The 64-bit CPU mode modern kernels run in"
- `grub` | GRUB | "A free, standard bootloader (GNU Grand Unified Bootloader)"
- `limine` | Limine | "A modern bootloader supporting Multiboot 2 and 64-bit kernels"

## Kernel & runtime
- `kernel` | Kernel | "The core program that owns the machine and manages hardware for other software"
- `freestanding` | Freestanding environment | "Compiling code that assumes no OS or standard library exists"
- `hosted` | Hosted environment | "A normal program that assumes an OS and libc exist underneath"
- `no_std` | no_std | "A Rust attribute that disables the standard library to run on bare metal"
- `no_main` | no_main | "A Rust attribute that disables the normal main() runtime"
- `panic-handler` | Panic handler | "The function that runs when a Rust kernel panics, since there is no OS to report to"
- `memory-management` | Memory management | "How a kernel tracks used and free RAM and hands it out safely"
- `paging` | Paging / page tables | "The CPU feature that translates virtual addresses to physical RAM via page tables"
- `heap-allocation` | Heap allocation | "Dynamically allocating memory at runtime, which a kernel must implement itself"
- `garbage-collection` | Garbage collection (GC) | "Automatic memory reclamation; required by managed runtimes like Go and C#"
- `frame-allocator` | Frame allocator | "The simplest memory manager that tracks which 4 KiB physical pages are free"
- `physical-virtual-memory` | Physical vs virtual memory | "Real RAM addresses vs the addresses your code sees after paging"

## CPU & interrupts
- `interrupt` | Interrupt | "A hardware signal that makes the CPU pause and run a registered handler"
- `idt` | Interrupt Descriptor Table (IDT) | "The kernel's table that tells the CPU where each interrupt handler lives"
- `isr` | Interrupt Service Routine (ISR) | "The handler function run for a specific interrupt number"
- `pic-apic` | PIC / APIC | "Chips that route hardware interrupts (timer, keyboard) to the CPU"
- `gdt` | Global Descriptor Table (GDT) | "A table describing memory segments the CPU uses in protected mode"
- `hlt-instruction` | hlt | "The CPU instruction that parks the CPU until an interrupt wakes it"
- `syscall` | System call | "The way user programs ask the kernel for services"
- `extern-c` | extern "C" | "C++ keyword that gives a function C linkage so its name isn't mangled"

## Display
- `vga-text-mode` | VGA text mode | "The 80x25 character display mode a minimal kernel writes to"
- `vga-framebuffer` | VGA framebuffer (0xB8000) | "The block of memory at 0xB8000 where the screen text lives"

## Toolchain & build
- `cross-compiler` | Cross-compiler | "A compiler that produces code for a different CPU/OS than the one it runs on"
- `assembler` | Assembler (NASM / GAS) | "A tool that turns assembly language into machine-code object files"
- `linker` | Linker / linker script | "The tool that merges object files into one image at a chosen address"
- `elf` | ELF | "The executable format that lets a bootloader load your kernel at a chosen address"
- `qemu` | QEMU | "A free emulator you can boot your kernel in for testing"
- `make` | Make / Makefile | "A build tool that runs compile commands from a Makefile"
- `bootloader-crate` | bootloader crate | "A Rust crate that wraps a kernel into a bootable disk image for you"
- `bootimage` | bootimage | "The tool that invokes the bootloader crate to make a bootable image"
- `cargo` | Cargo | "The Rust package manager and build tool"
- `gccgo` | gccgo | "The Go front-end of GCC, used to compile Go kernels bare-metal"
- `cosmos` | Cosmos OS | "An open-source C# operating-system kit"
- `nativeaot` | NativeAOT | ".NET's ahead-of-time compiler used by Cosmos to turn IL into native code"
- `il2cpu` | IL2CPU | "Cosmos's original IL-to-x86 compiler (now superseded by NativeAOT)"
- `managed-il` | Managed IL | "The intermediate language C# compiles to, which needs a runtime"
- `rustup` | Rust | "Used where docs reference the Rust toolchain (rustup/cargo)"

## Hardware & minsc
- `x86` | x86 / x86_64 | "The CPU architecture family this hub targets"
- `memory-mapped-io` | Memory-mapped I/O | "Hardware that is controlled by writing to regular memory addresses"
- `text-mode-cursor` | Cursor | "The current position in the VGA text buffer where the next char is written"

---

This is the contract: match these slugs EXACTLY in links (e.g. `[Multiboot](GLOSSARY/multiboot.md "tooltip")`). Tooltips may be trimmed, but keep the meaning.
