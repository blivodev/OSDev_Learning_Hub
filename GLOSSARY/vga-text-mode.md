<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# VGA Text Mode

> **[Back to glossary index](README.md)** · Category: Display

VGA text mode is the basic 80×25 character display mode a minimal kernel writes to by placing 2-byte cells directly in memory at `0xB8000`.

## The short version
Before you have a hard drive, a keyboard, or a framebuffer driver, you can already put text on screen by writing to a fixed block of memory at `0xB8000`. The screen is a grid of **80 columns × 25 rows** (2000 cells), each cell 2 bytes — a character byte and a color byte — and that single mechanism is the entire basis of a "Hello World!" OS.

## Detailed explanation
In text mode the screen is a grid of 80×25 = **2000 cells**. Each cell is 2 bytes:

```text
┌────────────┬────────────┐
│ char (low) │ color(high)│
│  'A' (0x41)│  0x0F      │
└────────────┴────────────┘
```

The low byte holds the character (e.g. `'A'` = `0x41`), and the high byte the color. The color byte splits as: **bits 7–4 = background, bits 3–0 = foreground**. So `0x0F` means white (`0xF`) foreground on black (`0x0`) background. To write the string `"Hello World!"` you store 12 such 2-byte cells starting at `0xB8000`:

```c
unsigned short* vga = (unsigned short*)0xB8000;
vga[0] = 0x0F48;   // 'H'
vga[1] = 0x0F65;   // 'e'
vga[2] = 0x0F6C;   // 'l'
vga[3] = 0x0F6C;   // 'l'
vga[4] = 0x0F6F;   // 'o'
vga[5] = 0x0F20;   // ' '
vga[6] = 0x0F57;   // 'W'
vga[7] = 0x0F6F;   // 'o'
vga[8] = 0x0F72;   // 'r'
vga[9] = 0x0F6C;   // 'l'
vga[10] = 0x0F64;  // 'd'
vga[11] = 0x0F21;  // '!'
```

The memory at `0xB8000` is the [VGA framebuffer](vga-framebuffer.md). A small terminal driver tracks a row/column, writes each character as `(color << 8) | char`, handles newline/carriage-return, wraps at 80 columns, and scrolls (the sample does a naive wrap to top). This works because the hardware makes the text buffer a plain, CPU-writable memory region — no device driver required to print.

## Why it matters here (OSDev_Learning_Hub)
The entire beginner flow in `04-vga-text-mode.md` and `Example_OS_Project/c/kernel.c` builds on text mode: `kernel.c` defines `VGA_WIDTH 80`, `VGA_HEIGHT 25`, `VGA_MEMORY ((unsigned short*)0xB8000)`, and `COLOR_WHITE_ON_BLACK 0x0F`, then `vga_putchar`/`vga_clear`/`vga_write` drive it. `boot.s` hands control to `kernel_main`, which writes "Hello World!" and halts. It is the proof that your entire toolchain works — and the same `0xB8000` [framebuffer](vga-framebuffer.md) is what higher-level display modes replace later.

## Watch / listen
[- Writing an OS in Rust - Part 3 - VGA Text Mode - Uncle Scientist](https://www.youtube.com/watch?v=DA2zIAkE26Q) — printing to the VGA text buffer
- [OSDev Wiki — Text Mode Cursor](https://wiki.osdev.org/Text_Mode_Cursor) — free, authoritative (related)
- [OSDev Wiki — VGA Hardware](https://wiki.osdev.org/VGA_Hardware) — free, authoritative
- [Wikipedia — VGA text mode](https://en.wikipedia.org/wiki/VGA_text_mode) — free, authoritative

## Related terms
- [VGA Framebuffer (`0xB8000`)](vga-framebuffer.md)
- [Hardware Interrupt](interrupt.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
