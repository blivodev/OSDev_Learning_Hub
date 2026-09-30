# Chapter 01 — Building "Hello World!" in C

*Original content written for OSDev_Learning_Hub — walks through the real,
verified code in `Example_OS_Project/c/`.*

## What you'll have at the end
A 5 KB [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") that boots in [QEMU](../../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing") and prints:
```
Hello World!
Welcome to your very own operating system (C edition).
```
**This is real and verified** — the exact files below booted in QEMU and
the [VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") was read back to confirm the text.

## Step 1 — `boot.s` (the Multiboot bootstrap)
Every C bare-metal kernel needs a tiny assembly file to (a) declare the
[Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002") header so a [bootloader](../../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") recognizes it, and (b) give the CPU a
stack (it has none when it boots). Full file: `c/boot.s`.

The three lines that matter most:
```nasm
.long 0x1BADB002          ; magic: bootloader's handshake
.long 0x03                ; flags: align + memory-map
.long -(0x1BADB002 + 0x03); checksum: magic+flags+checksum must = 0
```
Then it sets up a stack and calls the C function:
```nasm
movl $stack_top, %esp     ; point the stack at our 16 KiB
call kernel_main           ; jump into the C kernel
```

## Step 2 — `kernel.c` (the VGA driver + entry point)
The heart. It writes directly to the VGA text framebuffer at `0xB8000`:

```c
#define VGA_WIDTH   80
#define VGA_HEIGHT  25
#define VGA_MEMORY  ((unsigned short*)0xB8000)   // the text framebuffer
#define COLOR_WHITE_ON_BLACK  0x0F

static void vga_putchar(char c) {
    if (c == '\n') { col = 0; row++; if (row >= VGA_HEIGHT) row = 0; return; }
    unsigned int index = row * VGA_WIDTH + col;
    VGA_MEMORY[index] = (unsigned short)((COLOR_WHITE_ON_BLACK << 8) | (unsigned char)c);
    /* advance the cursor, wrap at the end of the line ... */
}
```
A VGA cell is `[color<<8 | char]` — the color byte's low nibble is the
foreground, the high nibble the background.

## Step 3 — `linker.ld` (where the kernel lives in memory)
Tells `ld` to load the kernel at **1 MiB** and put the `.multiboot` section
first:
```ld
ENTRY(_start)        /* bootloader jumps here */
SECTIONS {
    . = 1M;          /* load at 1 MiB, the convention */
    .text BLOCK(4K) : ALIGN(4K) { *(.multiboot) *(.text) }
    .rodata BLOCK(4K) : ALIGN(4K) { *(.rodata) }
    .data   BLOCK(4K) : ALIGN(4K) { *(.data) }
    .bss    BLOCK(4K) : ALIGN(4K) { *(COMMON) *(.bss) *(.bootstrap_stack) }
}
```

## Step 4 — build & run
```bash
make           # or the explicit commands:
as --32 boot.s -o boot.o
gcc -c kernel.c -o kernel.o -ffreestanding -fno-pie -m32 -nostdlib -O2
ld -m elf_i386 -T linker.ld -o kernel.bin boot.o kernel.o -nostdlib

make run-c     # boots kernel.bin in QEMU
```

## Verification we actually ran
```bash
grub-file --is-x86-multiboot c/kernel.bin   # ✅ VALID Multiboot v1 kernel
# then booted in QEMU and read the VGA buffer at 0xB8000:
#   Hello World!
#   Welcome to your very own operating system (C edition).
```

> **Bridge to OS concepts:** you just touched three core OS ideas —
> **[bootloaders](../../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it")/[Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002")** (concepts/01), **memory layout** via the linker
> script (concepts/02), and **direct hardware I/O** through the
> [VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") (concepts/04).

---

## Watch and learn

- [CS50x 2025 - Lecture 4 - Memory](https://youtu.be/kcRdFGbzR1I) — David Malan's classic lecture on pointers, hexadecimal addresses, the stack and heap, and how C manipulates memory — the exact mental model behind poking `0xB8000` and reading a VGA cell back.
- [CS50x 2026 - Section 4 - Memory](https://youtu.be/Gjf0L3mkVtY) — A refreshed, hands-on walkthrough of C pointers, dynamic memory allocation, and files, reinforcing the pointer syntax your kernel's `vga_putchar` and `VGA_MEMORY` indexing rely on.
- [C pointers explained](https://youtube.com/watch?v=DplxIq0mc_Y) — A concise crash course on what a pointer is, `&` vs `*`, pointers as function arguments, and dereferencing — ideal for grounding the `unsigned short*` cast to the VGA framebuffer.
