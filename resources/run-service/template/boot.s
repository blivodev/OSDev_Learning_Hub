/* boot.s — Universal Multiboot bootstrap (GNU as / AT&T syntax)
 *
 * Emits the Multiboot header (magic 0x1BADB002), reserves a 16 KiB stack,
 * and jumps to kernel_main. Shared by the C/C++ kernels.
 *
 * Build:  as --32 boot.s -o boot.o
 */

.set ALIGN,    1<<0
.set MEMINFO,  1<<1
.set FLAGS,    ALIGN | MEMINFO
.set MAGIC,    0x1BADB002
.set CHECKSUM, -(MAGIC + FLAGS)

.section .multiboot
.align 4
.long MAGIC
.long FLAGS
.long CHECKSUM

.section .bootstrap_stack, "aw", @nobits
stack_bottom:
.skip 16384
stack_top:

.section .text
.global _start
.type _start, @function
_start:
    movl $stack_top, %esp
    movl $stack_top, %ebp
    call kernel_main
    cli
    hlt
.Lhang:
    jmp .Lhang
.size _start, . - _start
