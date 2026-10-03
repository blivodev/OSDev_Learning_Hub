#!/usr/bin/env python3
"""Generate new OSDev glossary term files from a compact list.
Each term: slug | Title | category | one-line short version | one-paragraph detail.
Writes docs/GLOSSARY/<slug>.md in the standard glossary format.
"""
import os, sys

OUT = r"D:/Projects/OSDev-Tutorial-Site/docs/GLOSSARY"

TERMS = [
 # slug | title | category | short | detail
 ("scheduler", "Scheduler", "Kernel & runtime",
  "The part of the kernel that decides which process or thread runs next on the CPU.",
  "The scheduler picks the next runnable task and performs a context switch. Common policies are round-robin (RR), priority, and multi-level feedback queue (MLFQ). The OSDev kernel in this hub starts with a simple round-robin timer-driven scheduler, then adds priorities. It is triggered by the PIT or APIC timer interrupt."),
 ("context-switch", "Context switch", "Kernel & runtime",
  "Saving one task's CPU state and restoring another's so the CPU appears to run many tasks at once.",
  "On a context switch the kernel saves the outgoing task's registers and stack pointer (into its TCB/PCB), picks the next task, and restores its registers. This is what makes multitasking visible to user programs. The switch itself is pure assembly in most kernels, then returns into the restored task."),
 ("tcb", "Task Control Block (TCB) / Process Control Block (PCB)", "Kernel & runtime",
  "The kernel's per-task record holding saved registers, state, and metadata.",
  "Each process or thread has a TCB (or PCB for processes) that stores the saved context, state (ready/running/blocked), priority, and bookkeeping like time used. The scheduler walks the list of TCBs to pick the next runner. Also called the process list."),
 ("spinlock", "Spinlock", "Concurrency",
  "A lock that busy-waits (spins) until it is acquired; used for very short critical sections.",
  "A spinlock loops on an atomic test-and-set until the lock becomes free. Because it burns CPU while waiting, it is only used for short sections or on multi-core where the lock holder may run on another core. Kernels pair spinlocks with disabling interrupts to avoid deadlock on a single core."),
 ("mutex-kernel", "Mutex (kernel)", "Concurrency",
  "A sleeping lock that blocks the task instead of spinning when the lock is held.",
  "A mutex (mutual exclusion) lets a task sleep if the lock is contended, so it does not waste CPU. It is used for longer critical sections. Kernels implement mutexes on top of the scheduler (the waiter is moved to a blocked queue and woken when released)."),
 ("atomic", "Atomic operations", "Concurrency",
  "Read-modify-write CPU operations (like xchg, cmpxchg, lock inc) that cannot be interrupted.",
  "Atomics guarantee that an operation on shared memory completes without another CPU observing a partial result. They are the building blocks for spinlocks, refcounts, and lock-free data structures. On x86, the LOCK prefix makes an instruction atomic; on ARM/RISC-V it is done with LL/SC."),
 ("memory-barrier", "Memory barrier", "Concurrency",
  "An instruction that orders memory accesses so the CPU/compiler don't reorder them across it.",
  "CPUs and compilers reorder memory operations for performance, which can break shared-memory synchronization. A memory barrier (fence/mfence/dmb) forces ordering. Kernels use them around lock release/acquire so that writes before the lock are visible to the next holder."),
 ("smp", "SMP (Symmetric Multi-Processing)", "Multi-core",
  "Running the kernel on multiple CPUs that share one memory system.",
  "SMP means several cores run at once, each executing the kernel concurrently. This forces per-CPU data, spinlocks, and careful cache-coherency handling. The kernel must initialize each core (AP boot via SIPI) and manage per-CPU variables so cores don't clobber each other."),
 ("cache-coherence", "Cache coherence", "Multi-core",
  "The protocol that keeps multiple CPUs' caches consistent for shared memory.",
  "When cores share memory, their caches must agree on the current value. Hardware cache-coherence protocols (like MESI) track cache-line states and invalidate stale copies. Kernels need memory barriers so writes aren't stuck in one core's cache when another reads them."),
 ("acpi", "ACPI (Advanced Configuration and Power Interface)", "Hardware",
  "A firmware/OS standard for describing hardware and managing power.",
  "ACPI replaces the old APM for power management. The OS reads ACPI tables (RSDP/R SDT, FADT, MADT, DSDT) provided by firmware to learn about devices, power states (C-states, S-states), and the multi-core layout (MADT/APIC tables). It is the modern way a kernel discovers the machine."),
 ("pci", "PCI / PCIe (Peripheral Component Interconnect)", "Hardware",
  "The standard bus for attaching devices (GPUs, NICs, storage) to the CPU.",
  "PCI gives each device a config space (256 bytes, or 4096 for PCIe) that the OS scans by bus/device/function. The config space holds vendor/device IDs, BARs (Base Address Registers) that map device memory, and interrupt routing. The kernel enumerates PCI at boot and loads matching drivers."),
 ("usb", "USB (Universal Serial Bus)", "Hardware",
  "A serial bus for peripherals with a host controller and a device tree.",
  "USB is a tree of devices under one or more host controllers (EHCI/XHCI on x86). The OS talks to the controller, which manages the root hub and enumerates devices by addresses/endpoints. Drivers send control/bulk/interrupt/isochronous transfers through the host controller."),
 ("pit", "PIT (Programmable Interval Timer)", "Hardware & timing",
  "The classic 8254 timer chip that fires periodic interrupts for timekeeping.",
  "The PIT counts down from a programmed divisor and raises IRQ0 on expiry, giving a periodic tick (commonly 100 or 1000 Hz). It drives the scheduler's time slices and system time. The APIC timer is the modern replacement on multi-core systems."),
 ("rtc", "RTC (Real-Time Clock)", "Hardware & timing",
  "A battery-backed clock that keeps wall-clock time and can raise an alarm interrupt.",
  "The RTC keeps time even when the PC is off. The kernel reads it via CMOS (port 0x70/0x71) or an ACPI RTC to get the current date/time, and can use it as a low-frequency interrupt source. It complements the PIT/APIC tick."),
 ("syscall-abi", "Syscall ABI", "User/kernel boundary",
  "The register convention by which user programs request kernel services.",
  "A system call passes arguments in registers (on x86-64: rax=number, rdi/rsi/rdx=args) and triggers a switch to kernel mode (via syscall/sysenter or int 0x80). The kernel looks up the handler by number, validates arguments, and returns. The ABI defines error handling via errno/return values."),
 ("privilege-level", "Privilege levels / CPU rings", "CPU",
  "x86 protection rings (0–3) that restrict what code can do; the kernel runs in ring 0.",
  "The CPU enforces privilege: ring 0 (kernel) can run privileged instructions (like sti/cli, writing CR3), while rings 1–3 (user) are restricted. User code must use syscalls to cross into the kernel. Long mode uses the similar notion of CPL (current privilege level)."),
 ("interrupt-controller", "Interrupt controller (PIC/APIC)", "CPU & interrupts",
  "Hardware that collects device interrupts and delivers them to the CPU as IRQs.",
  "The 8259 PIC maps hardware interrupts to IDT vectors; the modern APIC (I/O APIC + local APIC) delivers them per-core. The kernel programs the controller to assign vectors, mask/unmask IRQs, and route them to the right CPU. It handles the priority and acknowledgment of interrupts."),
 ("mmio", "MMIO (Memory-Mapped I/O)", "I/O",
  "Accessing hardware registers through normal memory addresses rather than port I/O.",
  "Many devices expose their control registers in a memory window (described by BARs or ACPI). The kernel writes/reads those addresses to talk to the device, using volatile/barrier so the CPU doesn't cache or reorder them. x86 also has the separate port I/O space (in/out)."),
 ("dma", "DMA (Direct Memory Access)", "I/O",
  "Hardware that transfers data between devices and memory without the CPU copying it.",
  "DMA lets a device read/write system memory directly, freeing the CPU for other work. The kernel sets up a DMA buffer (often with an IOMMU translation), gives the device its address, and receives an interrupt when the transfer completes. Cache-coherent DMA requires careful memory barriers and sometimes cache flushing."),
 ("acpi-tables", "ACPI tables / RSDP", "Firmware",
  "Structured memory tables firmware provides that describe hardware to the OS.",
  "The kernel finds the RSDP (Root System Description Pointer) via the BIOS memory or EFI, then follows RSDT/XSDT to locate FADT (power/events), MADT (APIC/SMP layout), and DSDT/SSDT (device objects in AML). Reading these lets the kernel enumerate CPUs, interrupt routing, and power capabilities."),
 ("ps2-keyboard", "PS/2 keyboard", "Hardware & input",
  "The classic keyboard controller (8042) on port 0x60 that delivers scancodes.",
  "A PS/2 keyboard sends scancodes through the 8042 controller, which raises IRQ1. The kernel reads port 0x60 to get the scancode and translates it to keycodes. Modern UEFI machines still emulate PS/2 for legacy compatibility; USB keyboards go through the USB HID stack."),
 ("vga-attribute", "VGA text attributes", "Display",
  "The foreground/background color byte that accompanies each character in text mode.",
  "In VGA text mode each 16-bit cell holds a character and an attribute byte (low nibble = foreground, high nibble = background). Writing to the buffer at 0xB8000 with attribute bytes is how a bare-bones kernel prints colored text before a framebuffer is set up."),
 ("buddy-allocator", "Buddy allocator", "Memory",
  "A memory allocator that splits/free chunks in power-of-two sizes.",
  "The buddy system manages free blocks as powers of two. When a request comes, it splits a larger block and marks buddies; when freed, it coalesces adjacent buddies. It's simple and fast, at the cost of internal fragmentation. Kernels often use it for page frames, with a slab cache for small objects."),
 ("slab-allocator", "Slab allocator", "Memory",
  "A cache-based allocator for small, same-size kernel objects.",
  "The slab allocator keeps a cache of fixed-size objects (like task structs, inodes) to avoid repeated initialization and reduce fragmentation. Linux's slab/slub manages per-object-type caches backed by page frames. It sits on top of the page (buddy) allocator."),
 ("tlb", "TLB (Translation Lookaside Buffer)", "Memory",
  "The CPU cache of virtual-to-physical page mappings.",
  "The TLB caches recent page-table translations so the MMU doesn't walk tables every access. When the kernel changes page tables it must flush (invalidate) the relevant TLB entries — on x86 by writing CR3 or using invlpg. TLB flushes are why page-table changes are relatively expensive."),
 ("page-fault", "Page fault", "Memory & exceptions",
  "A CPU exception when accessing a page that isn't present, or with bad permissions.",
  "When the MMU can't translate an address, the CPU raises a page fault (exception 14). The kernel reads CR2 for the faulting address and either fixes it (demand paging, copy-on-write, lazy allocation) or kills the process for an invalid access. Handling page faults efficiently is core to virtual memory."),
 ("heap-kernel", "Kernel heap", "Memory",
  "The dynamic memory region inside the kernel used by kmalloc/new.",
  "The kernel heap serves small dynamic allocations during runtime. In the Rust kernel this is the allocator wired to the global allocator (heap_start), with a bump or linked-list allocator. It is distinct from the physical page allocator, which hands out whole frames."),
 ("interrupt-vector", "Interrupt vector", "CPU & interrupts",
  "The IDT entry index (0–255) that maps an interrupt/exception to a handler.",
  "Each interrupt or exception has a vector that indexes into the IDT (Interrupt Descriptor Table). Vectors 0–31 are CPU exceptions (page fault = 14, GPF = 13), 32–255 are software/hardware IRQs. The kernel installs handlers for each vector it wants to service."),
 ("initrd", "initrd / initramfs", "Storage & boot",
  "A small initial RAM disk the bootloader loads so the kernel can find real storage.",
  "The initrd is a filesystem image loaded into RAM at boot, letting the kernel mount a real root filesystem (the drivers to read it live in the initrd). The kernel unpacks it, runs /init, and the system boots. Essential when storage drivers aren't built into the kernel."),
 ("elf-loader", "ELF loader", "User processes",
  "Kernel code that maps an ELF executable into memory and starts it.",
  "When a program runs, the kernel reads its ELF headers, maps each PT_LOAD segment at the right virtual address with the right permissions, sets up the stack/argv/env, and jumps to the entry point (e_entry). It also handles dynamic linking by loading the interpreter (ld.so) first."),
 ("fork-exec", "fork & exec", "User processes",
  "The POSIX way to create processes: fork duplicates, exec replaces the image.",
  "fork() copies the current process (page tables, memory) to create a child; exec() replaces a process's memory with a new program. Together they launch programs. Copy-on-write makes fork cheap by sharing pages until one side writes. The kernel's 'fork to exec' is a key milestone in this hub."),
 ("io-apic", "I/O APIC", "CPU & interrupts",
  "The modern interrupt controller that routes device IRQs to specific CPUs.",
  "The I/O APIC sits on the bus and delivers device interrupts to chosen local APICs (and thus CPUs). It replaces the two 8259 PICs, giving many more vectors and per-CPU delivery. The kernel programs it via the MADT table to map IRQs to vectors. Critical for SMP."),
]

TEMPLATE = """<!-- GLOSSARY PAGE — {slug}.md -->

# {title}

> **[Back to glossary index](README.md)** · Category: {category}

**{title}** — {short}

## The short version
{detail}

## Related terms
- [Scheduler](scheduler.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials and standard OS-dev references.*
"""

made = 0
for slug, title, category, short, detail in TERMS:
    path = os.path.join(OUT, slug + ".md")
    if os.path.exists(path):
        print(f"SKIP exists: {slug}")
        continue
    content = TEMPLATE.format(slug=slug, title=title, category=category, short=short, detail=detail)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    made += 1
    print(f"created: {slug}")
print(f"\ncreated {made} new glossary files")
