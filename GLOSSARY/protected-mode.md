<!-- GLOSSARY PAGE — protected-mode.md -->

# Protected Mode

> **[Back to glossary index](README.md)** · Category: Boot & firmware

**Protected mode** is the 32-bit CPU mode with memory protection and privilege levels that Multiboot v1 loads kernels into — the mode most x86 "bare bones" kernels actually run in.

## The short version
After real mode, the next step up the x86 CPU is protected mode: 32-bit registers and, crucially, memory protection and privilege rings. This is the mode that **Multiboot v1** (the classic `0x1BADB002` protocol) delivers before jumping to your kernel. When the CPU is in protected mode, a kernel can address real RAM with full 32-bit pointers and can use the Global Descriptor Table (GDT) to describe memory segments and enforce protection between privilege levels.

## Detailed explanation
Real mode's lack of memory protection means any buggy or malicious program can clobber any memory. Protected mode fixes that by introducing **segmentation with protection** and **privilege levels** (rings). Every memory access goes through the Global Descriptor Table (GDT), which describes segments and what each segment is allowed to do, and the CPU enforces it — a program running at an unprivileged ring cannot touch memory it isn't allowed to and cannot execute privileged instructions. Registers are widened to 32 bits, so a kernel can address up to 4 GiB of flat memory with a single 32-bit pointer.

For OS development, protected mode is the "baseline capable" mode. It is what the classic **Multiboot v1** protocol sets up: the bootloader (GRUB) transitions the CPU from real mode into 32-bit protected mode, loads your kernel at 1 MiB, and then jumps to `_start` with the CPU already in protected mode. Your kernel can then immediately run 32-bit code, write to the VGA framebuffer, set up its own GDT/IDT, and manage memory — none of which is possible in the 16-bit real mode it started in.

Protected mode is the middle step of the boot chain. On the BIOS path, a 64-bit kernel still must pass through 32-bit protected mode to get to **long mode**: real mode → protected mode → long mode. On the UEFI path this detour is skipped because UEFI boots the CPU straight into 64-bit long mode.

```mermaid
flowchart LR
    RM[Real mode 16-bit] --> PM[Protected mode 32-bit]
    PM --> LM[Long mode 64-bit]
```

## Why it matters here (OSDev_Learning_Hub)
The `synthesized_tutorials/concepts/01-bootloaders-and-multiboot.md` concept page notes that Multiboot v1 (`0x1BADB002`) is the 32-bit protocol "what most Bare Bones tutorials use," and `synthesized_tutorials/00-introduction/01-how-a-computer-boots.md` draws the BIOS path ending at "Protected mode 32-bit" before the kernel runs. The `Example_OS_Project` kernels run in 32-bit protected mode once [GRUB](grub.md) loads them: `Example_OS_Project/c/boot.s` executes `movl`, `call`, `cli`, and `hlt` — all real machine instructions that rely on the protected-mode CPU state the bootloader establishes. See also [Real Mode](real-mode.md), [Long Mode](long-mode.md), and [Multiboot](multiboot.md).

## Watch / listen
[- How a Single Bit Inside Your Processor Shields Your OS's Integrity - Core Dumped](https://www.youtube.com/watch?v=H4SDPLiUnv4) — CPU privileged vs restricted execution modes
- [OSDev Wiki — Protected Mode](https://wiki.osdev.org/Protected_Mode) — free, authoritative
- [Wikipedia — Protected mode](https://en.wikipedia.org/wiki/Protected_mode) — free overview

## Related terms
- [Real Mode](real-mode.md)
- [Long Mode](long-mode.md)
- [Multiboot](multiboot.md)
- [Bootloader](bootloader.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
