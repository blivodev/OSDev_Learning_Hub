/* linker.ld — Universal linker script for Example_OS_Project (C/C++/Go)
 *
 * Tells GNU ld WHERE to place the kernel in memory and what the
 * entry point is. Shared by all "multiboot + GNU as" kernels.
 *
 * KEY IDEA: . = 1M; loads the kernel at 1 MiB, the conventional place
 * where bootloaders put kernels (below that is BIOS/reserved memory).
 * The .multiboot section must come FIRST so the magic header is at the
 * very start of the image for the bootloader to find.
 */

ENTRY(_start)                     /* the entry point the bootloader jumps to */

SECTIONS
{
    . = 1M;                       /* load at 1 MiB */

    .text BLOCK(4K) : ALIGN(4K)
    {
        *(.multiboot)             /* multiboot header first */
        *(.text)                  /* the code */
    }

    .rodata BLOCK(4K) : ALIGN(4K)
    {
        *(.rodata)                /* read-only data (string literals, etc.) */
    }

    .data BLOCK(4K) : ALIGN(4K)
    {
        *(.data)                  /* initialized data */
    }

    .bss BLOCK(4K) : ALIGN(4K)
    {
        *(COMMON)
        *(.bss)                   /* uninitialized data (stack, buffers) */
        *(.bootstrap_stack)
    }
}
