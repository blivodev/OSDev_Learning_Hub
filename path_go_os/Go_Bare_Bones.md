# OSDev Wiki — Go Bare Bones

> Source: https://wiki.osdev.org/Go_Bare_Bones — community-reviewed (difficulty: Medium).
> This is a **converted/summarized** reference copy for offline reading.

---

## Preface

Go was **not designed for OS development** — you'll be fighting the language. It is highly recommended to first read the C Bare Bones tutorial. For a *production* framework supporting OS dev in Go, see **TamaGo**.

## Cross-compiler

Set up a GCC [cross-compiler](../GLOSSARY/cross-compiler.md "A compiler that builds code for a different CPU/OS than the one it runs on") with Go enabled to get `i686-elf-gccgo`:

```bash
../gcc-x.y.z/configure --target=i686-elf --prefix="$PREFIX" \
    --disable-nls --enable-languages=c,c++,go --without-headers
```

This is the hard manual step (building a Go-enabled cross-compiler).

## Files
- `boot.s` — kernel entry point, sets up CPU environment
- `kernel.go` — your actual kernel routines
- `terminal.go` — package that prints text to the screen
- `linker.ld` — links the above

## Bootstrap Assembly (`boot.s`)

Same [Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002") header as C; then sets up a stack and calls `main`:

```nasm
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

.global _start
.type _start, @function
_start:
    mov $stack_top, %esp
    call main
    # Go runtime needs some stub symbols (see below)
    cli
    hlt
```

## Go runtime stubs

The Go runtime expects certain symbols. Just implement them as empty functions:

```nasm
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
```

## Terminal package (`terminal.go`)

```go
package terminal

// VGA text-mode buffer.
const (
    Width  = 80
    Height = 25
    Color  = 0x0F // white on black
    Screen = 0xB8000
)

func Init() {
    // clear screen
}

func Print(str string) {
    // write str to the VGA buffer
}
```

## Kernel (`kernel.go`)

```go
package kernel

import "terminal"

func Main() {
    terminal.Init()
    terminal.Print("Hello, Kernel World!\n")
}
```

## Linker script (`linker.ld`) and build

Same shape as the C Bare Bones [linker](../GLOSSARY/linker.md "Merges object files into one image at a chosen address") script (`. = 1M;`, `.text`, `.rodata`, `.data`, `.bss`).

```bash
i686-elf-as boot.s -o boot.o
i686-elf-gccgo -static -Werror -nostdlib -nostartfiles -nodefaultlibs -c kernel.go -o kernel.go.o
i686-elf-gcc -T linker.ld -o myos.bin -ffreestanding -O2 -nostdlib boot.o terminal.go.o kernel.go.o -lgcc
qemu-system-i386 -kernel myos.bin
```

---

## Key takeaways (beginner)
1. Go needs a **Go-enabled [cross-compiler](../GLOSSARY/cross-compiler.md "A compiler that builds code for a different CPU/OS than the one it runs on")** (`gccgo`) — that's the steepest part.
2. The **Go runtime expects stub symbols** (`__go_register_gc_roots`, `__go_runtime_error`) — provide empty ones.
3. You'll need your **own memory allocator** (sbrk) before Go can do much.
