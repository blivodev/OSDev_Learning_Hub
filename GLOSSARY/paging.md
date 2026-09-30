# Paging / Page Tables

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

Paging is the CPU feature that translates every *virtual address* your kernel's pointers use into a *physical address* of real RAM, using page tables.

## The short version
Modern CPUs don't let your code address RAM directly — each pointer is a *virtual address* that the CPU's Memory Management Unit (MMU) looks up in **page tables** to find the real physical address. Paging gives you isolation (each process thinks it owns all of memory), protection (mark pages read-only or non-executable), and "plumbing" (map your kernel at a high virtual address while it lives low in physical RAM).

## Detailed explanation
The memory chapter draws it simply:

```mermaid
flowchart LR
    A[Virtual addr 0xFFFF8000...] --> PT[Page tables]
    PT --> B[Physical addr in RAM]
```

On x86_64, address translation is done by a **multi-level page table** — the hardware walks page-map levels (PML4 → PDPT → PD → PT → 4 KiB page) to resolve a virtual address to a physical frame. Each entry holds a physical page-frame address plus flags such as read/write, present, and no-execute. This matters for three reasons the hub calls out:

- **Isolation:** each process thinks it owns the whole address space (page tables are per-address-space).
- **Protection:** mark pages read-only / no-execute to stop bugs and attacks.
- **Paging as plumbing:** map your kernel at a "high-half" virtual address (e.g. `0xFFFF8000...`) while it lives low in physical RAM (at 1 MiB).

`unsafe` in Rust is often used precisely when you manipulate page tables: reading and writing raw table memory is an operation the borrow checker can't verify. The hub notes the language doesn't change the job — "you'll write the same page-table code in C, C++, or Rust" — and that go/C# kernels lean on their runtime's memory model instead, which is part of why bare-metal Go/C# is harder.

## Why it matters here (OSDev_Learning_Hub)
Paging is covered in depth in `synthesized_tutorials/concepts/02-memory-management.md`, which is the grounding source for this page. The minimal `Hello World!` kernels in `Example_OS_Project/` don't set up paging yet (they write straight to the identity-mapped `0xB8000` framebuffer), but paging is the *next* memory tool every serious kernel reaches for after the frame allocator. See also [physical vs virtual memory](physical-virtual-memory.md).

## Watch / listen
[- Writing an OS in Rust - Part 9 - Paging Implementation - Uncle Scientist](https://www.youtube.com/watch?v=80h0uQq1jO0) — implementing x86 page tables in a kernel
[- The Most Successful Idea in Computer Science - Core Dumped](https://www.youtube.com/watch?v=LDhoD4IVElk) — why paging and virtual memory exist
- [OSDev Wiki — Page Tables](https://wiki.osdev.org/Page_Tables) — free, authoritative
- [OSDev Wiki — Paging](https://wiki.osdev.org/Paging) — free, authoritative
- [Blog "Writing an OS in Rust" — Paging Introduction](https://os.phil-opp.com/paging-introduction/) — free

## Related terms
- [Physical vs Virtual Memory](physical-virtual-memory.md)
- [Frame Allocator](frame-allocator.md)
- [Memory Management](memory-management.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
