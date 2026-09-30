# Rust kernel — build & run

A minimal `no_std` "Hello World!" [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") following the **Writing an OS in
Rust** series (os.phil-opp.com).

## Status
- ✅ **Kernel compiles** as a [freestanding](../../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists") `no_std` binary (verified).
- 🔧 **Bootable image**: produced with the `bootloader` crate, which needs a
  **nightly** toolchain + `cargo bootimage` (see below). The kernel source
  is complete; only the bootable-image assembly tool is nightly-only.

## Build the kernel (stable, verified)
```bash
rustup target add x86_64-unknown-none
cargo build --target x86_64-unknown-none
# ⟹ target/x86_64-unknown-none/debug/example_os_rust  (freestanding ELF)
```

## Make a bootable image & run in QEMU (needs nightly)
```bash
# once:
rustup toolchain install nightly --component rust-src llvm-tools
cargo +nightly install bootimage

# then:
cargo bootimage --target x86_64-unknown-none
qemu-system-x86_64 -drive format=raw,file=target/x86_64-unknown-none/debug/bootimage-example_os_rust.bin
```
Aliased as `make run` in this folder.

## How the kernel is structured
```
rust/
├── src/main.rs          # the whole kernel: no_std, _start, VGA driver, panic handler
├── Cargo.toml
├── rust-toolchain.toml  # pins stable + the bare-metal target
├── .cargo/config.toml   # default-build target = x86_64-unknown-none
└── Makefile
```

## Key Rust-for-bare-metal concepts this kernel shows
| Concept | How it's done here |
|---------|--------------------|
| No standard library | `#![no_std]` |
| No normal `main()` | `#![no_main]`, custom entry `_start` |
| No panic runtime | `#[panic_handler]` that `hlt`s |
| Writing to the screen | raw pointer write to `0xB8000` inside `unsafe {}` |
| Never returning | `_start -> !` loops forever |


## Watch and learn

Videos matched to this `no_std` Rust kernel and the Writing an OS in Rust series it follows.

- [Writing an OS in Rust - Part 1 - A Freestanding Rust Binary](https://www.youtube.com/watch?v=rH5jnbJ3tL4) — the exact blog this kernel follows, video-walked: a freestanding `no_std` Rust binary.
- [Writing an OS in Rust - Part 4 - Testing](https://www.youtube.com/watch?v=zTzwgKac8kA) — continues the series with testing, handy once your kernel compiles.
- [Write Your Own 64-bit Operating System Kernel #1 - Boot code and multiboot header](https://www.youtube.com/watch?v=FkrpUaGThTQ) — an alternative hands-on kernel series to see the same boot concepts in another language.
- [Write Your Own 64-bit Operating System Kernel #2 - Stack, long mode and printing using C code](https://www.youtube.com/watch?v=wz9CZBeXR6U) — printing to screen from a bare-metal kernel, the low-level sibling of this Rust VGA driver.
