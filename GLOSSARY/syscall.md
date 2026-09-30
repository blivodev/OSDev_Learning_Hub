<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# System Call

> **[Back to glossary index](README.md)** · Category: Concepts

A system call (syscall) is the controlled way a user-space program asks the kernel to perform a privileged service for it, rather than touching hardware or kernel memory directly.

## The short version
User programs run with restricted privileges (ring 3) and cannot access hardware or kernel structures directly. To do anything useful — read a file, print to a device, allocate memory — they issue a syscall. The CPU switches from user mode to kernel mode, runs the requested service, and returns. In the [IDT](idt.md) model, syscalls live in the 48–255 software range, distinct from CPU exceptions and hardware IRQs.

## Detailed explanation
There are two common mechanisms for making a syscall. The older x86 approach uses the `int` instruction to fire a software interrupt whose vector points at a syscall handler in the [IDT](idt.md) — this is why the tutorial's table reserves **48–255 for "Software / your custom"** use such as syscalls. The modern approach uses dedicated fast instructions (`syscall`/`sysret` on x86-64, `sysenter`/`sysexit` on 32-bit) that skip the interrupt-dispatch overhead.

In both cases the handler runs in ring 0 with kernel privileges, validates the request, performs the operation, and returns to ring 3. The whole flow depends on the [GDT](gdt.md) providing both kernel (ring 0) and user (ring 3) segment descriptors, and on the [ISR](isr.md)/handling glue working correctly. Before a syscall layer can exist, a kernel typically needs [IDT](idt.md), [GDT](gdt.md), and privilege-level transitions working — which is why the beginner "Hello World" examples precede it.

For a minimal teaching kernel a common first syscall family is tiny: `write` (put a string on the [VGA text screen](vga-text-mode.md)) and `exit` (stop the process). Even that requires a user/kernel mode split that the current sample project has not yet built — it still runs everything in ring 0.

## Why it matters here (OSDev_Learning_Hub)
`03-interrupts-and-the-idt.md` explicitly carves out IDT slots 48–255 for "Software / your custom" purposes and names syscalls as the canonical example. It is a forward-looking term: `Example_OS_Project` is still a ring-0 "Hello World" kernel, so syscalls are what you reach for once you add user mode, which in turn relies on the [GDT](gdt.md), [IDT](idt.md), and [Paging](paging.md) foundations.

## Watch / listen
[- How a Single Bit Inside Your Processor Shields Your OS's Integrity - Core Dumped](https://www.youtube.com/watch?v=H4SDPLiUnv4) — the mode switch that syscalls use
- [OSDev Wiki — System Calls](https://wiki.osdev.org/System_Calls) — free, authoritative
- [Wikipedia — System call](https://en.wikipedia.org/wiki/System_call) — free, authoritative

## Related terms
- [Hardware Interrupt](interrupt.md)
- [Interrupt Descriptor Table (IDT)](idt.md)
- [Interrupt Service Routine (ISR)](isr.md)
- [Global Descriptor Table (GDT)](gdt.md)
- [Paging / Page Tables](paging.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
