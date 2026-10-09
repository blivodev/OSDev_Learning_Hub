/* kernel.c — A minimal "Hello World!" OS kernel in C.
 *
 * Writes to the VGA text buffer (0xB8000) AND to COM1 serial, so it works
 * both in a graphical QEMU window and headless (serial -> terminal).
 */
#define VGA_WIDTH   80
#define VGA_HEIGHT  25
#define VGA_MEMORY  ((unsigned short*)0xB8000)
#define COLOR_WHITE_ON_BLACK  0x0F

/* ---- Serial (COM1) output ------------------------------------------- */
#define COM1 0x3F8
static inline void outb(unsigned short port, unsigned char val) {
    __asm__ volatile ("outb %0, %1" : : "a"(val), "Nd"(port));
}
static inline unsigned char inb(unsigned short port) {
    unsigned char ret;
    __asm__ volatile ("inb %1, %0" : "=a"(ret) : "Nd"(port));
    return ret;
}
static void serial_init(void) {
    outb(COM1 + 1, 0x00);
    outb(COM1 + 3, 0x80);
    outb(COM1 + 0, 0x03);
    outb(COM1 + 1, 0x00);
    outb(COM1 + 3, 0x03);
    outb(COM1 + 2, 0xC7);
    outb(COM1 + 4, 0x0B);
}
static void serial_putc(char c) {
    while (!(inb(COM1 + 5) & 0x20)) { }
    outb(COM1, (unsigned char)c);
}
static void serial_write(const char* s) {
    while (*s) serial_putc(*s++);
}

/* ---- VGA text output ------------------------------------------------ */
static int terminal_row = 0;
static int terminal_col = 0;
static void vga_putchar(char c) {
    if (c == '\n') { terminal_col = 0; terminal_row++; if (terminal_row >= VGA_HEIGHT) terminal_row = 0; return; }
    const unsigned int index = terminal_row * VGA_WIDTH + terminal_col;
    VGA_MEMORY[index] = (unsigned short)((COLOR_WHITE_ON_BLACK << 8) | (unsigned char)c);
    terminal_col++;
    if (terminal_col >= VGA_WIDTH) { terminal_col = 0; terminal_row++; if (terminal_row >= VGA_HEIGHT) terminal_row = 0; }
}
static void vga_write(const char* s) { while (*s) vga_putchar(*s++); }

/* ---- Kernel entry point -------------------------------------------- */
void kernel_main(void)
{
    serial_init();
    vga_write("Hello World!\n");
    vga_write("Welcome to your very own operating system (C edition).\n");
    serial_write("Hello World!\n");
    serial_write("Welcome to your very own operating system (C edition).\n");

    for (;;)
        /* spin */;
}
