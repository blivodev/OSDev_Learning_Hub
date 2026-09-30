# Frame Allocator

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

A frame allocator is the simplest memory manager: it tracks which fixed-size physical pages (usually 4 KiB each) are free and hands them out one at a time.

## The short version
Real memory comes in **physical pages** of 4 KiB. A frame allocator keeps a record of which of those pages are free — in its simplest form, a **bitmap** with one bit per page — and returns the address of a free page when asked. The hub calls it "the whole idea behind a buddy allocator and every frame allocator you'll ever read about."

## Detailed explanation
The memory-management chapter (`synthesized_tutorials/concepts/02-memory-management.md`) gives the canonical super-simplified bitmap allocator:

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

The math shows the key numbers: the bitmap needs `total_memory / 4096 / 8` bytes (one bit per 4 KiB page, 8 pages per byte), and page `i` lives at physical address `i * 4096`. "One bit per 4 KiB page." That's the entire idea. A frame allocator hands out fixed-size pages, which is all a paging MMU needs — page tables map whole frames, so variable-size allocation can wait. More sophisticated allocators (buddy allocators, free lists) optimize for speed and fragmentation, but they all solve the same core tracking problem.

## Why it matters here (OSDev_Learning_Hub)
The frame allocator is the foundational piece of `synthesized_tutorials/concepts/02-memory-management.md`, the hub's memory-management concept document. It's the first memory manager a kernel builds, sitting below [paging](paging.md) (which consumes these physical frames) and [heap allocation](heap-allocation.md) (which sits on top). The minimal kernels in `Example_OS_Project/` don't allocate yet, but the moment a kernel wants a stack, variables, or a heap, the frame allocator is where physical memory management begins.

## Watch / listen
[- Writing an OS in Rust - Part 9 - Paging Implementation - Uncle Scientist](https://www.youtube.com/watch?v=80h0uQq1jO0) — allocating physical frames for page tables
- [OSDev Wiki — Memory Management](https://wiki.osdev.org/Memory_management) — free, authoritative
- [Blog "Writing an OS in Rust" — Page Tables and Frame Allocator](https://os.phil-opp.com/) — free

## Related terms
- [Memory Management](memory-management.md)
- [Paging](paging.md)
- [Heap Allocation](heap-allocation.md)
- [Physical vs Virtual Memory](physical-virtual-memory.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
