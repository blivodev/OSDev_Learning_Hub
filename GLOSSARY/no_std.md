# `no_std`

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

`#![no_std]` is a Rust crate-level attribute that disables the standard library so the code can run on bare metal with no operating system.

## The short version
Rust's standard library (`std`) assumes an OS is beneath it: it uses a `syscall` layer, allocates via a process heap, and spawns threads. A kernel *is* the OS, so it can't use `std`. `#![no_std]` says "link only `core`" — the pure-language pieces with no OS dependency. Every bare-metal Rust crate in this hub starts with it.

## Detailed explanation
The Rust walkthrough (`synthesized_tutorials/02-rust/README.md`) is explicit about what `std` needs that a kernel doesn't have:

> `#![no_std]` — the Rust *standard library* (`std`) assumes an operating system underneath it: it talks to a `syscall` layer, allocates via the process heap, spawns threads. A kernel is the OS, so it links only against the Rust **`core`** library (the pieces that are pure language, no OS).

Concretely, `std` pulls in things like `Vec`, `String`, and `Box` backed by an allocator and OS memory calls, plus OS I/O and thread primitives. `core` has no such dependencies. With `no_std` you lose those conveniences unless you bring your own [memory allocator](heap-allocation.md) — but you also stop assuming an OS, which is the correct posture for a kernel. The very first two lines of `Example_OS_Project/rust/src/main.rs` are:

```rust
#![no_std]          // do NOT link the standard library
#![no_main]         // do NOT use the normal Rust main() runtime
```

When you disable `std`, you must also satisfy whatever the compiler can no longer assume: a `#[panic_handler]` becomes mandatory (there's no `std` panic runtime), and your entry point must be provided yourself. The hub builds this against the bare-metal target `x86_64-unknown-none`, pinned in `rust-toolchain.toml` and confirmed to `cargo build` cleanly on stable rustc 1.98.1.

## Why it matters here (OSDev_Learning_Hub)
`no_std` is the Rust expression of "freestanding," and the whole Rust kernel in `Example_OS_Project/rust/src/main.rs` hangs on it. The tutorial `synthesized_tutorials/02-rust/README.md` calls the three attributes (`no_std`, `no_main`, `#[panic_handler]`) the friction points that "map directly to a real OS-level concern," and notes that `no_std`/`no_main` are your first encounter with **what a runtime is and what it assumes**, bridging to bootloaders and direct hardware I/O.

## Watch / listen
[- Writing an OS in Rust - Part 1 - A Freestanding Rust Binary - Uncle Scientist](https://www.youtube.com/watch?v=rH5jnbJ3tL4) — disabling std for bare-metal code
- [Rust — `std` vs `core` (official crate docs)](https://doc.rust-lang.org/core/) — free official docs
- [Rust — The `no_std` guide (official docs)](https://doc.rust-lang.org/1.64.0/reference/names/crates.html) — free official docs
- [Blog "Writing an OS in Rust" — A Freestanding Rust Binary](https://os.phil-opp.com/freestanding-rust-binary/) — free

## Related terms
- [`no_main`](no_main.md)
- [Freestanding](freestanding.md)
- [Panic Handler](panic-handler.md)
- [Heap Allocation](heap-allocation.md)
- [Hosted](hosted.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
