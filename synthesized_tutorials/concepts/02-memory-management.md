# Concept — Memory Management

*Original content written for OSDev_Learning_Hub.*

## In one sentence
A kernel must keep track of **what memory exists, what's used, and what's free**, and hand it out safely — because unlike a normal program, there's no OS underneath to do it.

## The mental model

```mermaid
flowchart TD
    subgraph Physical memory
        A[Low memory < 1 MiB] --> A1[BIOS & real-mode territory]
        B[Your kernel at 1 MiB] --> B1[code/data/stack]
        C[Free RAM] --> C1[what you manage]
        D[High memory] --> D1[device & reserved]
    end
```

Your very first kernel can ignore memory management (it just writes to screen and halts). But the *moment* you want variables, stacks, or `malloc`, you must build a memory manager. The os01 book and the Phil Opp Rust series both spend serious chapters here for exactly this reason.

## The frame allocator — the simplest memory manager

Real memory is divided into **physical pages** (usually 4 KiB each). A *frame allocator* tracks which pages are free:

```c
// A super-simplified bitmap allocator (concept only)
uint8_t bitmap[ /* total_memory / 4096 / 8 */ ];

void* allocate_frame(void) {
    for (size_t i = 0; i < bitmap_size; i++) {
        if ((bitmap[i / 8] & (1 << (i % 8))) == 0) {  // page i is free
            bitmap[i / 8] |= (1 << (i % 8));           // mark used
            return (void*)(i * 4096);                  // return its address
        }
    }
    return NULL; // out of memory
}
```

One bit per 4 KiB page. That's the whole idea behind a **buddy allocator** and every frame allocator you'll ever read about.

## Paging — the address translator

Modern CPUs use **paging**: the CPU translates every *virtual address* your kernel's pointers use into a *physical address* of real RAM, using page tables.

```mermaid
flowchart LR
    A[Virtual addr 0xFFFF8000...] --> PT[Page tables]
    PT --> B[Physical addr in RAM]
```

Why it matters:
- **Isolation:** each process thinks it owns the whole address space.
- **Protection:** mark pages read-only / no-execute to stop bugs and attacks.
- **Paging as plumbing:** map your kernel at a "high-half" virtual address while it lives low in physical RAM.

The language doesn't matter here — you'll write the same page-table code in C, C++, or Rust. (Go and C# kernels tend to lean heavily on their runtime's existing memory model, which is part of why bare-metal Go/C# is harder.)

## A quick memory-model comparison across our languages
| Language | Memory model | Bare-metal state |
|----------|--------------|------------------|
| C / C++ | Raw pointers, manual `malloc` replacement | Full control — you write the allocator |
| Rust | Ownership + raw pointers via `unsafe` | Also full control; borrow checker protects you |
| Go | GC runtime (goroutines, heap) | Runtime needs many stubs on bare metal |
| C# | GC runtime (managed heap) | Needs a whole framework (Cosmos) to bootstrap |

> **Next:** [`03-interrupts-and-the-idt.md`](03-interrupts-and-the-idt.md).
