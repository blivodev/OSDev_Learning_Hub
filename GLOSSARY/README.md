# OSDev Glossary

**Inline tooltips + deep-dive pages for every technical term used in this hub.**

Throughout the docs you'll see technical terms as **linked, underlined-blue text**:

- **Hover** over the link → a short **tooltip** summarizes the term.
- **Click** the link → lands on this glossary page for a detailed explanation with diagrams and further reading.

## How the tooltips work
Every term is written in Markdown as a link with a *title* attribute, which renders as a native tooltip on GitHub, Gitea, and most Markdown viewers:

```markdown
Write to the [VGA framebuffer](vga-text-mode.md "The 80x25 text buffer at 0xB8000 that a kernel writes to directly") at 0xB8000.
```

The `"..."` after the link is the tooltip text shown on hover.

## Repository index (alphabetical)

### Boot & firmware
- [Basic Input/Output System (BIOS)](bios.md)
- [Unified Extensible Firmware Interface (UEFI)](uefi.md)
- [Firmware](firmware.md)
- [Bootloader](bootloader.md)
- [Multiboot](multiboot.md)
- [Entry Point (`_start`)](entry-point.md)
- [Real Mode](real-mode.md)
- [Protected Mode](protected-mode.md)
- [Long Mode](long-mode.md)
- [GRUB](grub.md)
- [Limine](limine.md)

### The kernel
- [Kernel](kernel.md)
- [Freestanding Environment](freestanding.md)
- [Hosted Environment](hosted.md)
- [`no_std`](no_std.md)
- [`no_main`](no_main.md)
- [Panic Handler](panic-handler.md)
- [Memory Management](memory-management.md)
- [Paging / Page Tables](paging.md)
- [Heap Allocation](heap-allocation.md)
- [Frame Allocator](frame-allocator.md)
- [Physical vs Virtual Memory](physical-virtual-memory.md)

### CPU & interrupts
- [Hardware Interrupt](interrupt.md)
- [Interrupt Descriptor Table (IDT)](idt.md)
- [Interrupt Service Routine (ISR)](isr.md)
- [PIC / APIC](pic-apic.md)
- [Global Descriptor Table (GDT)](gdt.md)
- [`hlt` Instruction](hlt-instruction.md)
- [GCC Runtime / unmangled symbol & `extern "C"`](extern-c.md)

### Display
- [VGA Text Mode](vga-text-mode.md)
- [VGA Framebuffer (`0xB8000`)](vga-framebuffer.md)
- [Text-Mode Cursor](text-mode-cursor.md)
- [Memory-Mapped I/O](memory-mapped-io.md)

### Toolchain & build
- [Compiler / Cross-Compiler](cross-compiler.md)
- [Assembler (NASM / GAS)](assembler.md)
- [Linker / Linker Script](linker.md)
- [ELF](elf.md)
- [QEMU](qemu.md)
- [`Makefile` / Make](make.md)
- [Rust `bootloader` crate](bootloader-crate.md)
- [`bootimage`](bootimage.md)
- [`cargo`](cargo.md)
- [`rustup`](rustup.md)
- [gccgo](gccgo.md)
- [Cosmos OS](cosmos.md)
- [NativeAOT](nativeaot.md)
- [IL2CPU](il2cpu.md)
- [Managed IL](managed-il.md)

### Concepts
- [Garbage Collection (GC)](garbage-collection.md)
- [System Call](syscall.md)

### Hardware
- [x86 / x86_64](x86.md)

---

A good place to start is the [Synthesized Beginner Guide](../synthesized_tutorials/README.md), which links every concept to its glossary page as you read.
