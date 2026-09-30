<!-- Glossary page — Cargo. Grounded in OSDev_Learning_Hub docs. -->

# Cargo

> **[Back to glossary index](README.md)** · Category: Toolchain & build

Cargo is Rust's package manager and build tool — the Rust analog of `make` + a dependency manager in one command.

## The short version
Rust kernels aren't built by invoking `rustc` by hand; you use Cargo. The Rust kernel in this hub is a *package* described by `Cargo.toml`, built with `cargo build --target x86_64-unknown-none`. Cargo handles compiling, fetching dependencies (like the `bootloader` crate), and running subcommands like `cargo bootimage`.

## Detailed explanation
Cargo reads a project's `Cargo.toml` to know the package name, its dependencies, and build profile settings. The hub's Rust kernel config (from `Example_OS_Project/rust/Cargo.toml`) shows key bare-metal details:

```toml
[package]
name = "example_os_rust"
edition = "2021"

[dependencies]

[profile.release]
panic = "abort"   # no unwinding on bare metal
```

The `panic = "abort"` is a bare-metal requirement: there's no unwinding runtime on a kernel. Because the kernel is `no_std`, there are **zero dependencies** — a deliberate choice to keep it lean.

Two supporting files drive Cargo's cross-compiling behavior:
- `.cargo/config.toml` contains `[build] target = "x86_64-unknown-none"` so Cargo defaults to the bare-metal target without you passing `--target` every time.
- `rust-toolchain.toml` pins `channel = "stable"` with `targets = ["x86_64-unknown-none"]` and `components = ["rust-src", "llvm-tools"]`.

The `cargo build` command compiles the kernel and produces an ELF (the "freestanding ELF" from the README). Subcommands extend Cargo: `cargo bootimage` isn't built-in — it's installed via `cargo install bootimage` and runs as a Cargo subcommand. The tool is powerful enough that the Rust "Makefile" is mostly a thin wrapper around Cargo: `make run` just runs `cargo build --target ...` and `cargo bootimage --target ...`.

```mermaid
flowchart LR
    T[Cargo.toml + config.toml] --> C[cargo build]
    C --> ELF[freestanding kernel ELF]
    ELF --> BI[cargo bootimage]
    BI --> IMG[bootable disk image]
```

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/rust/Cargo.toml` — package config with `panic = "abort"`.
- `Example_OS_Project/rust/.cargo/config.toml` — sets the default target to `x86_64-unknown-none`.
- `Example_OS_Project/rust/Makefile` — `CARGO ?= cargo`, wraps `cargo build` and `cargo bootimage`.
- `Example_OS_Project/rust/README.md` — `cargo build --target x86_64-unknown-none` documented as the verified stable step.

## Watch / listen
- [The Cargo Book — Official docs](https://doc.rust-lang.org/cargo/) — free, authoritative
- [Rust — Installing Rust with rustup](https://doc.rust-lang.org/book/ch01-01-installation.html) — free

## Related terms
- [rustup](rustup.md)
- [bootloader-crate](bootloader-crate.md)
- [bootimage](bootimage.md)
- [make](make.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
