/* kernel.c — A minimal "Hello World!" OS kernel in C.
 *
 * This is the C reference implementation. It:
 *   1. Implements a tiny VGA text-mode driver (writes to 0xB8000).
 *   2. Prints "Hello World!" to the screen.
 *   3. Halts forever (a kernel never returns to an OS — there is none).
 *
 * Compile (freestanding — no libc):
 *     gcc -c kernel.c -o kernel.o -ffreestanding -fno-pie -m32 \
 *         -nostdlib -O2 -Wall -Wextra
 */

/* ---- VGA text-mode constants --------------------------------------- */
#define VGA_WIDTH   80            /* columns */
#define VGA_HEIGHT  25            /* rows */
#define VGA_MEMORY  ((unsigned short*)0xB8000)   /* the text framebuffer */

/* The color byte: low nibble = foreground, high nibble = background.
 * 0x0 = black, 0xF = white. 0x0F = white text on black background. */
#define COLOR_WHITE_ON_BLACK  0x0F

/* ---- Serial (COM1) output ---- */
#include "serial.h"

/* ---- Simple terminal state ----------------------------------------- */
static int terminal_row = 0;
static int terminal_col = 0;

/* Write ONE character to the VGA framebuffer at the current cursor.
 * A VGA cell is 2 bytes: [char][color]. */
static void vga_putchar(char c)
{
    if (c == '\n') {             /* handle newline: wrap to next row */
        terminal_col = 0;
        terminal_row++;
        if (terminal_row >= VGA_HEIGHT)
            terminal_row = 0;    /* naive scroll: wrap to top */
        return;
    }

    const unsigned int index = terminal_row * VGA_WIDTH + terminal_col;
    /* cell = (color << 8) | character */
    VGA_MEMORY[index] = (unsigned short)((COLOR_WHITE_ON_BLACK << 8) | (unsigned char)c);

    terminal_col++;
    if (terminal_col >= VGA_WIDTH) {   /* wrap at end of line */
        terminal_col = 0;
        terminal_row++;
        if (terminal_row >= VGA_HEIGHT)
            terminal_row = 0;
    }
}

/* Print a NUL-terminated string to the screen. */
static void vga_write(const char* s)
{
    while (*s)
        vga_putchar(*s++);
}

/* Clear the whole screen by filling every cell with a blank space. */
static void vga_clear(void)
{
    for (int y = 0; y < VGA_HEIGHT; y++) {
        for (int x = 0; x < VGA_WIDTH; x++) {
            const unsigned int index = y * VGA_WIDTH + x;
            VGA_MEMORY[index] = (unsigned short)((COLOR_WHITE_ON_BLACK << 8) | ' ');
        }
    }
    terminal_row = 0;
    terminal_col = 0;
}

/* ---- Kernel entry point -------------------------------------------- */
/* Called by boot.s (`call kernel_main`). Note: even though this is C,
 * it is NOT main() — there is no runtime, no libc, no OS to return to. */
void kernel_main(void)
{
    vga_clear();
    vga_write("Hello World!\n");
    vga_write("Welcome to your very own operating system (C edition).\n");


    /* Also echo to COM1 serial so the kernel works in headless mode:
     *   qemu-system-i386 -kernel kernel.bin -nographic -serial stdio
     * prints this to the terminal (no graphical display needed). */
    serial_init();
    serial_write("Hello World!\n");
    serial_write("Welcome to your very own operating system (C edition).\n");

    /* A kernel never returns. If it did, boot.s would hang in a loop. */
    for (;;)
        /* spin */;
}
