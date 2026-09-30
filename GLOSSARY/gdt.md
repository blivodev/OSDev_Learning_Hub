<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# Global Descriptor Table (GDT)

> **[Back to glossary index](README.md)** · Category: CPU & interrupts

The Global Descriptor Table (GDT) is a table of memory-segment descriptors that the CPU consults in protected and long mode to define how memory is laid out and what privileges your code runs with.

## The short version
In protected mode the CPU does not reference flat physical addresses directly — it goes through segment registers whose values index the GDT. Each entry describes a segment (base, limit, and access/privilege flags). A minimal kernel sets up a GDT with a few entries (null, code, data) so it can jump from the bootloader's state into friendly flat segments before going further.

## Detailed explanation
Every segment register (CS for code, DS/ES/SS for data, etc.) holds a *selector* whose upper bits index the GDT, not the segment itself. The GDT is an array of 8-byte descriptors, and the CPU is pointed at it with the `lgdt` instruction (the counterpart to `lidt` for the [IDT](idt.md)). The leftmost entry must be a zeroed null descriptor; a typical flat layout then adds a code segment and a data segment covering the whole address space, with the descriptor's privilege level (`DPL`) setting ring 0 vs ring 3.

Because protected-mode kernels and the Multiboot boot flow expect a GDT to exist, most bootstraps either rely on the bootloader's GDT or install their own early. The GDT is closely tied to privilege: switching to (or from) ring 3 — which user programs and [syscalls](syscall.md) require — means loading a user code/data descriptor from the GDT. [Paging](paging.md) then does the heavy lifting of per-page protection; the GDT governs segment-level access.

A GDT entry layout (simplified):

```text
bits 0–15  : segment limit, low
bits 16–31 : base, low 16 bits
bits 32–39 : base, next 8 bits
bits 40–47 : access byte (present, DPL, code/data, readable/writable...)
bits 48–55 : flags + limit, high
bits 56–63 : base, high
```

## Why it matters here (OSDev_Learning_Hub)
The GDT is the [segment](memory-management.md) counterpart to the [IDT](idt.md): the [IDT](idt.md) descriptors point at handler offsets *within* a segment named by the GDT. While `Example_OS_Project` currently leans on the flat environment left by its bootloader, the GDT becomes explicit once you move toward user-mode code, [syscalls](syscall.md), or long mode, which has its own 64-bit GDT with null, code, and data entries.

## Watch / listen
[- OSDev Lecture Series 4: Global Descriptor Table - AptRock327](https://www.youtube.com/watch?v=0nT_2aIOTq8) — GDT and segmentation explained
[- Building an OS - 8 - Interrupts, IDT, GDT - nanobyte](https://www.youtube.com/watch?v=5LbXClJhxcs) — GDT setup in a real OS
- [OSDev Wiki — Global Descriptor Table](https://wiki.osdev.org/Global_Descriptor_Table) — free, authoritative
- [Wikipedia — Global Descriptor Table](https://en.wikipedia.org/wiki/Global_Descriptor_Table) — free, authoritative

## Related terms
- [Interrupt Descriptor Table (IDT)](idt.md)
- [Hardware Interrupt](interrupt.md)
- [Memory Management](memory-management.md)
- [Paging / Page Tables](paging.md)
- [System Call](syscall.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
