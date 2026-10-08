/* serial.h — 16550 UART driver using REAL x86 port I/O (inb/outb).
 * x86 serial is PORT-mapped, so we must use the `out`/`in` instructions,
 * not memory stores. That's why the earlier version hung (THRE never set).
 */
#ifndef SERIAL_H
#define SERIAL_H

#define COM1 0x3F8

static inline void outb(unsigned short port, unsigned char val) {
    __asm__ volatile ("outb %0, %1" : : "a"(val), "Nd"(port));
}
static inline unsigned char inb(unsigned short port) {
    unsigned char ret;
    __asm__ volatile ("inb %1, %0" : "=a"(ret) : "Nd"(port));
    return ret;
}

static inline void serial_init(void) {
    outb(COM1 + 1, 0x00);   /* IER: no interrupts */
    outb(COM1 + 3, 0x80);   /* LCR: DLAB = 1 */
    outb(COM1 + 0, 0x03);   /* DLL: 38400 baud */
    outb(COM1 + 1, 0x00);   /* DLM */
    outb(COM1 + 3, 0x03);   /* LCR: 8N1, DLAB = 0 */
    outb(COM1 + 2, 0xC7);   /* FCR: enable FIFO, clear, 14-byte trigger */
    outb(COM1 + 4, 0x0B);   /* MCR: DTR + RTS + OUT2 */
}

static inline void serial_wait_tx(void) {
    while (!(inb(COM1 + 5) & 0x20)) { }   /* LSR: wait THRE */
}

static inline void serial_putc(char c) {
    serial_wait_tx();
    outb(COM1, (unsigned char)c);
}

static inline void serial_write(const char* s) {
    while (*s) serial_putc(*s++);
}

#endif
