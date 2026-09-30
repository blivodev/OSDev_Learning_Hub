# `no_main`

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

`#![no_main]` is a Rust crate-level attribute that disables the normal `main()` runtime so you can provide your own kernel entry point.

## The short version
A normal Rust program's `fn main()` is wrapped by a runtime that sets up the environment and eventually calls a C `main`. A kernel neither has nor wants that runtime, so `#![no_main]` throws it away and lets you define the entry symbol (`_start`) yourself. It's the Rust half of "freestanding," paired with `#![no_std]`.

## Detailed explanation
The Rust tutorial explains why `main` is unusable in a kernel:

> `#![no_main]` — the normal `fn main()` entry point is wrapped by a runtime that calls a C `main`, which your kernel neither has nor wants. With `no_main` you throw that away and provide `_start` yourself.

When you disable the `main` runtime, the compiler no longer expects a `fn main`. Instead you declare the real entry point the bootloader will jump to. In `Example_OS_Project/rust/src/main.rs` that is:

```rust
#[no_mangle]
pub extern "C" fn _start() -> ! {
    vga_write("Hello World!\n");
    vga_write("Welcome to your very own operating system (Rust edition).\n");
    loop {
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}
```

The three attributes here matter: `#[no_mangle]` stops the compiler from mangling `_start` (so the bootloader can find the exact symbol); `extern "C"` gives it C ABI so the bootloader's jump works; and `-> !` (the never type) tells Rust this function never returns — honest, because there is no caller below a kernel. Without `#![no_main]` the compiler would assume you have the standard `main` runtime, which would drag in OS dependencies and a mangled, non-`_start` entry — precisely what a bare-metal kernel must avoid.

## Why it matters here (OSDev_Learning_Hub)
`no_main` sits right next to `no_std` at the top of `Example_OS_Project/rust/src/main.rs` and is walked through step-by-step in `synthesized_tutorials/02-rust/README.md` (Step 2, "The entry point"). It's also the Rust mirror of the linker's `ENTRY(_start)` directive and the C stub in `boot.s` that jumps into `_start`/`main` — see `synthesized_tutorials/00-introduction/02-your-toolchain.md` where every language's entry story begins in assembly.

## Watch / listen
[- Writing an OS in Rust - Part 1 - A Freestanding Rust Binary - Uncle Scientist](https://www.youtube.com/watch?v=rH5jnbJ3tL4) — a freestanding binary with no main entry
- [Rust — `no_mangle` (Reference, official)](https://doc.rust-lang.org/reference/abi.html#the-mangle-attribute) — free official docs
- [Blog "Writing an OS in Rust" — A Freestanding Rust Binary](https://os.phil-opp.com/freestanding-rust-binary/) — free
- [OSDev Wiki — Boot Sequence](https://wiki.osdev.org/Boot_Sequence) — free, authoritative

## Related terms
- [`no_std`](no_std.md)
- [Entry Point](entry-point.md)
- [Freestanding](freestanding.md)
- [Panic Handler](panic-handler.md)
- [Assembly / Assembler](assembler.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
