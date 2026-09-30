/* boot.s — Universal Multiboot bootstrap (GNU as / AT&T syntax)
 *
 * THIS FILE IS SHARED BY THE C, C++ AND GO KERNELS in Example_OS_Project.
 * It is the FIRST thing the bootloader (GRUB or QEMU -kernel) runs.
 *
 * Job of this file (in order):
 *   1. Emit the Multiboot header (magic 0x1BADB002) so a bootloader
 *      recognizes this as a valid kernel image.
 *   2. Reserve a 16 KiB stack (the CPU has NO stack when it boots).
 *   3. Jump to the high-level kernel entry point (kernel_main).
 *   4. If the kernel somehow returns, halt forever.
 *
 * Build with the GNU assembler (does not require NASM):
 *     as --32 boot.s -o boot.o
 */

/* ---- Multiboot header ----------------------------------------------- */
/* The bootloader scans the start of the image for these 12 bytes. */
.set ALIGN,    1<<0              /* align loaded modules on page boundaries */
.set MEMINFO,  1<<1              /* provide memory map */
.set FLAGS,    ALIGN | MEMINFO   /* this is the Multiboot 'flag' field */
.set MAGIC,    0x1BADB002        /* 'magic number' lets bootloader find header */
.set CHECKSUM, -(MAGIC + FLAGS)  /* checksum of above, to prove we are multiboot */

.section .multiboot
.align 4
.long MAGIC
.long FLAGS
.long CHECKSUM

/* ---- Bootstrap stack ------------------------------------------------ */
/* The CPU boots with an undefined stack pointer. We reserve 16 KiB of
 * uninitialized (BSS) memory and point esp/ebp at its top. */
.section .bootstrap_stack, "aw", @nobits
stack_bottom:
.skip 16384                      /* 16 KiB */
stack_top:

/* ---- Kernel entry point -------------------------------------------- */
.section .text
.global _start
.type _start, @function
_start:
    movl $stack_top, %esp        /* point the stack at the top of our 16 KiB */
    movl $stack_top, %ebp        /* set the frame pointer too (for debugging) */

    call kernel_main              /* jump into the C/C++/Go kernel */

    cli                          /* clear the interrupt flag (no more irqs) */
    hlt                          /* halt the CPU */

/* Safety net: if kernel_main somehow returns, loop forever. */
.Lhang:
    jmp .Lhang
.size _start, . - _start
