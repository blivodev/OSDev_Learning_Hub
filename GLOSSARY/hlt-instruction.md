<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# `hlt` Instruction

> **[Back to glossary index](README.md)** · Category: CPU & interrupts

The `hlt` (halt) instruction parks the CPU by stopping execution until an unmasked interrupt arrives to wake it.

## The short version
`hlt` stops the CPU consuming power until a hardware interrupt fires and resumes it. A kernel that has nothing to do — like the sample after printing "Hello World!" — should `hlt` rather than spin, because it saves power and lets the CPU wait for the next interrupt instead of busy-looping.

## Detailed explanation
`hlt` stops the processor and puts it into a halted, low-power state. The CPU resumes only when an unmasked [interrupt](interrupt.md) (a hardware [IRQ](pic-apic.md), a [syscall](syscall.md)-style software interrupt, or an NMI) occurs. This makes it the idiomatic "idle loop" instruction — but it is usually combined with `sti` (or used inside a loop that re-enables interrupts after each wake), so that the next interrupt can actually arrive. Since most interrupts are masked by default, a bare `hlt` with interrupts still off can freeze the machine.

In the sample bootstrap, `boot.s` shuts down cleanly:

```asm
    cli    /* clear the interrupt flag (no more irqs) */
    hlt    /* halt the CPU */
```

That sequence disables interrupts first so nothing can wake the CPU, then halts as a final shutdown. Because a CPU with interrupts disabled stays halted, the tutorial's suffix is a safety loop that catches even the case where execution somehow continues:

```asm
.Lhang:
    jmp .Lhang
```

A real kernel's idle path instead runs `sti; hlt` in a loop, so an interrupt wakes the CPU, runs its [ISR](isr.md), then the idle loop re-arms itself. The `hlt` instruction lives right at the end of the beginner flow in the tutorials: print to the [VGA framebuffer](vga-text-mode.md), then halt forever.

## Why it matters here (OSDev_Learning_Hub)
`Example_OS_Project/c/boot.s` ends with `cli` then `hlt` (the exact snippet above), and `kernel.c` "halts forever" with `for (;;) ;` as its kernel never returns. `04-vga-text-mode.md` repeats the pattern: `term_write("Hello World!")` then `for (;;) ;`. Understanding `hlt` is what turns those idle loops from a mystery into the standard low-power wait-for-interrupt mechanism.

## Watch / listen
- [OSDev Wiki — HLT](https://wiki.osdev.org/HLT) — free, authoritative
- [Wikipedia — HLT](https://en.wikipedia.org/wiki/HLT) — free, authoritative

## Related terms
- [Hardware Interrupt](interrupt.md)
- [Interrupt Descriptor Table (IDT)](idt.md)
- [PIC / APIC](pic-apic.md)
- [VGA Text Mode](vga-text-mode.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
