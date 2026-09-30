# Path Go — Go → Operating System Development (Beginner)

An **free Go OS-dev track** (note: Go is not designed for OS dev, but it is learnable).

## Primary Resource

### OSDev Wiki — Go Bare Bones
- **Where:** https://wiki.osdev.org/Go_Bare_Bones
- **License:** Open wiki (community-reviewed)
- **Local copy:** [`Go_Bare_Bones.md`](Go_Bare_Bones.md)
- **Difficulty:** Medium (it's built on top of the C Bare Bones tutorial)
- **Why chosen:** The canonical free Go minimal-kernel tutorial. Uses an `i686-elf-gccgo` [cross-compiler](../GLOSSARY/cross-compiler.md "A compiler that builds code for a different CPU/OS than the one it runs on"). You implement Go-runtime stubs (e.g. `__go_register_gc_roots`, `__go_runtime_error`) as empty functions, then write `kernel.go` + `terminal.go` and link with a `linker.ld`.

### (Optional) Realistic frameworks for later
- **eggos** (https://github.com/alexflint/eggos) — a Go **unikernel** running on [x86](../GLOSSARY/x86.md "The CPU architecture family this hub targets") bare metal; an excellent advanced follow-up.
- **TamaGo** — the production framework for bare-metal Go.

## What you'll build in this path
A minimal Go kernel printing **"Hello, Kernel World!"** via the VGA text buffer, booted by [Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002").

## Supporting material already in this hub
- Fully-commented minimal implementation → [`Example_OS_Project/go/`](../Example_OS_Project/go/)
- Synthesized consolidated beginner guide → [`synthesized_tutorials/05-go/`](../synthesized_tutorials/05-go/)

## Toolchain needed (see `Example_OS_Project/docs/setup.md`)
`gccgo` (Go-enabled cross-compiler `i686-elf-gccgo` OR `x86_64-elf-gccgo`), `nasm`, `ld`, `make`, `qemu-system-x86_64`. Building the cross-compiler from source is the hard manual step.
