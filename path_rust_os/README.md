# Path B — Rust → Operating System Development (Beginner)

The **most beginner-friendly, free Rust OS-dev track** we selected.

## Primary Resource

### Writing an OS in Rust — Philipp Oppermann (phil-opp)
- **Where:** https://os.phil-opp.com/ | https://github.com/phil-opp/blog_os
- **License:** Free; blog content CC-BY-NC, code Apache-2.0/MIT
- **Local copy:** [`blog_os/`](blog_os/) (full GitHub source, 144 markdown post sources under `blog/content/edition-2/`)
- **Why chosen:** *The* most famous free Rust OS-development series. Perfectly matches **Path B (Rust beginner → OS beginner)**. Text-heavy, diagram-rich, step-by-step. Covers `no_std` freestanding binaries, panic handler, bootloader + `bootimage` boot, VGA text buffer, interrupts, paging, heap allocation, and more.

## What you'll build in this path
- A freestanding Rust binary (`#![no_std]`) with a custom panic handler
- A minimal x86_64 kernel that prints to the VGA text buffer in QEMU
- Booted using the `bootloader` crate + `bootimage` (no cross-compiler needed — just Rust nightly)

## Supporting material already in this hub
- Fully-commented minimal implementation → [`Example_OS_Project/rust/`](../Example_OS_Project/rust/)
- Synthesized consolidated beginner guide → [`synthesized_tutorials/02-rust/`](../synthesized_tutorials/02-rust/)

## Toolchain needed (see `Example_OS_Project/docs/setup.md`)
`rustup` (nightly channel), `cargo`, `cargo bootimage`, `llvm-tools-preview` component, `qemu-system-x86_64`.
