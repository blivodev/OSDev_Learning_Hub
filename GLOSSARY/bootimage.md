<!-- Glossary page — bootimage. Grounded in OSDev_Learning_Hub docs. -->

# bootimage

> **[Back to glossary index](README.md)** · Category: Toolchain & build

`bootimage` is a Cargo subcommand (run as `cargo bootimage`) that invokes the `bootloader` crate to turn your Rust kernel ELF into a bootable disk image.

## The short version
Once you've built a freestanding Rust kernel with `cargo build --target x86_64-unknown-none`, `cargo bootimage --target x86_64-unknown-none` produces a BIOS-bootable `.bin` image in the target directory. You then boot that image in QEMU with `-drive format=raw`. It's the tool that makes the Rust kernel actually *boot*, and it needs a nightly toolchain loaded with the `rust-src` and `llvm-tools` components.

## Detailed explanation
Rust kernel development ships as two separate tools in this hub:

1. **The kernel build** (`cargo build`) is freestanding and verified on **stable**.
2. **The bootable image** (`cargo bootimage`) needs the **nightly** toolchain plus two components: `rust-src` (so the compiler can rebuild the core library for the bare-metal target) and `llvm-tools` (which provides the object tooling `bootimage` uses).

The exact setup from `Example_OS_Project/rust/README.md`:
```bash
rustup toolchain install nightly --component rust-src llvm-tools
cargo +nightly install bootimage
# then:
cargo bootimage --target x86_64-unknown-none
qemu-system-x86_64 -drive format=raw,file=target/x86_64-unknown-none/debug/bootimage-example_os_rust.bin
```

The output file is `bootimage-example_os_rust.bin` inside the target directory for the `x86_64-unknown-none` triple. The top-level `run-rust` Makefile target (`make run`) wires all of this together for you.

Unlike the C/C++/Go kernels — which are Multiboot ELFs booted with `qemu-system-i386 -kernel` — the bootimage output is a **raw disk image**, booted with `qemu-system-x86_64 -drive format=raw,file=...`. That's because the bootloader crate's boot protocol differs from Multiboot v1.

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/rust/Makefile` — the `run` target: `$(CARGO) bootimage --target $(TARGET)` then boots the produced `.bin`.
- `Example_OS_Project/rust/README.md` — full nightly setup + aliased `make run`.
- The root `Example_OS_Project/README.md` status matrix marks Rust bootable via *"install nightly + `cargo bootimage`, then `make run`"*.

## Watch / listen
- [Writing an OS in Rust — Bootimage](https://os.phil-opp.com/minimal-rust-kernel/) — free, the authoritative series using this tool
- [crates.io — bootimage](https://crates.io/crates/bootimage) — free

## Related terms
- [bootloader-crate](bootloader-crate.md)
- [cargo](cargo.md)
- [rustup](rustup.md)
- [QEMU](qemu.md)
- [ELF](elf.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
