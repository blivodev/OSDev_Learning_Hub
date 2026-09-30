# Rust kernel — build & run

A minimal `no_std` "Hello World!" kernel following the **Writing an OS in
Rust** series (os.phil-opp.com).

## Status
- ✅ **Kernel compiles** as a freestanding `no_std` binary (verified).
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
