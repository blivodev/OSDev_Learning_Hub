<!-- GLOSSARY PAGE — bios.md -->

# Basic Input/Output System (BIOS)

> **[Back to glossary index](README.md)** · Category: Boot & firmware

The **BIOS** (Basic Input/Output System) is the older firmware burned onto the motherboard that runs the moment the power button is pressed, runs a self-test, finds a bootable disk, and hands control to a bootloader.

## The short version
BIOS is the original "first program" on an x86 PC, stored in ROM on the motherboard rather than on your disk. Its only true job at boot time is to run a power-on self-test (POST), scan your drives for something bootable, and then jump into whatever bootloader it finds. Because it predates 64-bit computing, it starts the CPU in 16-bit real mode, which is why any BIOS-path kernel must be loaded into a 32-bit protected mode first (exactly what Multiboot v1 and GRUB do).

## Detailed explanation
When you press power, the CPU has no idea what an OS or a filesystem is. The BIOS is code permanently stored on the motherboard (in ROM/flash), and the CPU is hardwired to start executing the BIOS's code at the reset vector. The BIOS performs a **power-on self-test (POST)** to check memory and basic hardware, then it scans the drives for a bootable medium — a disk whose first sector carries a valid boot signature. When it finds one, the CPU jumps into the bootloader stored there, and the BIOS's active role is over.

The defining characteristic of the BIOS boot path is **16-bit real mode**. The processor starts in real mode with no memory protection, and the BIOS itself is 16-bit firmware. That means the firmware portion of the chain runs in real mode, and a 32-bit or 64-bit kernel cannot simply run on top of it — something has to move the CPU into 32-bit protected mode first. That "something" is the bootloader.

Modern machines still contain a BIOS, but almost all of them actually ship with UEFI and run a **Compatibility Support Module (CSM)** that emulates the old BIOS behavior. From a software point of view this is largely transparent: the boot chain still looks like the classic BIOS story. For a beginning OS developer this is actually a feature — it means a tiny, well-understood bootloader like GRUB can move the CPU from real mode into protected mode and load your kernel, so you don't have to re-implement the boot process yourself.

Because the BIOS reserves the **low 1 MiB** of memory for its own data structures, interrupt vectors, and video buffers, kernels are conventionally loaded **at or above 1 MiB** (`0x100000`) so they do not stomp on BIOS-owned memory. Your linker script places the kernel there with `. = 1M;`.

```mermaid
flowchart LR
    A1[BIOS] --> A2[16-bit real mode]
    A2 --> A3[GRUB boots]
    A3 --> A4[Protected mode 32-bit]
    A4 --> A5[Your kernel at 1 MiB]
```

## Why it matters here (OSDev_Learning_Hub)
The `synthesized_tutorials/00-introduction/01-how-a-computer-boots.md` chapter describes the BIOS path in detail — the power-on self-test, the scan for a bootloader, and the jump into it — and explains that BIOS boots into 16-bit real mode first, then relies on a bootloader to reach 32-bit protected mode. It is the firmware world that the hub's canonical **BIOS + GRUB/Multiboot** learning path sits on top of. The hub's bootloader ([GRUB](grub.md)) is what moves the CPU out of BIOS's real mode and into [Protected Mode](protected-mode.md) so it can load the kernel at [1 MiB](multiboot.md) via [Multiboot](multiboot.md).

## Watch / listen
[- How Computers BOOT: From Startup to Viruses - Dave's Garage](https://www.youtube.com/watch?v=rmgla4yeCXw) — walks the full BIOS boot chain, from reset to OS
- [OSDev Wiki — BIOS](https://wiki.osdev.org/BIOS) — free, authoritative
- [Wikipedia — BIOS](https://en.wikipedia.org/wiki/BIOS) — free overview of the boot firmward and its history

## Related terms
- [UEFI](uefi.md)
- [Firmware](firmware.md)
- [Bootloader](bootloader.md)
- [Multiboot](multiboot.md)
- [Real Mode](real-mode.md)
- [Protected Mode](protected-mode.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
