# Concept — Memory Management

*Original content written for OSDev_Learning_Hub.*

## In one sentence
A [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") must keep track of **what memory exists, what's used, and what's free**, and hand it out safely — because unlike a normal program, there's no OS underneath to do it.

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

Your very first kernel can ignore [memory management](../../GLOSSARY/memory-management.md "How a kernel tracks used and free RAM and hands it out safely") (it just writes to screen and halts). But the *moment* you want variables, stacks, or `malloc`, you must build a memory manager. The os01 book and the Phil Opp Rust series both spend serious chapters here for exactly this reason.

## The frame allocator — the simplest memory manager

Real memory is divided into **physical pages** (usually 4 KiB each). A *[frame allocator](../../GLOSSARY/frame-allocator.md "The simplest manager that tracks which 4 KiB physical pages are free")* tracks which pages are free:

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

Modern CPUs use [paging](../../GLOSSARY/paging.md "Translates virtual addresses to physical RAM via page tables"): the CPU translates every *virtual address* your kernel's pointers use into a *physical address* of real RAM, using [page tables](../../GLOSSARY/paging.md "Translates virtual addresses to physical RAM via page tables").

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

## Watch and learn

<details class="video-embed">
<summary>▶ Watch: How Computer Memory Works</summary>
<iframe src="https://www.youtube-nocookie.com/embed/XETZoRYdtkw" title="How Computer Memory Works" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>Computerphile explains how logic gates build the memory circuits that make up your machine's RAM.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: The Call Stack and Stack Overflows (example in C)</summary>
<iframe src="https://www.youtube-nocookie.com/embed/jVzSBkbfdiw" title="The Call Stack and Stack Overflows (example in C)" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>Jacob Sorber shows how the stack, locals, and heap are laid out in a C program's memory.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: Stack vs Heap Memory in C++</summary>
<iframe src="https://www.youtube-nocookie.com/embed/wJ1L2nSIV1s" title="Stack vs Heap Memory in C++" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>The Cherno breaks down the two memory regions you manage by hand when writing C++.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: WHY IS THE HEAP SO SLOW?</summary>
<iframe src="https://www.youtube-nocookie.com/embed/ioJkA7Mw2-U" title="WHY IS THE HEAP SO SLOW?" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>Core Dumped explains how an operating system allocates dynamic memory and why it costs a system call.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: What's Virtual Memory? - Computerphile</summary>
<iframe src="https://www.youtube-nocookie.com/embed/5lFnKYCZT5o" title="What's Virtual Memory? - Computerphile" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>Dr Steve Bagley explains virtual memory, page tables, and how the MMU translates addresses — the exact "paging" ideas your kernel will implement.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: Memory Mapping - Computerphile</summary>
<iframe src="https://www.youtube-nocookie.com/embed/di5WodGWTiY" title="Memory Mapping - Computerphile" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>A friendly, robot-and-"bouncer" analogy for how pages give each program its own view of memory — the reason paging exists.</p>
</details>

---

## Further reading

- [OSDev Wiki — Memory Management](https://wiki.osdev.org/Memory_Management) — the whole topic map: frames, paging, heap, and more.
- [OSDev Wiki — Paging](https://wiki.osdev.org/Paging) — how virtual addresses become physical via page tables.
- [OSDev Wiki — Setting Up Paging](https://wiki.osdev.org/Setting_Up_Paging) — the concrete page-table code for when you're ready to write it.
- [OSDev Wiki — Page Frame Allocation](https://wiki.osdev.org/Page_Frame_Allocation) — the bitmap/buddy allocators behind the "one bit per page" idea here.
- [OSDev Wiki — Detecting Memory (x86)](https://wiki.osdev.org/Detecting_Memory_(x86)) — where your kernel learns how much RAM actually exists (the Multiboot memory map).
- [Writing an OS in Rust — Paging Introduction](https://os.phil-opp.com/paging-introduction/) — a clear walkthrough of a real page-table setup with code.

---

## A note on the heap (light add-on)

The `malloc`-style heap your normal programs take for granted is actually built *on top of* paging plus a frame allocator. A kernel's heap is just a region of virtual pages that the kernel's own allocator hands out in small chunks. So the roadmap is: **frame allocator → paging → heap**. Don't try to skip ahead to `malloc` until the first two work — almost every OS-dev gotcha lives in that gap.
