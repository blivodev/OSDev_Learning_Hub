# Go kernel — build & run

The Go [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") cannot be built with the **standard** `go build` toolchain —
Go's runtime was not designed for bare metal. It requires a **Go-enabled
[cross-compiler](../../GLOSSARY/cross-compiler.md "A compiler that builds code for a different CPU/OS than the one it runs on")** (`i686-elf-gccgo`), built from GCC source.

## Why the cross-compiler is unavoidable
The OSDev "Go Bare Bones" tutorial's key insight: standard Go links a full
runtime (GC, goroutines, `runtime` package) that needs an OS. A [freestanding](../../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists")
kernel uses `gccgo` with `-nostdlib` and **disables that runtime**, providing
only the empty stub symbols (`__go_register_gc_roots`, `__go_runtime_error`)
that the toolchain still expects — see `boot.s`.

## Build (once you have i686-elf-gccgo)
```bash
# 1. Assemble the bootstrap (this also defines the Go-runtime stubs)
as --32 boot.s -o boot.o

# 2. Compile the two Go packages with gccgo (freestanding)
i686-elf-gccgo -static -Werror -nostdlib -nostartfiles -nodefaultlibs \
    -c terminal/terminal.go -o terminal.go.o
i686-elf-gccgo -static -Werror -nostdlib -nostartfiles -nodefaultlibs \
    -c kernel.go -o kernel.go.o

# 3. Link into a Multiboot kernel at 1 MiB
i686-elf-gcc -T linker.ld -o kernel.bin -ffreestanding -O2 -nostdlib \
    boot.o kernel.go.o terminal.go.o -lgcc

# 4. Boot it
qemu-system-i386 -kernel kernel.bin
```

## Building the cross-compiler (Ubuntu/Debian)
```bash
# Prerequisites
sudo apt install build-essential bison flex libgmp-dev libmpfr-dev \
                 libmpc-dev texinfo nasm qemu-system-x86

# Download + build i686-elf binutils and gcc WITH go enabled
export PREFIX="$HOME/opt/cross"
export TARGET=i686-elf
export PATH="$PREFIX/bin:$PATH"

# binutils
wget https://ftp.gnu.org/gnu/binutils/binutils-2.41.tar.xz
tar xf binutils-2.41.tar.xz && cd binutils-2.41
mkdir build && cd build
../configure --target=$TARGET --prefix="$PREFIX" --with-sysroot \
             --disable-nls --disable-werror
make -j$(nproc) && make install

# gcc (enable go!)
cd ../..
wget https://ftp.gnu.org/gnu/gcc/gcc-13.2.0/gcc-13.2.0.tar.xz
tar xf gcc-13.2.0.tar.xz && cd gcc-13.2.0
mkdir build && cd build
../configure --target=$TARGET --prefix="$PREFIX" --disable-nls \
             --enable-languages=c,c++,go --without-headers
make -j$(nproc) all-gcc && make install-gcc
```

> **Simpler alternative:** use **eggos** (https://github.com/alexflint/eggos),
> a Go *unikernel* that runs normal Go apps on bare metal, for when you
> outgrow this hand-rolled stub. For learning the low-level details, this
> `boot.s` + `kernel.go` + `terminal.go` stub is the right start.


## Watch and learn

Videos matched to writing and booting a kernel in Go (and why it needs a cross-compiled runtime).

- [GopherCon 2025: An Operating System in Go - Patricio Whittingslow](https://www.youtube.com/watch?v=SvsdVe1kgSU) — a live talk on building an OS in Go, the systems-programming question this folder explores.
- [Can I Build an Operating System in Go?](https://www.youtube.com/watch?v=uotfXZDLAEA) — a practical look at the feasibility (and hurdles) of a Go kernel.
- [Write Your Own 64-bit Operating System Kernel #1 - Boot code and multiboot header](https://www.youtube.com/watch?v=FkrpUaGThTQ) — the bare-metal boot target (Multiboot + QEMU) this Go stub ultimately produces, in a C walkthrough.
- [How does an OS boot? //Source Dive// 001](https://www.youtube.com/watch?v=KkenLT8S9Hs) — the boot sequence your `boot.s` engages on hardware.
