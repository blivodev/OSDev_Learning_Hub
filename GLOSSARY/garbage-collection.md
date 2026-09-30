# Garbage Collection (GC)

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

Garbage collection is automatic memory reclamation — and on bare metal it's a burden, because managed runtimes like Go and C# assume an OS underneath to support their collector.

## The short version
Languages like Go and C# don't hand you raw memory management — they ship a runtime that allocates on a managed heap and automatically reclaims (garbage-collects) objects no longer reachable. That runtime is written for a **hosted** environment. On bare metal there's no OS services for it to lean on, which is exactly why writing a Go or C# kernel is hard.

## Detailed explanation
In a language with a garbage collector, the programmer never calls `malloc`/`free` manually: the runtime tracks live objects and frees the rest. This is convenient but heavyweight — the collector needs threads, a registry of roots, a managed heap of its own, and often OS-provided facilities. The hub's memory-model comparison spells out the bare-metal consequence:

| Language | Memory model | Bare-metal state |
|----------|--------------|------------------|
| C / C++ | Raw pointers, manual `malloc` replacement | Full control — you write the allocator |
| Rust | Ownership + raw pointers via `unsafe` | Also full control; borrow checker protects you |
| Go | GC runtime (goroutines, heap) | Runtime needs many stubs on bare metal |
| C# | GC runtime (managed heap) | Needs a whole framework (Cosmos) to bootstrap |

So while a C or Rust kernel hands out memory through its own [frame allocator](frame-allocator.md) and [heap allocator](heap-allocation.md), a Go kernel's GC runtime "needs many stubs on bare metal," and a C# kernel's GC-managed heap "needs a whole framework (Cosmos) to bootstrap." The memory-management chapter notes that kernels in these languages "tend to lean heavily on their runtime's existing memory model, which is part of why bare-metal Go/C# is harder." This is why the hub's toolchain chapter lists no direct `-ffreestanding`-style switch for C# — there's none, because the managed heap assumes an OS.

## Why it matters here (OSDev_Learning_Hub)
Garbage collection appears throughout the hub as the *contrast* that explains why C, C++, and Rust are the naturals for minimal kernels while Go and C# need scaffolding. It's discussed in `synthesized_tutorials/concepts/02-memory-management.md` (the memory-model comparison table) and in the toolchain chapter (`synthesized_tutorials/00-introduction/02-your-toolchain.md`), where C# is noted as having "no direct equivalent — needs Cosmos/NativeAOT." The C# kernel path in the hub leans on [Cosmos OS](cosmos.md) precisely because of this.

## Watch / listen
[- Garbage Collection (Mark & Sweep) - Computerphile](https://www.youtube.com/watch?v=c32zXYAK7CI) — how a tracing GC reclaims memory
[- Rust and RAII Memory Management - Computerphile](https://www.youtube.com/watch?v=pTMvh6VzDls) — the no-GC alternative kernels use
- [Wikipedia — Garbage collection (computer science)](https://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29) — free
- [Go documentation — Garbage collection](https://go.dev/doc/gc-guide) — free official docs

## Related terms
- [Heap Allocation](heap-allocation.md)
- [Frame Allocator](frame-allocator.md)
- [Memory Management](memory-management.md)
- [Hosted](hosted.md)
- [Cosmos OS](cosmos.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
