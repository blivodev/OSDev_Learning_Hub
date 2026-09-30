# Hosted Environment

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

A hosted environment is a normal program that assumes an operating system and a standard library (like libc) exist underneath it.

## The short version
Most code you've ever written is **hosted**: it includes `<stdio.h>`, calls `printf`, and expects the OS to load it, give it memory and a stack, and clean up when `main` returns. A kernel is the *opposite* — it is **freestanding** and assumes none of that exists. The toolchain chapter contrasts the two to explain why kernels need special compiler flags.

## Detailed explanation
In a hosted program you take the operating system for granted. `printf` inside libc has to talk to the kernel eventually, the loader sets up your stack before `main`, and when `main` returns the OS reclaims everything. Consider the example from `synthesized_tutorials/00-introduction/02-your-toolchain.md`:

```c
#include <stdio.h>
int main(void) { printf("hi\n"); return 0; }
```

This compiles with a **hosted** mode that assumes a running libc and a functioning OS underneath. It cannot run on bare metal. A kernel cannot call `printf` (there is no OS to do the syscall for it) and cannot `return` from `main` (there is no caller to receive the value). The hosted/freestanding contrast maps directly onto the compiler flags the hub teaches:

| Language | Hosted default | Freestanding switch |
|----------|----------------|---------------------|
| C | normal `gcc` | `gcc -ffreestanding` |
| C++ | normal `g++` | `g++ -ffreestanding -fno-exceptions -fno-rtti` |
| Rust | normal `cargo` (links `std`) | `#![no_std]` attribute |
| Go | normal `go build` (GC runtime) | `gccgo -nostdlib` (+ stubs) |
| C# | normal .NET (managed heap) | no direct equivalent — needs Cosmos/NativeAOT |

## Why it matters here (OSDev_Learning_Hub)
Understanding "hosted" tells you exactly *what you're giving up* when you go freestanding. The memory-management chapter (`synthesized_tutorials/concepts/02-memory-management.md`) makes the point directly: "unlike a normal program, there's no OS underneath to do it." The chapter comparing the languages' memory models notes that hosted runtimes — Go's GC and C#'s managed heap — are exactly what make bare-metal Go and C# harder, because those runtimes assume the services of an operating system.

## Watch / listen
- [Wikipedia — Freestanding and hosted environments](https://en.wikipedia.org/wiki/Freestanding_and_hosted_environments) — free
- [OSDev Wiki — Main Page](https://wiki.osdev.org/Main_Page) — free, authoritative

## Related terms
- [Freestanding](freestanding.md)
- [Kernel](kernel.md)
- [System Call](syscall.md)
- [Garbage Collection](garbage-collection.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
