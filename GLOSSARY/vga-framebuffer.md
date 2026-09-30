<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# VGA Framebuffer (`0xB8000`)

> **[Back to glossary index](README.md)** · Category: Display

The VGA framebuffer is the fixed block of memory at `0xB8000` where the VGA text screen lives: each character on the 80×25 screen is one 2-byte cell stored here.

## The short version
In text mode you don't ask the graphics card to draw — you just write to `0xB8000`, a memory region the VGA hardware maps directly to the screen. Each cell is a character byte plus a color byte, and the CPU can read and write it like plain RAM, which is why printing a "Hello World!" OS is so simple.

## Detailed explanation
`0xB8000` is the start of the text-mode framebuffer: memory that the VGA controller continuously scans and renders. The screen has **80 columns × 25 rows = 2000 cells**, and each cell is **2 bytes** laid out as:

```text
┌────────────┬────────────┐
│ char (low) │ color(high)│
│  'A' (0x41)│  0x0F      │
└────────────┴────────────┘
```

Indexing is `row * 80 + column`, exactly as in the sample driver:

```c
#define VGA_WIDTH  80
#define VGA_HEIGHT 25
#define VGA_MEMORY ((unsigned short*)0xB8000)

// kernel.c
const unsigned int index = terminal_row * VGA_WIDTH + terminal_col;
VGA_MEMORY[index] = (unsigned short)((COLOR_WHITE_ON_BLACK << 8) | (unsigned char)c);
```

The color byte's **low nibble is the foreground, high nibble the background**; `0x0F` is white on black. Because the framebuffer is plain memory-mapped hardware ([memory-mapped I/O](memory-management.md)), the kernel needs no I/O-port driver to print — it just stores the cells. The first 16 KiB of VGA memory covers the 2000-cell text buffer (at 2 bytes each, 4000 bytes used; the rest covers other planes).

The framebuffer concept generalizes: in graphics modes the buffer instead holds pixel data, and the *address* differs, but the principle — "the screen is a chunk of memory you write to" — is identical. The text-mode `0xB8000` buffer is simply the friendliest first example because characters, not pixels, are the unit.

## Why it matters here (OSDev_Learning_Hub)
`Example_OS_Project/c/kernel.c` centers on this buffer: `VGA_MEMORY ((unsigned short*)0xB8000)` and the `[char][color]` cell layout the tutorial above documents. `04-vga-text-mode.md` walks through writing `"Hello World!"` as twelve 2-byte cells starting at `0xB8000`. It's the hub's very first "own the machine" moment and the foundation every later [VGA text mode](vga-text-mode.md) driver builds on.

## Watch / listen
- [OSDev Wiki — Text Mode Cursor](https://wiki.osdev.org/Text_Mode_Cursor) — free, authoritative (related)
- [OSDev Wiki — VGA Hardware](https://wiki.osdev.org/VGA_Hardware) — free, authoritative
- [Wikipedia — Memory-mapped I/O](https://en.wikipedia.org/wiki/Memory-mapped_I/O) — free, authoritative

## Related terms
- [VGA Text Mode](vga-text-mode.md)
- [Memory Management](memory-management.md)
- [Kernel](kernel.md)
- [Frame Buffer](framebuffer.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
