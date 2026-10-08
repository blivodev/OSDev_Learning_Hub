// kernel.c++ — A minimal "Hello World!" OS kernel in C++.
//
// This is the C++ reference implementation. Same idea as the C kernel,
// with the two C++-specific things that matter on bare metal:
//   1. extern "C" = the entry point has C linkage so boot.s can call it.
//   2. -fno-exceptions -fno-rtti = C++ exceptions/RTTI need a runtime that
//      does not exist on bare metal, so we compile without them.
//
// We deliberately use ONLY built-in C/C++ types (char, unsigned short)
// and NO standard headers: <cstdint> would pull in the C++ runtime
// headers, which are neither freestanding-safe nor available in a
// -m32 toolchain on most systems. On bare metal you bring your own.
//
// Compile (freestanding C++):
//   g++ -c kernel.c++ -o kernel.o -ffreestanding -fno-pie -m32
//       -nostdlib -fno-exceptions -fno-rtti -O2 -Wall -Wextra

// ---- VGA text-mode constants (same as the C kernel) -----------------
// The framebuffer address is a POINTER (0xB8000 does not fit in
// unsigned short). We use a macro like the C kernel to avoid C++'s
// constexpr + reinterpret_cast restrictions on bare metal.
#define VGA_SCREEN ((unsigned short*)0xB8000)

#include "serial.h"

namespace vga {
    constexpr unsigned short WIDTH  = 80;
    constexpr unsigned short HEIGHT = 25;
    constexpr unsigned short COLOR  = 0x0F;  // white on black

    int row = 0;
    int col = 0;

    // Write a single character as a [char][color] cell to the framebuffer.
    inline void putchar(char c) {
        if (c == '\n') { col = 0; row++; if (row >= HEIGHT) row = 0; return; }
        unsigned short* cell = VGA_SCREEN + (row * WIDTH + col);
        *cell = (unsigned short)((COLOR << 8) | (unsigned char)c);
        col++;
        if (col >= WIDTH) { col = 0; row++; if (row >= HEIGHT) row = 0; }
    }

    void write(const char* s) {
        while (*s) putchar(*s++);
    }

    void clear() {
        unsigned short* cell = VGA_SCREEN;

        for (int i = 0; i < WIDTH * HEIGHT; i++)
            cell[i] = (unsigned short)((COLOR << 8) | ' ');
        row = 0; col = 0;
    }
}

// ---- Kernel entry point ---------------------------------------------
// extern "C" = C linkage. Without it, the C++ compiler would "mangle"
// kernel_main into something like _Z11kernel_mainv, which boot.s could
// not call. C linkage keeps the exported symbol exactly "kernel_main".
extern "C" void kernel_main() {
    vga::clear();
    vga::write("Hello World!\n");
    vga::write("Welcome to your very own operating system (C++ edition).\n");

    serial_init();
    serial_write("Hello World!\n");
    serial_write("Welcome to your very own operating system (C++ edition).\n");

    for (;;)   // a kernel never returns
        ;
}
