# Panic Handler

> **[Back to glossary index](README.md)** · Category: Kernel & runtime

The panic handler is the `#[panic_handler]` function that runs when a Rust kernel panics — and since there is no OS to report the error to, the kernel must define this itself.

## The short version
In a normal Rust program, a panic is handled by the `std` runtime, which prints a message and unwinds the stack. A bare-metal kernel has **no panic runtime** — no `std`. So Rust requires you to provide a `#[panic_handler]`; without it, the compiler refuses to build. The minimal handler in this hub just halts forever.

## Detailed explanation
Whenever code hits a `panic!(...)` or an out-of-bounds slice access, control must go somewhere. On hosted Rust, `std` installs a default handler that formats the message and unwinds. A `no_std` kernel links only `core`, which has no operating system to print to or unwind through — so the `#[panic_handler]` becomes *mandatory*: the compiler will refuse to build without one somewhere in the crate graph.

The walkthrough (`synthesized_tutorials/02-rust/README.md`) states this directly and shows the minimal handler from `Example_OS_Project/rust/src/main.rs`:

```rust
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}
```

"It just halts forever — the minimal honest response when there's no OS to recover you." Note the `-> !` return type: a panic handler must *never return*, because if it did, execution would resume in an undefined state. In this hub the handler parks the CPU with the `hlt` instruction. A real kernel would grow this into printing the panic message and halting with a sensible error state, but the minimal kernel's job is just to stop safely.

The related `Cargo.toml` sets `panic = "abort"` for release builds: "no unwinding on bare metal." On freestanding targets there is no unwinder, so all panics are aborts that land in this handler.

## Why it matters here (OSDev_Learning_Hub)
`#[panic_handler]` is one of the three "friction points" the Rust chapter (`synthesized_tutorials/02-rust/README.md`) says map directly to a real OS-level concern. It lives in `Example_OS_Project/rust/src/main.rs`, alongside `#![no_std]` and `#![no_main]`, and is verified to build under `x86_64-unknown-none` on stable rustc 1.98.1. Conceptually it's the kernel's answer to: what happens on a fatal error when there's no OS to catch it?

## Watch / listen
- [Rust — `panic!` macro (std docs)](https://doc.rust-lang.org/std/macro.panic.html) — free official docs
- [Rust — PanicInfo (std docs)](https://doc.rust-lang.org/core/panic/struct.PanicInfo.html) — free official docs
- [Blog "Writing an OS in Rust" — A Freestanding Rust Binary](https://os.phil-opp.com/freestanding-rust-binary/) — free

## Related terms
- [`no_std`](no_std.md)
- [`no_main`](no_main.md)
- [`hlt` Instruction](hlt-instruction.md)
- [Interrupt](interrupt.md)
- [Freestanding](freestanding.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
