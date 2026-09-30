<!-- GLOSSARY PAGE — uefi.md -->

# Unified Extensible Firmware Interface (UEFI)

> **[Back to glossary index](README.md)** · Category: Boot & firmware

**UEFI** (Unified Extensible Firmware Interface) is the modern replacement for BIOS — motherboard firmware that is 64-bit native, boots the CPU directly into long mode, and hands control to a bootloader.

## The short version
UEFI is the contemporary firmware standard that every modern PC actually ships with. Unlike BIOS, it is a 64-bit native environment and it boots the CPU straight into 64-bit long mode rather than starting in 16-bit real mode. For OS development this changes the whole shape of the boot: a UEFI path goes from UEFI straight to a modern bootloader like [Limine](limine.md) (or the Rust `bootloader` crate) and then to a 64-bit kernel — no detour through 32-bit protected mode.

## Detailed explanation
Where BIOS is a glorified 16-bit ROM program, UEFI is a proper specification with a full runtime API, a driver model, and a boot manager. The motherboard's firmware implements the UEFI spec, and at power-on it initializes the memory controller and device hardware, then hands off to a boot manager that can load an OS loader or kernel directly from an EFI system partition (ESP). The key architectural difference from BIOS is that the CPU is put into **64-bit long mode** up front, so 64-bit kernels and 64-bit bootloaders can run natively.

This matters enormously for a kernel developer. On the BIOS path the bootloader must wrestle the CPU out of real mode into protected mode before it can load even a 32-bit kernel. On the UEFI path none of that 16-bit/32-bit shuffling is needed — a 64-bit kernel is loaded directly. The trade-off is complexity: UEFI brings a real API, EFI system partitions, driver protocols, and mandatory Secure Boot considerations, which is a lot more machinery than the "read a sector and jump" BIOS model.

The hub draws the two firmware worlds side by side in `01-how-a-computer-boots.md`: the BIOS path (BIOS → 16-bit real mode → GRUB → 32-bit protected mode) versus the UEFI path (UEFI → 64-bit long mode → Limine / bootloader crate → 64-bit kernel). UEFI is "modern and 64-bit native, but more complex."

For learning, the hub notes that **BIOS + GRUB/Multiboot** (or the Rust `bootloader` crate for a UEFI path) is the smoothest way to start, and that is the path `Example_OS_Project` uses — so this hub's tutorials emphasize the BIOS/Multiboot route while acknowledging UEFI as the modern alternative.

```mermaid
flowchart LR
    B1[UEFI] --> B2[64-bit long mode]
    B2 --> B3[Limine / bootloader crate]
    B3 --> B4[64-bit kernel]
```

## Why it matters here (OSDev_Learning_Hub)
The hub's `synthesized_tutorials/00-introduction/01-how-a-computer-boots.md` chapter explicitly sets up the UEFI path as the modern alternative to BIOS, booting into 64-bit [Long Mode](long-mode.md) and using [Limine](limine.md) or the Rust `bootloader` crate rather than GRUB. While the `Example_OS_Project` kernels boot through the simpler BIOS + Multiboot route (see `c/boot.s`), the docs make clear that UEFI is what a modern production OS would target, and that it starts in [Long Mode](long-mode.md) instead of [Real Mode](real-mode.md).

## Watch / listen
[- Windows Secure Boot Compromised! - Dave's Garage](https://www.youtube.com/watch?v=7sYzwb6eUgQ) — explains how UEFI secure boot works and why it matters
- [OSDev Wiki — UEFI](https://wiki.osdev.org/UEFI) — free, authoritative
- [Wikipedia — UEFI](https://en.wikipedia.org/wiki/UEFI) — free overview of the specification

## Related terms
- [BIOS](bios.md)
- [Firmware](firmware.md)
- [Limine](limine.md)
- [Long Mode](long-mode.md)
- [Bootloader](bootloader.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
