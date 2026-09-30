# Heap Allocation

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

Heap allocation is dynamically allocating memory at runtime — and in a kernel, you must implement the allocator yourself, because there's no operating system below to hand out heap memory.

## The short version
A hosted program calls `malloc` (or Rust's `alloc`) and an OS-backed allocator fulfills it. A kernel is the OS, so when it wants dynamic memory it must build its own allocator from scratch. The hub positions heap allocation as a layer on top of the raw [frame allocator](frame-allocator.md) and [paging](paging.md) foundation.

## Detailed explanation
Heap allocation is the act of dividing a large, contiguous region of memory into variable-sized chunks on demand. Unlike the frame allocator (which hands out fixed-size 4 KiB pages one at a time), a heap allocator services requests of *arbitrary sizes* — `Vec<T>`, `String`, `Box<T>` in Rust, or `malloc` in C — and must track both used and freed chunks so it can reuse them.

The memory chapter makes clear where heaps fit in the bare-metal stack:

> Real memory is divided into **physical pages** (usually 4 KiB each). A *frame allocator* tracks which pages are free.

The heap is built *on top of* those pages, usually using paging. In Rust specifically, `#![no_std]` strips out the global allocator, so to use `alloc`-based types you must write a `#[global_allocator]` that implements `GlobalAlloc` — a Rust-visible version of the same work a C kernel does with a `malloc` replacement. The hub's memory-model table summarizes the bare-metal states: C/C++ write "your own allocator," Rust writes the allocator too but is protected by the borrow checker, while Go and C# rely on a GC-managed heap that needs many stubs on bare metal.

## Why it matters here (OSDev_Learning_Hub)
`Example_OS_Project/rust/src/main.rs` deliberately does not allocate yet — it only writes to the `0xB8000` framebuffer and loops. Heap allocation is the layer this hub's memory chapter (`synthesized_tutorials/concepts/02-memory-management.md`) builds toward: first manage physical pages, then build higher-level allocation on top. It is the bridge between the raw [frame allocator](frame-allocator.md) and the language runtime features like [garbage collection](garbage-collection.md).

## Watch / listen
[- Writing an OS in Rust - Part 10 - Heap Allocation - Uncle Scientist](https://www.youtube.com/watch?v=hJpgu-LYrj8) — adding a heap allocator to a kernel
[- Pulling Back the Curtain on the Heap - Jacob Sorber](https://www.youtube.com/watch?v=GIWeQ2I67rk) — what the heap is and how allocators manage it
[- Stack vs Heap Memory in C++ - The Cherno](https://www.youtube.com/watch?v=wJ1L2nSIV1s) — stack vs heap explained
- [OSDev Wiki — Memory Allocation](https://wiki.osdev.org/Memory_Allocation) — free, authoritative
- [Rust — GlobalAlloc trait (official docs)](https://doc.rust-lang.org/std/alloc/trait.GlobalAlloc.html) — free official docs
- [Blog "Writing an OS in Rust" — Heap Allocation](https://os.phil-opp.com/heap-allocation/) — free

## Related terms
- [Frame Allocator](frame-allocator.md)
- [Memory Management](memory-management.md)
- [Paging](paging.md)
- [Garbage Collection](garbage-collection.md)
- [`no_std`](no_std.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
