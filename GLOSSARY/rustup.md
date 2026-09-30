<!-- Glossary page — rustup. Grounded in OSDev_Learning_Hub docs. -->

# rustup

> **[Back to glossary index](README.md)** · Category: Toolchain & build

`rustup` is Rust's toolchain manager — it installs, switches, and pins Rust toolchains and their targets, which is essential for bare-metal cross-compilation.

## The short version
You're never just "using Rust" — you choose a *toolchain* (stable or nightly) and a *target* (which CPU/OS to compile for). `rustup` manages all of that. For the Rust kernel here you use `rustup target add x86_64-unknown-none` to enable the bare-metal target, and `rustup toolchain install nightly --component rust-src llvm-tools` to get the nightly toolchain the bootable-image step needs.

## Detailed explanation
A kernel compiles for a *bare-metal target* (`x86_64-unknown-none`) that has no operating system. That target doesn't ship with a default Rust install, so you add it:

```bash
rustup target add x86_64-unknown-none

# list installed targets / toolchains
rustup target list --installed
rustup toolchain list
```

The hub's Rust kernel introduces the **stable/nightly split**. The kernel itself builds on **stable** with the `x86_64-unknown-none` target. But producing a *bootable disk image* (via the `bootloader` crate / `cargo bootimage`) needs the **nightly** toolchain plus two components:

```bash
rustup toolchain install nightly --component rust-src llvm-tools
cargo +nightly install bootimage
```

- `rust-src` lets the compiler rebuild Rust's core library for the bare-metal target.
- `llvm-tools` provides the object tooling `bootimage` needs.

`rustup` also enforces project-specific toolchains via `rust-toolchain.toml`. The hub's file pins `stable`, the bare-metal target, and those two components:

```toml
[toolchain]
channel = "stable"
targets = ["x86_64-unknown-none"]
components = ["rust-src", "llvm-tools"]
```

When you're inside the `rust/` folder, `rustup` reads this file and uses the pinned channel automatically.

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/rust/rust-toolchain.toml` — pins stable + the bare-metal target + `rust-src`/`llvm-tools`.
- `Example_OS_Project/rust/README.md` — the `rustup target add` and `rustup toolchain install nightly` commands, and the stable-vs-nightly split.
- `Example_OS_Project/rust/.cargo/config.toml` — sets the default build target.
- `Example_OS_Project/rust/Makefile` — wraps the rustup-driven cargo commands as `make run`.

## Watch / listen
- [rustup — Official book](https://rust-lang.github.io/rustup/) — free, authoritative
- [Rust — Installing Rust with rustup (The Rust Book)](https://doc.rust-lang.org/book/ch01-01-installation.html) — free

## Related terms
- [cargo](cargo.md)
- [bootloader-crate](bootloader-crate.md)
- [bootimage](bootimage.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
