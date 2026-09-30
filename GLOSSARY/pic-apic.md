<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# PIC / APIC

> **[Back to glossary index](README.md)** · Category: CPU & interrupts

The PIC (Programmable Interrupt Controller) and its modern replacement the APIC are the chips that route hardware interrupt signals (timer, keyboard) from devices to the CPU.

## The short version
Hardware devices like the timer and keyboard don't drive the CPU directly — they signal an interrupt controller, which decides whether to forward the request to the CPU. The traditional 8259 PIC delivers IRQs; the modern Intel/AMD APIC supersedes it. The controller also lets a kernel *remap* IRQs so they don't collide with CPU exception vectors.

## Detailed explanation
The classic x86 setup has (at least) two cascaded 8259 PICs providing **15 hardware IRQ lines** (the timer on IRQ 0, the keyboard on IRQ 1). Each PIC is programmed over I/O ports. By default IRQs map to vectors 0–15, which collide with CPU exceptions — so part of interrupt setup is **remapping** the PIC so the hardware IRQs land higher, typically at vectors 32–47. After the remap, the tutorial's table shows the timer at vector 32 and the keyboard at 33.

```c
// Remap by writing new base vectors to the PIC's I/O ports (0x20/0x21, 0xA0/0xA1).
// ...pic remap code that sets the timer IRQ to vector 32, keyboard to 33...
```

The APIC is the successor: the local APIC sits inside the CPU and the I/O APIC routes external interrupts, supporting many more devices and, crucially, working per-CPU so interrupts can be directed to a specific core. On modern hardware the bootloader (or a boot protocol like Multiboot/AP) puts the machine in a state where an APIC driver is appropriate, though a simple PIC remap still suffices for a single-CPU beginner kernel.

Whichever controller you program, the outcome is the same pair of facts the [IDT](idt.md) table encodes: after remap, **hardware IRQs occupy vectors 32–47**, distinct from CPU exceptions (0–31) and software interrupts (48–255).

## Why it matters here (OSDev_Learning_Hub)
`03-interrupts-and-the-idt.md` lists the PIC/APIC as one of the pieces you set up for interrupts and relies on the remap in its 256-slot table (timer 32, keyboard 33). The current `Example_OS_Project` kernel doesn't configure the PIC yet — it prints and halts — so adding IRQ routing is a clear next step after the [IDT](idt.md) and [ISR](isr.md).

## Watch / listen
- [OSDev Wiki — Programmable Interrupt Controller](https://wiki.osdev.org/Programmable_Interrupt_Controller) — free, authoritative
- [OSDev Wiki — APIC](https://wiki.osdev.org/APIC) — free, authoritative
- [Wikipedia — Programmable Interrupt Controller](https://en.wikipedia.org/wiki/Programmable_Interrupt_Controller) — free, authoritative

## Related terms
- [Hardware Interrupt](interrupt.md)
- [Interrupt Descriptor Table (IDT)](idt.md)
- [Interrupt Service Routine (ISR)](isr.md)
- [System Call](syscall.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
