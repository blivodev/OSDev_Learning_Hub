/* linker.ld — linker script for the Go kernel
 *
 * Same as the C/C++ linker script: load the kernel at 1 MiB, put the
 * Multiboot header first. Used to link boot.o + kernel.go.o + terminal.go.o.
 *
 * Link (requires a Go-enabled i686-elf cross-compiler):
 *   i686-elf-gcc -T linker.ld -o kernel.bin -ffreestanding -O2 -nostdlib \
 *       boot.o kernel.go.o terminal.go.o -lgcc
 */

ENTRY(_start)

SECTIONS
{
    . = 1M;

    .text BLOCK(4K) : ALIGN(4K)
    {
        *(.multiboot)
        *(.text)
    }

    .rodata BLOCK(4K) : ALIGN(4K)
    {
        *(.rodata)
    }

    .data BLOCK(4K) : ALIGN(4K)
    {
        *(.data)
    }

    .bss BLOCK(4K) : ALIGN(4K)
    {
        *(COMMON)
        *(.bss)
        *(.bootstrap_stack)
    }
}
