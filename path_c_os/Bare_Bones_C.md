# OSDev Wiki — Bare Bones (C)

> Source: https://wiki.osdev.org/Bare_Bones — community-reviewed, beginner minimal-kernel tutorial.
> This is a **converted/summarized** reference copy for offline reading. Full authoritative version at the URL above; 32-bit x86 kernel booted by GRUB/Multiboot.

---

## Overview

Write a simple 32-bit [x86](../GLOSSARY/x86.md "The CPU architecture family this hub targets") kernel and boot it with the **[GRUB](../GLOSSARY/grub.md "The free GNU bootloader that loads Multiboot kernels")** bootloader using the **[Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002")** boot protocol.

Tools used:
- **[GNU Linker](../GLOSSARY/linker.md "Merges object files into one image at a chosen address")** (`ld`) — link object files into the final kernel.
- **[GNU Assembler](../GLOSSARY/assembler.md "Turns assembly language into machine-code object files")** (`as`, or optionally **NASM**) — assemble instructions into object files of machine code.
- **GNU Compiler Collection** (`gcc`) — compile high-level C into assembly.
- **C** — write the high-level kernel logic.
- **GRUB** — bootloader that loads us into 32-bit [protected mode](../GLOSSARY/protected-mode.md "The 32-bit CPU mode Multiboot v1 kernels run in") (paging disabled).
- **[ELF](../GLOSSARY/elf.md "The executable format that lets a bootloader load your kernel")** — executable format controlling where/how the kernel is loaded.

> Windows users can complete this from WSL, MinGW, or Cygwin.

---

## 1. Building a Cross-Compiler

You need a [cross-compiler](../GLOSSARY/cross-compiler.md "A compiler that builds code for a different CPU/OS than the one it runs on") targeting `i686-elf`. Setting one up is essential and non-optional (this is where the OSDev tutorial's *GCC Cross-Compiler* page matters most). For a quick beginner test on a normal machine you can sometimes use native x86_64 GCC with [Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002"), but a real target uses `i686-elf-gcc`.

---

## 2. Bootstrap Assembly (`boot.s`)

Sets up the CPU environment and declares the **Multiboot header** so GRUB recognizes the kernel:

```nasm
# Declare constants for the multiboot header.
.set ALIGN,    1<<0              # align loaded modules on page boundaries
.set MEMINFO,  1<<1              # provide memory map
.set FLAGS,    ALIGN | MEMINFO   # this is the Multiboot 'flag' field
.set MAGIC,    0x1BADB002        # 'magic number' lets bootloader find the header
.set CHECKSUM, -(MAGIC + FLAGS)  # checksum of above, to prove we are multiboot

.section .multiboot
.align 4
.long MAGIC
.long FLAGS
.long CHECKSUM

# Provide our own stack (16 KiB).
.section .bootstrap_stack, "aw", @nobits
stack_bottom:
.skip 16384
stack_top:

.section .text
.global _start
.type _start, @function
_start:
    mov $stack_top, %esp        # set up the stack
    call kernel_main             # call the C entry point
    hlt                          # halt the CPU (should never return)
```

Key idea: the `.multiboot` section with `MAGIC = 0x1BADB002` is what GRUB searches for at the start of the kernel image.

---

## 3. Kernel (`kernel.c`)

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// VGA text-mode terminal driver.
static const size_t VGA_WIDTH  = 80;
static const size_t VGA_HEIGHT = 25;
static uint16_t* const VGA_MEMORY = (uint16_t*) 0xB8000;

void terminal_initialize(void) {
    // fill the buffer with blank ' ' characters
    for (size_t y = 0; y < VGA_HEIGHT; y++)
        for (size_t x = 0; x < VGA_WIDTH; x++) {
            const size_t index = y * VGA_WIDTH + x;
            VGA_MEMORY[index] = (uint16_t) 0x0F00 | ' ';
        }
}

// main entry point, called from _start
void kernel_main(void) {
    terminal_initialize();
    // write "Hello World!" at the top-left of the screen
    const char* msg = "Hello World!";
    size_t i = 0;
    while (msg[i] != '\0') {
        VGA_MEMORY[i] = (uint16_t) 0x0F00 | msg[i];
        i++;
    }
}
```

- `0xB8000` is the VGA text-mode framebuffer in real/protected mode: 80 columns × 25 rows of 16-bit cells.
- Each cell: low byte = character, high byte = color (here `0x0F` = white on black).

---

## 4. Linking (`linker.ld`)

Tells the [linker](../GLOSSARY/linker.md "Merges object files into one image at a chosen address") where to place sections and sets the [entry point](../GLOSSARY/entry-point.md "The symbol (usually _start) the bootloader jumps to"):

```ld
ENTRY(_start)

SECTIONS {
    . = 1M;                       /* load kernel at 1 MiB (conventional) */

    .text BLOCK(4K) : ALIGN(4K) {
        *(.multiboot)
        *(.text)
    }
    .rodata BLOCK(4K) : ALIGN(4K) { *(.rodata) }
    .data   BLOCK(4K) : ALIGN(4K) { *(.data) }
    .bss    BLOCK(4K) : ALIGN(4K) { *(COMMON) *(.bss) *(.bootstrap_stack) }
}
```

The `1M` origin is where kernels are conventionally loaded by GRUB/Multiboot.

---

## 5. Build commands

```bash
# Assemble bootstrap
nasm -f elf32 boot.s -o boot.o        # or: as --32 boot.s -o boot.o
# Compile kernel as freestanding
gcc -c kernel.c -o kernel.o -ffreestanding -O2 -Wall -Wextra
# Link
ld -T linker.ld -o myos.bin -ffreestanding -nostdlib boot.o kernel.o
# Test with QEMU
qemu-system-i386 -kernel myos.bin
```

---

## Key takeaways (beginner)
1. **Multiboot header** (`0x1BADB002`) is how a bootloader recognizes your kernel.
2. **`-ffreestanding`** tells the compiler "no standard library / no host OS".
3. **VGA text buffer at `0xB8000`** — direct memory writes are how you print without an OS.
4. Kernels are conventionally linked at **1 MiB**.
