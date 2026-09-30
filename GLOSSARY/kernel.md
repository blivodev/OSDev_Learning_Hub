# Kernel

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

The kernel is the core program that owns the machine and manages hardware and memory for every other piece of software running on it.

## The short version
In a normal program something else (the OS) sets up your memory, stack, and libraries and cleans up after you. A kernel is that "something else": it runs at power-on, talks to hardware **directly**, and never exits. In OSDev_Learning_Hub the kernel is the freestanding program that starts at 1 MiB and writes "Hello World!" straight to the VGA framebuffer at `0xB8000`.

## Detailed explanation
In this hub, the kernel is the only program that runs with *no assumption of anything underneath it*. Unlike an app that calls `printf` and expects an OS to service it, the kernel must provide every service itself: a memory manager, an interrupt table, a display driver, and a scheduler. The [toolchain chapter](https://wiki.osdev.org/Expanded_Main_Page) makes this concrete: each language compiles the kernel with a *freestanding* flag (`gcc -ffreestanding`, `g++ -ffreestanding -fno-exceptions -fno-rtti`, or Rust's `#![no_std]`), and the linker places its image at a chosen address via a linker script:

```ld
ENTRY(_start)          /* entry point the bootloader jumps to */
SECTIONS {
    . = 1M;            /* load the kernel at 1 MiB */
    .text : { *(.multiboot) *(.text) }
    .rodata : { *(.rodata) }
    .data  : { *(.data) }
    .bss   : { *(COMMON) *(.bss) }
}
```

The `.multiboot` section must come first so the Magic Number (`0x1BADB002`) is at the very front of the image. The CPU's first steps are in **assembly** (boot stub), which then jumps into the high-level `_start`/`main`. A kernel never returns from that entry function — the Rust example ends in `loop { hlt }`, because there is no OS below it to return to. The minimal kernel here writes directly to the VGA text buffer: each `0xB8000` cell is `[color<<8 | char]`, e.g. `vga[0] = 0x0F48;` for an `'H'` in white-on-black.

## Why it matters here (OSDev_Learning_Hub)
The whole hub builds one thing: a kernel. The C, C++, Rust, Go, and C# variants in `Example_OS_Project/` are all the same program written against each language's freestanding rules. The walkthrough is grounded in files such as `Example_OS_Project/rust/src/main.rs` (the Rust `_start` kernel) and `synthesized_tutorials/00-introduction/02-your-toolchain.md` (why a kernel needs an assembler, compiler, linker, and QEMU). Concept grounding for what the kernel must own lives in `synthesized_tutorials/concepts/02-memory-management.md`.

## Watch / listen
[- The Question Nobody Ever Explains: Where Does the Kernel End? - Core Dumped](https://www.youtube.com/watch?v=ZmPIxfCggFw) — what a kernel is and where it sits
- [OSDev Wiki — Kernel](https://wiki.osdev.org/Kernel) — free, authoritative
- [OSDev Wiki — Bare Bones (writing a minimal kernel)](https://wiki.osdev.org/Bare_Bones) — free, authoritative
- [Rust standard library documentation](https://doc.rust-lang.org/) — free official docs

## Related terms
- [Freestanding](freestanding.md)
- [Hosted](hosted.md)
- [Entry Point](entry-point.md)
- [Memory Management](memory-management.md)
- [VGA Framebuffer](vga-framebuffer.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
