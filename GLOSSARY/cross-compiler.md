<!-- Glossary page — Cross-Compiler. Grounded in OSDev_Learning_Hub docs. -->

# Cross-Compiler

> **[Back to glossary index](README.md)** · Category: Toolchain & build

A cross-compiler is a compiler that runs on your machine but produces machine code for a *different* CPU (and often a different operating system) than the one it runs on.

## The short version
In this hub you write kernels on a normal PC (x86_64, Windows/Linux) but target `i686` (32-bit x86) bare metal — code that runs with *no OS underneath*. Your system compiler pretty much works for simple C/C++ (via `-m32`), but a proper kernel deserves a dedicated `i686-elf` cross-compiler so no host library or startup assumptions leak in. Go is the hard case: it *requires* a Go-enabled cross-compiler (`i686-elf-gccgo`) because the standard Go toolchain can't target bare metal.

## Detailed explanation
The four pillars of kernel development — assembler, compiler, linker, emulator — all target a machine that doesn't run Linux or Windows. A normal (`hosted`) program assumes an OS and standard library; a kernel is `freestanding`, assuming *nothing*. A cross-compiler for the target `i686-elf` (or `x86_64-elf`) is built with **no headers and no libc** (`--without-headers`), so it can never silently pull in host runtime code.

For C and C++ in this hub, the build works on a normal machine by passing `-m32` and `-ffreestanding -nostdlib` to the system `gcc`/`g++` and booting the 32-bit Multiboot ELF directly with `qemu-system-i386 -kernel`. That is a pragmatic shortcut — as the C Makefile notes, *"for real bare-metal or GRUB-on-disk you should use i686-elf-gcc"*. The OSDev community recommendation is to build an `i686-elf` cross-compiler once and never depend on host quirks.

The Go kernel (`go/README.md`) makes the cross-compiler unavoidable. Standard Go links a full runtime — a garbage collector, goroutine scheduler, and the `runtime` package — that needs an operating system. So the hub builds `i686-elf-gccgo` from GCC source with `--enable-languages=c,c++,go --without-headers` and invokes it with `-nostdlib -nostartfiles -nodefaultlibs`.

```mermaid
flowchart LR
    H[Host machine x86_64] --> CC[Cross-compiler i686-elf-gcc]
    CC --> OBJ[freestanding .o objects]
    OBJ --> LD[Linker with linker.ld at 1 MiB]
    LD --> K[kernel.bin / ELF]
    K --> Q[QEMU emulator]
```

## Why it matters here (OSDev_Learning_Hub)
- The C and C++ kernels use the *system* compiler with freestanding flags (`-ffreestanding -m32 -nostdlib`) — see `Example_OS_Project/c/Makefile` and `Example_OS_Project/cpp/Makefile` — each of which carries a comment explaining when the true `i686-elf` cross-compiler is required.
- The Go kernel genuinely needs one: `i686-elf-gccgo -static -Werror -nostdlib -nostartfiles -nodefaultlibs -c kernel.go -o kernel.go.o` — see `Example_OS_Project/go/README.md` and `go/boot.s`.
- The freestanding-vs-hosted idea that justifies the cross-compiler is the centerpiece of `synthesized_tutorials/00-introduction/02-your-toolchain.md`.

## Watch / listen
- [OSDev Wiki — GCC Cross-Compiler](https://wiki.osdev.org/GCC_Cross-Compiler) — the authoritative, free step-by-step build guide
- [OSDev Wiki — Why do I need a Cross Compiler?](https://wiki.osdev.org/Why_do_I_need_a_Cross_Compiler%3F) — free and thorough

## Related terms
- [Linker](linker.md)
- [Assembler](assembler.md)
- [ELF](elf.md)
- [gccgo](gccgo.md)
- [Freestanding Environment](freestanding.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
