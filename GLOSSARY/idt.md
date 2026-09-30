<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# Interrupt Descriptor Table (IDT)

> **[Back to glossary index](README.md)** · Category: CPU & interrupts

The Interrupt Descriptor Table (IDT) is the kernel's phonebook that tells the CPU where to jump for every one of the 256 possible interrupt numbers (0–255).

## The short version
The IDT is an array of 256 descriptors, one per interrupt vector. When an interrupt fires, the CPU looks up the vector in the IDT and jumps to the listed handler (an [ISR](isr.md)). You load the table with the `lidt` instruction and then enable interrupts with `sti`.

## Detailed explanation
The IDT is a flat array of descriptors — at minimum one entry per vector, up to the full **256 slots**. Each entry describes where the handler lives (its segment selector and offset, plus attributes like privilege level). The CPU must be told where the table is; the C tutorial does this by building a packed `struct idt_ptr` holding the limit and base address and executing `lidt`:

```c
struct idt_ptr { uint16_t limit; uint32_t base; } __attribute__((packed));
struct idt_ptr idtp;
// ... fill 256 idt_entry_t entries ...
__asm__ volatile("lidt (%0)" : : "r"(&idtp));
__asm__ volatile("sti");   // enable interrupts
```

Because the table is only an address/length pair, the IDT itself lives in normal RAM that the kernel allocates and fills. The Rust approach in the tutorial uses the `x86-interrupt` calling convention and a `lazy_static` `InterruptDescriptorTable`, setting a handler for the timer with `set_handler_fn`.

The 256 slots divide into three ownership ranges taught by the tutorial:

| Range | Who owns it | Example |
|-------|-------------|---------|
| 0–31 | **CPU exceptions** | #PF page fault (14), #GP general protection (13) |
| 32–47 | **Hardware IRQs** (after PIC remap) | timer (32), keyboard (33) |
| 48–255 | Software / your custom | syscalls, custom events |

The same IDs reused for hardware IRQs need the [PIC / APIC](pic-apic.md) remap so the timer and keyboard land at slots 32 and 33 instead of clashing with CPU exceptions.

## Why it matters here (OSDev_Learning_Hub)
`03-interrupts-and-the-idt.md` walks through building this exactly as above — the C `lidt` snippet and the Rust `extern "x86-interrupt"` timer handler both appear there. It is the first real OS feature most kernels implement after the [GDT](gdt.md), and it is the prerequisite for [syscalls](syscall.md), which occupy the 48–255 software range.

## Watch / listen
[- Building an OS - 8 - Interrupts, IDT, GDT - nanobyte](https://www.youtube.com/watch?v=5LbXClJhxcs) — setting up an IDT in a real OS
- [OSDev Wiki — Interrupt Descriptor Table](https://wiki.osdev.org/Interrupt_Descriptor_Table) — free, authoritative
- [OSDev Wiki — Interrupts](https://wiki.osdev.org/Interrupts) — free, authoritative

## Related terms
- [Hardware Interrupt](interrupt.md)
- [Interrupt Service Routine (ISR)](isr.md)
- [PIC / APIC](pic-apic.md)
- [Global Descriptor Table (GDT)](gdt.md)
- [System Call](syscall.md)
- [Paging / Page Tables](paging.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
