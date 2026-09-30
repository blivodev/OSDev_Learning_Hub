<!-- Glossary page — QEMU. Grounded in OSDev_Learning_Hub docs. -->

# QEMU

> **[Back to glossary index](README.md)** · Category: Toolchain & build

QEMU is a free, open-source emulator that runs your kernel like a real PC on your desktop — safely and instantly.

## The short version
You can't reboot a real machine every time you change your kernel, so the hub tests in QEMU. QEMU emulates an entire PC (CPU, memory, VGA, disk, keyboard) and boots a kernel exactly like real hardware, but in a window on your normal OS. It's the fourth of the "four pillars" of kernel development, after the assembler, compiler, and linker.

## Detailed explanation
QEMU can boot a Multiboot kernel two main ways, and this hub uses both:

```bash
# 1. 32-bit C/C++/Go kernel — a Multiboot ELF loaded directly:
qemu-system-i386 -kernel kernel.bin

# 2. Rust kernel — a bootable disk image (produced by the bootloader crate):
qemu-system-x86_64 -drive format=raw,file=bootimage-example_os_rust.bin

# 3. Optional ISO (built with grub-mkrescue + xorriso):
qemu-system-i386 -cdrom Example_OS_C.iso
```

The first form uses QEMU's built-in Multiboot loader (it scans the ELF for the `0x1BADB002` magic and loads it at 1 MiB). The Rust form boots a whole disk image because the `bootloader` crate produces a BIOS-bootable raw disk, not a Multiboot ELF — so it uses `-drive format=raw,file=...` with the `x86_64` emulator.

Why QEMU and not a real PC? The tutorial puts it plainly: *"QEMU lets you boot your kernel millions of times a day without rebooting your PC. It's also scriptable, so your Makefile can build-and-boot in one command."* The `run` targets in the Makefiles wrap exactly the commands above.

```mermaid
flowchart LR
    K[kernel.bin / disk image] --> Q[qemu-system-i386 / -x86_64]
    Q --> V["Hello World! on VGA"]
```

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/c/Makefile` and `cpp/Makefile`: the `run` target does `qemu-system-i386 -kernel $(BIN)`.
- `Example_OS_Project/rust/Makefile`: `$(QEMU) -drive format=raw,file=target/$(TARGET)/debug/bootimage-example_os_rust.bin` where `QEMU ?= qemu-system-x86_64`.
- `Example_OS_Project/go/README.md`: `qemu-system-i386 -kernel kernel.bin`.
- `Example_OS_Project/csharp/README.md`: `qemu-system-i386 -cdrom bin/Debug/MyOS.iso` for the Cosmos ISO.
- The hub ships tools that read the screen back from QEMU, e.g. `Example_OS_Project/tools/read_vga_text.py`.

## Watch / listen
[- QEMU/KVM for absolute beginners - Veronica Explains](https://www.youtube.com/watch?v=BgZHbCDFODk) — running virtual machines with QEMU
- [QEMU — Official site](https://www.qemu.org/) — free, authoritative
- [OSDev Wiki — QEMU](https://wiki.osdev.org/QEMU) — free and specific to kernel testing

## Related terms
- [Bootloader](bootloader.md)
- [Multiboot](multiboot.md)
- [Linker](linker.md)
- [make](make.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
