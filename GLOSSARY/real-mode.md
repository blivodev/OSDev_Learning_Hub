<!-- GLOSSARY PAGE — real-mode.md -->

# Real Mode

> **[Back to glossary index](README.md)** · Category: Boot & firmware

**Real mode** is the 16-bit CPU mode the x86 starts in at power-on, with no memory protection and direct access to hardware — the mode every BIOS-path boot chain begins in.

## The short version
When an x86 CPU powers on, it begins in real mode: 16-bit registers and no memory protection. This is the original mode of the very first 8086 processors, carried forward for backward compatibility. It is the mode the BIOS firmware runs in, and it is why any BIOS-path kernel cannot simply run after firmware — something (a bootloader) must move the CPU into a more capable mode first. Modern operating systems never actually run their kernel in real mode; they leave real mode as quickly as the bootloader allows.

## Detailed explanation
Real mode is the CPU's default, most primitive execution state. It is the mode the CPU is in the instant after reset, before any operating system or bootloader does anything. Register widths are 16-bit, and memory is accessed through the segmented model where an address is formed from a segment register and an offset (segment × 16 + offset). There is **no memory protection**: any code running in real mode can read or write any physical memory address and can execute privileged instructions freely, because there is no distinction between ring levels yet.

This is exactly the environment the classic **BIOS** firmware expects. The BIOS is 16-bit firmware, so the entire BIOS boot path runs in real mode: the CPU starts in real mode, runs the BIOS's POST, and the BIOS chain continues in 16-bit mode. That is why `synthesized_tutorials/00-introduction/01-how-a-computer-boots.md` draws the BIOS path as "BIOS → 16-bit real mode → GRUB boots → protected mode 32-bit." The bootloader (GRUB) is the piece that transitions the CPU out of real mode and into **protected mode** so it can load a modern kernel.

Real mode is also why modern BIOS emulation works the way it does: a UEFI machine running a Compatibility Support Module (CSM) reproduces the classic real-mode BIOS behavior so old bootloaders still work. But no real operating system ships a 32-bit or 64-bit kernel that runs in real mode — real mode exists at the very start of the chain and is exited before the kernel proper takes over.

```mermaid
flowchart LR
    A1[BIOS] --> A2[16-bit real mode]
    A2 --> A3[Bootloader transitions]
    A3 --> A4[Protected mode 32-bit]
```

## Why it matters here (OSDev_Learning_Hub)
In `synthesized_tutorials/00-introduction/01-how-a-computer-boots.md` real mode appears as the mode the BIOS path starts in — "BIOS is old, simple... It boots into a 16-bit mode first." The hub's canonical learning path (BIOS + [GRUB](grub.md) + [Multiboot](multiboot.md)) depends on the bootloader dragging the CPU out of real mode into [Protected Mode](protected-mode.md) so it can load the kernel at 1 MiB. The `Example_OS_Project` kernels assume protected (or via QEMU, directly) mode already — `Example_OS_Project/c/boot.s` writes straight to memory and calls C code, which requires the protected-mode CPU state the bootloader establishes.

## Watch / listen
[- How Computers BOOT: From Startup to Viruses - Dave's Garage](https://www.youtube.com/watch?v=rmgla4yeCXw) — shows the 16-bit real-mode start of boot
[- Intro to x86 Assembly Language (Part 1)](https://www.youtube.com/watch?v=wLXIWKUWpSs) — registers and real-mode machine code
- [OSDev Wiki — Real Mode](https://wiki.osdev.org/Real_Mode) — free, authoritative
- [Wikipedia — Real mode](https://en.wikipedia.org/wiki/Real_mode) — free overview

## Related terms
- [Protected Mode](protected-mode.md)
- [Long Mode](long-mode.md)
- [BIOS](bios.md)
- [Bootloader](bootloader.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
