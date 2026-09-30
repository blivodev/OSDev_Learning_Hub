# Concept — VGA Text Mode & Your First "Hello World"

*Original content written for OSDev_Learning_Hub.*

## In one sentence
Before you have a hard drive, a keyboard, or a framebuffer driver, you can already put text on the screen by writing directly to a fixed block of memory: **`0xB8000`**.

## What VGA text mode is

In [text mode](../../GLOSSARY/vga-text-mode.md "The 80x25 character display mode a minimal kernel writes to"), the screen is a grid of **80 columns × 25 rows** = 2000 cells. Each cell is **2 bytes**:

```
┌────────────┬────────────┐
│ char (low) │ color(high)│
│  'A' (0x41)│  0x0F      │
└────────────┴────────────┘
```

So writing the string `"Hello World!"` means writing 12 such 2-byte cells starting at `0xB8000`:

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

The color byte `0x0F` = foreground `0xF` (white) + background `0x0` (black). Lower 4 bits = foreground, upper 4 bits = background.

```
color byte:
 bits 7 6 5 4   = background
 bits 3 2 1 0   = foreground
```

## The universal "Hello World" driver

Here's the same 20-line [VGA terminal driver](../../GLOSSARY/vga-text-mode.md "The 80x25 character display mode a minimal kernel writes to") in C. **Every** language version in this hub builds the same logic — only the syntax differs:

```c
#define VGA_WIDTH  80
#define VGA_HEIGHT 25
#define VGA_MEMORY ((unsigned short*)0xB8000)

static int row = 0;
static int col = 0;

void term_putchar(char c) {
    if (c == '\n') { row++; col = 0; return; }   // newline
    if (c == '\r') { col = 0; return; }          // carriage return
    VGA_MEMORY[row * VGA_WIDTH + col] = (0x0F << 8) | (unsigned char)c;
    col++;
    if (col >= VGA_WIDTH) { col = 0; row++; }    // wrap
    if (row >= VGA_HEIGHT) { row = 0; }          // scroll (naive)
}

void term_write(const char* s) { while (*s) term_putchar(*s++); }

void kernel_main(void) {
    term_write("Hello World!");
    // halt forever — the kernel never returns
    for (;;) ;
}
```

## The complete beginner flow (any language)
```mermaid
flowchart TD
    A[Boot: bootloader jumps to _start] --> B[Set up stack]
    B --> C[Call kernel_main]
    C --> D[Write 'H','e','l',... to 0xB8000]
    D --> E[Halt forever]
```

## What QEMU shows you
![Screenshot]: Add a screenshot here — a black [QEMU](../../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing") window with white text reading "Hello World!".

That's it. That is literally all a "Hello World" OS does — but it's the *proof* that your entire toolchain works and you own the machine.

> **Next:** [`05-the-hello-world-of-oses.md`](05-the-hello-world-of-oses.md) — the one kernel you'll build in all five languages.

## Watch and learn

- [How VGA Works](https://www.youtube.com/watch?v=5exFKr-JJtg) — Tech Tangents explains VGA signals and hardware, the display standard your text-mode hello world drives.
- [Building an OS - 1 - Hello world](https://www.youtube.com/watch?v=9t-SPTC7Tczc) — Nanobyte writes a hello-world program in assembly and boots it from a floppy, the classic first step.
- [Building an OS - 5 - How to implement printf](https://www.youtube.com/watch?v=dG8PV6xqm4s) — Nanobyte builds a `printf` that writes formatted text to the screen, a gateway to real VGA text output.
