<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# Interrupt Service Routine (ISR)

> **[Back to glossary index](README.md)** · Category: CPU & interrupts

An Interrupt Service Routine (ISR) is the handler function the CPU runs for a specific interrupt number after it is dispatched through the [IDT](idt.md).

## The short version
The ISR is the "actual work" half of the interrupt pair: the [IDT](idt.md) says *where* to jump, and the ISR is *what runs* there. In the tutorial's Rust example a timer ISR is as simple as a function that runs when the timer fires — the seed of a whole scheduling system.

## Detailed explanation
When an interrupt fires and the CPU finds the matching entry in the [IDT](idt.md), it jumps to the ISR for that vector. The ISR runs with interrupts typically masked and must save and restore any register state it touches, then return with `iret` (interrupt return) rather than a normal `ret`, because the CPU pushed extra state for the interrupted context. A keyboard ISR might read a scan code; a timer ISR might kick the scheduler.

Because writing ISR entry glue by hand is fiddly, high-level languages provide calling conventions that do it for you. The tutorial shows the Rust approach:

```rust
extern "x86-interrupt" fn timer_interrupt_handler(_: InterruptStackFrame) {
    // a hardware timer just fired — a whole scheduling system starts here
}
```

The `x86-interrupt` convention makes the compiler emit the correct prologue/epilogue and `iret`. In lower-level C the entry shape is a fixed-function wrapper that the IDT points at, which usually pushes an error code, saves registers, calls a C handler, then restores and returns.

Each ISR is tied to one vector. The CPU exceptions (vectors 0–31) each have canonical ISRs, hardware [IRQs](interrupt.md) land at 32–47 after the [PIC](pic-apic.md) remap, and software [syscalls](syscall.md) sit in 48–255. Handling every slot is common in real kernels so an unregistered exception doesn't silently corrupt state.

## Why it matters here (OSDev_Learning_Hub)
`03-interrupts-and-the-idt.md` names the ISR as one of the pieces you set up for interrupts and shows the Rust timer ISR above. In `Example_OS_Project` the kernel currently does not use ISRs (it prints and halts), so this is the natural next milestone once you want a timer tick or a keyboard driver.

## Watch / listen
[- Building an OS - 8 - Interrupts, IDT, GDT - nanobyte](https://www.youtube.com/watch?v=5LbXClJhxcs) — writing interrupt service routines
- [OSDev Wiki — Interrupt Service Routines](https://wiki.osdev.org/Interrupt_Service_Routines) — free, authoritative
- [OSDev Wiki — Interrupt descriptor table and the IDT](https://wiki.osdev.org/Interrupt_Descriptor_Table) — free, authoritative

## Related terms
- [Hardware Interrupt](interrupt.md)
- [Interrupt Descriptor Table (IDT)](idt.md)
- [PIC / APIC](pic-apic.md)
- [System Call](syscall.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
