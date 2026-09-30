# Chapter 02 — Building "Hello World!" in Rust

*Original content written for OSDev_Learning_Hub — walks through the real,
verified code in `Example_OS_Project/rust/`.*

## What you'll have at the end
A [freestanding](../../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists") Rust [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") that prints:
```
Hello World!
Welcome to your very own operating system (Rust edition).
```
Rust is different from C in how it *restricts* you. There is no `#define`
macro and no raw global pointer you can poke freely — the language forces you
to say `#![no_std]`, `#![no_main]`, write a `#[panic_handler]`, and wrap every
write to `0xB8000` in an `unsafe {}` block. Each of those friction points maps
directly to a real OS-level concern, so this chapter is as much about *what
Rust makes explicit* as about the kernel itself.

## The flow, in one picture

```mermaid
flowchart LR
    A[cargo build<br/>--target x86_64-unknown-none] --> B[#![no_std]<br/>no stdlib linked]
    B --> C[#![no_main]<br/>no Rust runtime]
    C --> D["#[no_mangle] pub extern \"C\" fn _start() -> !"]
    D --> E[unsafe write to 0xB8000]
    E --> F[loop  hlt]
    F --> G["#[panic_handler]<br/>halts on error"]
```
The stable build targets a bare-metal CPU. Making a *bootable* disk image is a
separate step (needs nightly + `cargo bootimage`) — shown at the end.

## Step 1 — `no_std`, `no_main`: refusing the two runtimes

The top of `rust/src/main.rs`:

```rust
#![no_std]          // do NOT link the standard library
#![no_main]         // do NOT use the normal Rust main() runtime
```

- **`#![no_std]`** — the Rust *standard library* (`std`) assumes an operating
  system underneath it: it talks to a `syscall` layer, allocates via the
  process heap, spawns threads. A kernel is the OS, so it links only against
  the Rust **`core`** library (the pieces that are pure language, no OS).
- **`#![no_main]`** — the normal `fn main()` entry point is wrapped by a
  runtime that calls a C `main`, which your kernel neither has nor wants. With
  `no_main` you throw that away and provide `_start` yourself.

## Step 2 — The entry point: `extern "C" fn _start() -> !`

```rust
#[no_mangle]
pub extern "C" fn _start() -> ! {
    vga_write("Hello World!\n");
    vga_write("Welcome to your very own operating system (Rust edition).\n");
    loop {
        // A kernel never returns. `hlt` parks the CPU to save power;
        // interrupts (added in later chapters) wake it up again.
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}
```

Three attributes do the heavy lifting:

- **`#[no_mangle]`** — like C++'s `extern "C"`, stops the compiler from name
  mangling `_start` into a symbol the bootloader can't find. The exported name
  is exactly `_start`.
- **`pub extern "C"`** — C ABI, so the bootloader's jump into our code works.
- **`-> !`** — the **never type**: Rust is told this function *never returns*.
  That's honest — it's a kernel, there is no caller below it. The compiler
  then lets us write an infinite `loop` and knows no code "after" the call
  can exist.

`hlt` parks the CPU in a low-power state instead of a busy spin — but with
interrupts still disabled at this stage it acts as a pause until something
(resumable in later chapters) wakes the CPU.

## Step 3 — Writing to 0xB8000: `unsafe` and the panic handler

Rust's memory safety rules don't allow "just writing to a magic address", so
the write is an explicit `unsafe` block with a safety comment:

```rust
const VGA_BUFFER: *mut u16 = 0xB8000 as *mut u16;   // the framebuffer
const COLOR_WHITE_ON_BLACK: u16 = 0x0F;              // fg=white, bg=black
...
let index = row * VGA_WIDTH + col;
// Safety: 0xB8000 is the valid, always-mapped VGA text framebuffer.
unsafe {
    *VGA_BUFFER.add(index) = (COLOR_WHITE_ON_BLACK << 8) | c as u16;
}
```

The cell layout is identical to C's — `[color<<8 | char]` — because it's the
same hardware. What differs is that Rust makes you prove, in a comment, *why*
touching this raw pointer is safe.

Because a kernel has **no panic runtime** (no `std` to print a backtrace or
unwind), the `#[panic_handler]` is mandatory — the compiler will refuse to
build without a `#[panic_handler]` attribute somewhere:

```rust
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}
```

It just halts forever — the minimal honest response when there's no OS to
recover you.

## Step 4 — `Cargo.toml` and `rust-toolchain.toml`

Nothing is a dependency — this kernel links only `core`:

```toml
[dependencies]

[profile.release]
panic = "abort"   # no unwinding on bare metal
```

And the toolchain pins the built-in bare-metal target:

```toml
[toolchain]
channel = "stable"
targets = ["x86_64-unknown-none"]
components = ["rust-src", "llvm-tools"]
```

`.cargo/config.toml` just sets the default target so `cargo build` needs no
`--target` flag:

```toml
[build]
target = "x86_64-unknown-none"
```

## Step 5 — Build the kernel, then make it boot

The `rust/Makefile` splits this in two:

```make
all:  cargo build --target x86_64-unknown-none   # kernel only (stable)

run:  cargo bootimage --target x86_64-unknown-none
      qemu-system-x86_64 -drive format=raw,file=target/x86_64-unknown-none/debug/bootimage-example_os_rust.bin
```

1. **`cargo build`** produces the freestanding [ELF](../../GLOSSARY/elf.md "The executable format that lets a bootloader load your kernel") — **verified on stable**
   Rust. This is your kernel.
2. **A bootable image** needs more: `cargo bootimage` bundles your ELF with
   the `bootloader` crate into a BIOS-bootable raw disk, and that crate
   currently requires a **nightly** toolchain. That's a documented limitation,
   not a bug: the *kernel* is perfectly buildable on stable; only the
   image-packaging step needs nightly.

## Verification

What was actually verified for this language:

- `cargo build --target x86_64-unknown-none` **succeeded on stable rustc
  1.98.1** with **zero errors** — `Finished dev profile, 0.19s`. The
  `x86_64-unknown-none` freestanding kernel ELF (`target/.../example_os_rust`)
  was produced.
- The **bootable-image** step (`cargo bootimage` + `make run`) was confirmed to
  need nightly + the `bootloader` crate per the toolchain config and Makefile —
  a documented limitation, so the kernel-level build is the verified
  deliverable.
- The `_start` symbol is exported unmangled as `_start` (the `#[no_mangle]`
  guarantee), with `-> !` letting the loop be written honestly.

> **Bridge to OS concepts:** Rust's `no_std`/`no_main` are your first real
> **what a runtime is and what it assumes** — a bridge to
> [bootloaders](../../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") and how a kernel is entered (concepts/01) and to **direct
> hardware I/O** via the [VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") (concepts/04). The `unsafe` raw
> pointer, the never-returning `_start`, and the panic handler are Rust
> spelling out the very rules C lets you swallow silently.

---

## Watch and learn

<details class="video-embed">
<summary>▶ Watch: Writing an OS in Rust - Part 1 - A Freestanding Rust Binary</summary>
<iframe src="https://www.youtube-nocookie.com/embed/rH5jnbJ3tL4" title="Writing an OS in Rust - Part 1 - A Freestanding Rust Binary" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>A video walkthrough of Philipp Oppermann's blog series, staring with the very `#![no_std] #![no_main]` freestanding binary you just built in this chapter.</p>
</details>
- [Rust OS - playlist](https://www.youtube.com/playlist?list=PLib6-zlkjfXkdCjQgrZhmfJOWBk_C2FTY) — The full video series through the "Writing an OS in Rust" posts, from the freestanding binary and minimal kernel onward, so you can follow the `unsafe` `0xB8000` write and `_start` entry point visually.
<details class="video-embed">
<summary>▶ Watch: Rust: What is Ownership and Borrowing?</summary>
<iframe src="https://www.youtube-nocookie.com/embed/79phqVpE7cU" title="Rust: What is Ownership and Borrowing?" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>The core ownership rules explained — move vs clone, references, and the borrow checker — which is exactly why Rust makes you write `unsafe` around a raw pointer to the framebuffer.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: Understanding Ownership in Rust</summary>
<iframe src="https://www.youtube-nocookie.com/embed/VFIOSWy93H0" title="Understanding Ownership in Rust" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>A clear deep-dive into the three ownership rules and how moves, clones, and references interact with the stack and heap — the memory model behind a language with no garbage collector.</p>
</details>
