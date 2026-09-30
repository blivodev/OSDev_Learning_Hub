# Path B — Rust → Operating System Development (Beginner)

The **most beginner-friendly, free Rust OS-dev track** we selected.

## Primary Resource

### Writing an OS in Rust — Philipp Oppermann (phil-opp)
- **Where:** https://os.phil-opp.com/ | https://github.com/phil-opp/blog_os
- **License:** Free; blog content CC-BY-NC, code Apache-2.0/MIT
- **Local copy:** [`blog_os/`](blog_os/) (full GitHub source, 144 markdown post sources under `blog/content/edition-2/`)
- **Why chosen:** *The* most famous free Rust OS-development series. Perfectly matches **Path B (Rust beginner → OS beginner)**. Text-heavy, diagram-rich, step-by-step. Covers `no_std` [freestanding](../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists") binaries, [panic handler](../GLOSSARY/panic-handler.md "The function that runs when a Rust kernel panics (no OS to report to)"), [bootloader](../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") + `bootimage` boot, VGA text buffer, [interrupts](../GLOSSARY/interrupt.md "A hardware signal that makes the CPU run a registered handler"), [paging](../GLOSSARY/paging.md "Translates virtual addresses to physical RAM via page tables"), [heap allocation](../GLOSSARY/heap-allocation.md "Dynamically allocating memory at runtime; a kernel does it itself"), and more.

## What you'll build in this path
- A freestanding Rust binary (`#![no_std]`) with a custom panic handler
- A minimal x86_64 [kernel](../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") that prints to the VGA text buffer in [QEMU](../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing")
- Booted using the `bootloader` crate + `bootimage` (no cross-compiler needed — just Rust nightly)

## Supporting material already in this hub
- Fully-commented minimal implementation → [`Example_OS_Project/rust/`](../Example_OS_Project/rust/)
- Synthesized consolidated beginner guide → [`synthesized_tutorials/02-rust/`](../synthesized_tutorials/02-rust/)

## Toolchain needed (see `Example_OS_Project/docs/setup.md`)
`rustup` (nightly channel), `cargo`, `cargo bootimage`, `llvm-tools-preview` component, `qemu-system-x86_64`.
