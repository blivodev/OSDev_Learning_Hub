# Physical vs Virtual Memory

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

Physical memory is the actual RAM installed in the machine, while virtual memory is the address space your code sees after the CPU's paging feature translates it.

## The short version
Every pointer your kernel uses is a *virtual address*, not the real RAM location. The CPU's paging unit translates each virtual address into a *physical address* through page tables. This is why a kernel can, say, map itself at a high "high-half" virtual address like `0xFFFF8000...` while it physically lives low in RAM at 1 MiB.

## Detailed explanation
The memory chapter separates the two clearly:

> Real memory is divided into **physical pages** (usually 4 KiB each).

**Physical** memory is the raw RAM (plus memory-mapped hardware like the VGA framebuffer at `0xB8000` and the kernel loaded at 1 MiB). **Virtual** memory is what your code actually dereferences — before any pointer reaches the memory bus, the MMU rewrites it through **page tables** to a physical frame. The hub's diagram:

```mermaid
flowchart LR
    A[Virtual addr 0xFFFF8000...] --> PT[Page tables]
    PT --> B[Physical addr in RAM]
```

This separation is what makes the three big benefits of [paging](paging.md) possible: isolation (each process sees its own complete virtual address space), protection (flags on pages), and plumbing (an object can live at one physical location but be visible at a chosen virtual address). One classic consequence the memory chapter highlights: "map your kernel at a 'high-half' virtual address while it lives low in physical RAM" — the kernel is physically at 1 MiB but addressed through a high virtual range.

The frame allocator deals in *physical* pages; page tables and the MMU are what connect the physical world to the virtual world your code lives in. A `malloc`-style heap then operates on *virtual* addresses that map to those physical pages underneath.

## Why it matters here (OSDev_Learning_Hub)
The physical/virtual split underpins `synthesized_tutorials/concepts/02-memory-management.md`, the hub's grounding source for this page, and is essential to understanding [paging](paging.md). The minimal kernels in `Example_OS_Project/` write to `0xB8000` — a *physical* (identity-mapped) address — without any page tables yet, but a real kernel introduces virtual mapping on top of the physical frame allocator.

## Watch / listen
[- The Most Successful Idea in Computer Science - Core Dumped](https://www.youtube.com/watch?v=LDhoD4IVElk) — virtual address spaces vs physical RAM
- [Wikipedia — Virtual memory](https://en.wikipedia.org/wiki/Virtual_memory) — free
- [OSDev Wiki — Paging](https://wiki.osdev.org/Paging) — free, authoritative
- [Blog "Writing an OS in Rust" — Paging Introduction](https://os.phil-opp.com/paging-introduction/) — free

## Related terms
- [Paging](paging.md)
- [Frame Allocator](frame-allocator.md)
- [Memory Management](memory-management.md)
- [Heap Allocation](heap-allocation.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
