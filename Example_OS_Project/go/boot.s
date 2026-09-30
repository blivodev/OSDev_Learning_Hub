// boot.s — Go kernel bootstrap (GNU as / AT&T syntax)
//
// Same universal Multiboot bootstrap as the C/C++ kernels, with one
// Go-specific extra: it defines the Go-runtime stub symbols
// (__go_register_gc_roots and __go_runtime_error) as empty functions so
// the linker is satisfied. Without these, gccgo emits "undefined
// reference" errors when building a freestanding kernel.
//
// Build:     as --32 boot.s -o boot.o
// NOTE: the Go kernel is typically built for i686-elf with a Go-enabled
// cross-compiler (i686-elf-gccgo). See docs/setup.md.

/* ---- Multiboot header ----------------------------------------------- */
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

/* ---- Bootstrap stack ------------------------------------------------ */
.section .bootstrap_stack, "aw", @nobits
stack_bottom:
.skip 16384
stack_top:

/* ---- Go runtime stub symbols ---------------------------------------- */
/* The Go runtime expects these; freestanding builds don't need real
 * implementations, so we provide empty functions to satisfy the link. */
.global __go_register_gc_roots
.type __go_register_gc_roots, @function
__go_register_gc_roots:
    ret
.size __go_register_gc_roots, . - __go_register_gc_roots

.global __go_runtime_error
.type __go_runtime_error, @function
__go_runtime_error:
    ret
.size __go_runtime_error, . - __go_runtime_error

/* ---- Kernel entry point --------------------------------------------- */
.section .text
.global _start
.type _start, @function
_start:
    movl $stack_top, %esp
    movl $stack_top, %ebp

    call main                    /* Go kernel entry point is "main" */

    cli
    hlt
.Lhang:
    jmp .Lhang
.size _start, . - _start
