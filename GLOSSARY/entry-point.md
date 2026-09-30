<!-- GLOSSARY PAGE — entry-point.md -->

# Entry Point (`_start`)

> **[Back to glossary index](README.md)** · Category: Boot & firmware

The **entry point** is the symbol — usually `_start` — that the bootloader jumps to when your kernel starts, the first instruction of your kernel that ever runs.

## The short version
Once a bootloader has loaded your kernel into memory and set up the CPU, it needs a fixed, well-known place to jump into — a symbol it can find. In this hub that symbol is `_start`, declared as a global function in `boot.s`. The linker script tells the loader (via `ENTRY(_start)`) that this is the kernel's first instruction, and the bootloader jumps there to hand the machine to your kernel.

## Detailed explanation
The CPU boots with essentially nothing set up for you. Notably it has **no defined stack pointer**, so before a kernel can call any function — even a C function like `kernel_main` — the bootstrap code must establish a stack. In `Example_OS_Project/c/boot.s`, `_start` does exactly this in order:

1. It emits the Multiboot header (magic `0x1BADB002`) so a bootloader recognizes the image as a valid kernel.
2. It reserves a **16 KiB bootstrap stack** in a `.bootstrap_stack` section (`stack_bottom:` … `.skip 16384`, with `stack_top:` marking the end).
3. It sets the stack pointer and frame pointer to that stack's top.
4. It calls the high-level kernel entry point (`kernel_main`).
5. If the kernel somehow returns, it clears interrupts (`cli`), halts (`hlt`), and loops forever.

The assembly looks like this:

```nasm
.section .bootstrap_stack, "aw", @nobits
stack_bottom:
.skip 16384                      /* 16 KiB */
stack_top:

.section .text
.global _start
.type _start, @function
_start:
    movl $stack_top, %esp        /* point the stack at the top of our 16 KiB */
    movl $stack_top, %ebp        /* set the frame pointer too (for debugging) */

    call kernel_main              /* jump into the C/C++/Go kernel */

    cli                          /* clear the interrupt flag (no more irqs) */
    hlt                          /* halt the CPU */

.Lhang:
    jmp .Lhang                   /* safety net: loop forever */
```

The linker script ties the entry point together. `Example_OS_Project/c/linker.ld` begins with `ENTRY(_start)` — the entry point the bootloader jumps to — and loads the kernel at 1 MiB with `. = 1M;`, placing the `.multiboot` section first so the magic header is at the very start of the image. From the bootloader's point of view, "the kernel" is simply a jump to `_start` at the loaded address.

From that first instruction on, there is **no operating system underneath you anymore**. The `printf` you used in your first C program is gone; `malloc`, threads, files, and network are all gone. A kernel is just a program that runs on raw hardware, and `_start` is where it begins.

## Why it matters here (OSDev_Learning_Hub)
The entry point is the exact junction where bootloader and kernel meet. `synthesized_tutorials/00-introduction/01-how-a-computer-boots.md` defines it in its "key terms" table as "the symbol (usually `_start`) the bootloader jumps to." `Example_OS_Project/c/boot.s` defines and exports `_start`, `Example_OS_Project/c/linker.ld` declares `ENTRY(_start)`, and the bootloader ([GRUB](grub.md) or QEMU `-kernel`) performs the jump. See also [Multiboot](multiboot.md) and [Linker](linker.md).

## Watch / listen
[- How the C++ Linker Works - The Cherno](https://www.youtube.com/watch?v=H4s55GgAg0I) — how the entry point is found and linked
- [OSDev Wiki — Bare Bones](https://wiki.osdev.org/Bare_Bones) — free; shows the `_start` entry point and bootstrap stack
- [OSDev Wiki — Kernel Entry Point](https://wiki.osdev.org/Kernel_Entry_Point) — free, authoritative

## Related terms
- [Bootloader](bootloader.md)
- [Multiboot](multiboot.md)
- [Linker](linker.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
