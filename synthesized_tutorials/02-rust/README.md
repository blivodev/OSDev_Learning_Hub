# Chapter 02 — Building "Hello World!" in Rust

*Original content written for OSDev_Learning_Hub — walks through the real,
verified code in `Example_OS_Project/rust/`.*

> **Read this after Chapter 01 (C).** The C chapter gave you the raw mental
> model: Multiboot header, a stack, a VGA cell of `[color<<8|char]`, the
> `for(;;)` "never return" discipline. Rust *reimplements all of that* while
> adding a layer the C kernel never had: **the compiler policing your memory
> safety**. Where C lets you poke `0xB8000` freely, Rust makes you say
> `unsafe`. That friction is the whole point of this chapter.

---

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

---

## Part A — Rust fundamentals you actually need

Rust is a big language, but the 97-line `main.rs` in this project uses only a
focused slice. Before we read the kernel, let's build the three concepts the
rest of the chapter leans on: **ownership**, **`unsafe`**, and **the ternary
world of `no_std`**.

### A.1 — Ownership: why there is no garbage collector (and no free)

Rust manages memory with **ownership** rather than a garbage collector. Three
rules cover everything:

```rust
// Rule 1: Every value has ONE owner.
let s = String::from("hello");   // 's' owns this String

// Rule 2: Ownership can MOVE (not shallow-copy) to a new owner.
let t = s;                        // 's' is now dead — its value moved to 't'
// println!("{s}");               // ERROR: borrow of moved value

// Rule 3: When the owner goes out of scope, the value is dropped (freed)
//         automatically. No free(), no GC, no leaks — by construction.
```

Compare this with C: in C *you* are the owner and *you* must `free()` manually,
or leak. In Go, the runtime's garbage collector owns and reclaims. In Rust,
the **compiler** tracks ownership at compile time, so memory is freed exactly
when its owner dies — with zero runtime overhead. That's why Rust can do
bare-metal (no GC to stub out) *and* be memory-safe.

Why does this matter for your kernel? Because the classic kernel bug is a
**use-after-free**: you release a page of memory that something still points
at, then an attacker (or a stray driver) reads or writes through the dangling
pointer. Rust's ownership model makes that class of bug a *compile error* in
safe code. The only way to even attempt it is inside `unsafe` — and that's
precisely where the kernel's `0xB8000` write lives.

### A.2 — `unsafe`: the escape hatch that makes bare metal possible

Rust's safety guarantees only apply in **safe** code. Raw pointers, hardware
registers, and dereferencing a magic address are all *outside* those
guarantees, so they require `unsafe`. The keyword is not "scary" — it is an
**audit trail**:

```rust
// Safe Rust: the borrow checker verifies everything you touch is valid.
let cells: &[u16] = &[0x0F48, 0x0F65];       // reads 2 valid, owned u16s

// Unsafe Rust: you are telling the compiler "trust me, this is a valid
// memory address and I know what lives there."
const VGA_BUFFER: *mut u16 = 0xB8000 as *mut u16;   // a raw pointer
unsafe {
    *VGA_BUFFER = 0x0F48;   // you must be RIGHT about 0xB8000 yourself
}
```

Every `unsafe` block is a promise the language itself cannot verify. Good Rust
kernels put a **safety comment** right above each one explaining *why* it's
safe:

```rust
// Safety: 0xB8000 is the valid, always-mapped VGA text framebuffer.
unsafe { *VGA_BUFFER.add(index) = cell; }
```

The C kernel could poke `0xB8000` with no ceremony whatsoever. Rust's version
forces you to type `unsafe` and justify it. Both compile to the same machine
code — but the Rust version leaves a *written contract* of why that memory is
valid. That's the OSDev value of Rust: it turns every hardware assumption into
a documented checkpoint.

### A.3 — `no_std` vs `std`: two worlds, one compiler

Your normal Rust programs get the **standard library** (`std`) — `Vec`,
`String`, `HashMap`, and crucially an *operating system underneath* that
provides allocation, file I/O, and threads. A kernel **is** the OS, so it must
run with `#![no_std]` — meaning it can use only the `core` library (pure
language primitives that don't need an OS) and **nothing** that requires
allocation or syscalls.

```rust
// What you lose with #![no_std]:
//   Vec, String, Box, HashMap  →  need an allocator (OS provides it)
//   println! macro             →  needs std::io
//   std::thread                →  needs an OS scheduler
//
// What #![no_std] keeps:
//   primitives, slices, iterators, raw pointers, core::arch (asm!)
//   Result/Option, traits, closures
```

For this kernel we use almost nothing from `core` — just `core::panic::PanicInfo`
and `core::arch::asm!` for the `hlt` instruction. That's how lean a "Hello
World" kernel is.

---

## The flow, in one picture

```mermaid
flowchart LR
    subgraph build["cargo build --target x86_64-unknown-none"]
        A["cargo build<br/>--target x86_64-unknown-none"] --> B["#![no_std]<br/>no stdlib linked"]
        B --> C["#![no_main]<br/>no Rust runtime"]
    end
    C --> D["#[no_mangle] pub extern \"C\" fn _start() -> !"]
    D --> E["unsafe write to 0xB8000"]
    E --> F["loop { asm!(\"hlt\") }"]
    F --> G["#[panic_handler]<br/>halts on error"]
    G --> H["tree rust → (stable) kernel ELF + (nightly) bootimage"]
```
The stable build targets a bare-metal CPU. Making a *bootable* disk image is a
separate step (needs nightly + `cargo bootimage`) — shown at the end.

---

## Part B — Reading the real `Example_OS_Project/rust/src/main.rs`

Here is the *actual* file, with a line-by-line story. It is only 97 lines.

```rust
#![no_std]          // do NOT link the standard library
#![no_main]         // do NOT use the normal Rust main() runtime

use core::panic::PanicInfo;

// ---- VGA text-mode driver -------------------------------------------
const VGA_WIDTH: usize = 80;
const VGA_HEIGHT: usize = 25;
const VGA_BUFFER: *mut u16 = 0xB8000 as *mut u16;   // the framebuffer
const COLOR_WHITE_ON_BLACK: u16 = 0x0F;              // fg=white, bg=black

static mut CURSOR_ROW: usize = 0;
static mut CURSOR_COL: usize = 0;

fn vga_putchar(c: u8) {
    if c == b'\n' { /* newline handling, wrap */ return; }
    let row = unsafe { CURSOR_ROW };
    let col = unsafe { CURSOR_COL };
    let index = row * VGA_WIDTH + col;
    // Safety: 0xB8000 is the valid, always-mapped VGA text framebuffer.
    unsafe {
        *VGA_BUFFER.add(index) = (COLOR_WHITE_ON_BLACK << 8) | c as u16;
    }
    unsafe { /* advance cursor, wrap at end of row */ }
}

fn vga_write(s: &str) {
    for byte in s.bytes() { vga_putchar(byte); }
}

// ---- Kernel entry point ---------------------------------------------
#[no_mangle]
pub extern "C" fn _start() -> ! {
    vga_write("Hello World!\n");
    vga_write("Welcome to your very own operating system (Rust edition).\n");
    loop {
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}

// ---- Panic handler --------------------------------------------------
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop { unsafe { core::arch::asm!("hlt", options(nomem, nostack)) } }
}
```

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

Think of these as the Rust equivalent of C's `-ffreestanding -nostdlib`: both
are "do not assume an OS exists." C expresses it as a compiler flag; Rust
expresses it as crate-level attributes that are part of the source itself.

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

**Why `-> !` matters technically:** in C, `kernel_main` returning is *defined
but wrong* — the assembler catches you with `.Lhang`. In Rust, `_start -> !`
makes returning a *type error* — the function simply cannot return and the
compiler knows it. Rust moves the "never return" discipline from a runtime
safety net into the type system. That's a small but real safety win.

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

**Why is the panic handler *required*?** `core` can panic (a slice index out of
bounds, an unwrap on `None`, an overflow in a debug build). In a hosted Rust
program, `std` installs a default that unwinds and prints. With `#![no_std]`
there is no default — so the compiler demands *you* provide one. This is Rust
making explicit something C never even mentions: "what happens when a normal
C function hits an impossible state?" In C the answer is "undefined behavior /
whatever the hardware does." In Rust, the answer is "your `#[panic_handler]`
decides."

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

### Why `panic = "abort"`?

In `std` Rust, a panic *unwinds* the stack — running destructors as it goes —
which requires landing-pad metadata and runtime support. A bare-metal kernel
has no unwind runtime (just like C++ with `-fno-exceptions`), so `panic =
"abort"` tells the compiler that a panic should **abort** (jump straight to
your `#[panic_handler]`) instead of unwinding. This removes the unwinding
runtime entirely. It's Rust's analogue of C++'s `-fno-exceptions`.

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

### Stable vs. nightly, honestly explained

- The freestanding **kernel** (`x86_64-unknown-none`) needs nothing unstable —
  `#[no_std]`, `#[no_main]`, the panic handler, and `core::arch::asm!` all
  work on stable. **This is your verified deliverable.**
- The **bootable image** merges `bootloader` (a boot disk-writing crate) into
  your kernel. That packaging step currently wants nightly. So "I built the
  kernel" (stable ✔) and "I made a bootable USB" (needs nightly) are *different
  claims* — this project verifies the first completely and documents the
  second's requirement honestly.

---

## Part C — A guided walkthrough tied to the code

### C.1 — Build the kernel exactly as verified

```bash
# Inside Example_OS_Project/rust:
rustup target add x86_64-unknown-none   # once
cargo build --target x86_64-unknown-none
```

On a stable toolchain (this project verified rustc 1.98.1) this succeeds with
**zero errors** in ~0.19s and produces
`target/x86_64-unknown-none/debug/example_os_rust`. That ELF is your kernel.

### C.2 — Inspect the produced ELF

```bash
file target/x86_64-unknown-none/debug/example_os_rust
# => ELF 64-bit LSB executable, x86-64, statically linked, not stripped

nm target/x86_64-unknown-none/debug/example_os_rust | grep _start
# => 0000000000000000 T _start        ← unmangled, symbol 'T' (text)
```

The `nm` grep of `_start` is the *proof* of `#[no_mangle]`: the bootloader
needs a plain `_start`, and there it is, exported under its unmangled name.

### C.3 — Read the kernel's segment layout

```bash
readelf -l target/x86_64-unknown-none/debug/example_os_rust
```

You'll see a single `LOAD` segment — a minimal flat binary. That's what the
`bootloader` crate will wrap into a bootable image. There's no libc to drag
in, no .interp, no dynamic sections — exactly what a freestanding kernel
should look like.

### C.4 — Make it actually boot (nightly step)

```bash
# Requires a nightly toolchain for the bootloader crate:
cargo bootimage --target x86_64-unknown-none
qemu-system-x86_64 -drive format=raw,file=target/x86_64-unknown-none/debug/bootimage-example_os_rust.bin
```

The bootimage crate prepends a minimal BIOS bootloader to your ELF and packs
them into a raw disk image QEMU can boot. When it works, you'll see:

```
Hello World!
Welcome to your very own operating system (Rust edition).
```

### C.5 — Exercise: make your kernel panic *on purpose*

The cleanest way to *see* your `#[panic_handler]` fire is to trigger a panic
and watch nothing-but-halt happen:

```rust
#[no_mangle]
pub extern "C" fn _start() -> ! {
    vga_write("Hello World!\n");
    // Trigger the panic path deliberately:
    panic!("intentional panic — watch the screen freeze");
    // if it boots with the bootimage; otherwise this halts via panic handler
}
```

If you build with a stable target only, `panic!` still reaches your
`#[panic_handler]`, which halts. Try it — a kernel where you *control* the
panic behavior is safer than one where a panic is undefined behavior.

---

## Part D — Pitfalls, warnings, and the Rust-specific traps

These are the mistakes learners make on *this exact* Rust kernel:

1. **Forgetting `#![no_mangle]`.** Without it, `_start` is mangled into
   `_ZN..._start...` and the bootloader can't find its entry point. Your
   `nm | grep _start` check catches it instantly.

2. **Forgetting the `#[panic_handler]`.** The compiler will *refuse to build*
   with `error: `#[panic_handler]` function required, but not found`. That's
   Rust being explicit where C is silent.

3. **Mixing stable/nightly accidentally.** The *kernel* builds on stable; the
   `bootimage` step needs nightly. Don't conclude "Rust can't do OS dev" from
   a nightly-only packaging requirement — the kernel itself is stable.

4. **`no_std` but reaching for `Vec`/`println!`.** Remember, without an
   allocator and without `std::io`, those simply don't exist. Write bytes to
   the framebuffer, or gradually build an allocator (later chapters / the
   `heap-allocation` concept).

5. **Implicit assumptions about `core::arch::asm!`.** `options(nomem, nostack)`
   promise the asm touches no memory and no stack — true for `hlt`. If you add
   an instruction that *does* touch memory (e.g. writing a port), you must drop
   those options or the optimizer may reorder incorrectly.

6. **The borrow-checker "fight" on `static mut`.** The kernel uses
   `static mut CURSOR_ROW/COL` and reads/writes them inside `unsafe`. Rust 2024
   makes `static mut` access require `unsafe` for *reads* too. A cleaner design
   (seen in Phil Opp's series) wraps the cursor in a `struct` with interior
   mutability. For a "Hello World" kernel, the direct form is fine — just know
   it's the least safe corner of the file.

### When Rust is *better* than C for OS dev (honest)

- **Memory safety by default** — the overlap-and-dangling-pointer classes of
  kernel bugs become compile errors in safe code.
- **`-> !`** makes "never returns" a type-level guarantee instead of a comment.
- **The `#[panic_handler]`** forces you to *decide* and *document* the failure
  path.
- **`unsafe` audit trail** — every hardware assumption is a visible, justified
  block, which is gold for code review.

### When C is still right for you

- If you want to *fully* understand the machine with no compiler between you
  and the hardware, C is more transparent.
- Rust's `unsafe` + ownership learning curve is steep; for a first-ever kernel,
  C is gentler. Rust shines once you're building a *real* memory-safe kernel
  with paging, allocations, and concurrency.

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

---

## Part E — Rust vs. C on the same kernel (side-by-side)

The quickest way to "get" Rust-in-OS-dev is to line the two kernels up. Both
print Hello World to `0xB8000`; the language is the only difference.

| Concern | C (`kernel.c`) | Rust (`main.rs`) |
|---------|----------------|-------------------|
| No libc | `-ffreestanding -nostdlib` flags | `#![no_std]` attribute |
| No `main` runtime | `kernel_main` called by `boot.s` (convention) | `#![no_main]` + `#[no_mangle] extern "C" fn _start` |
| Entry-point name | plain `kernel_main`, any name works | `_start` unmangled via `#[no_mangle]` |
| Never returns | `for (;;);` (runtime, the `.Lhang` net) | `-> !` (type system) |
| Write `0xB8000` | `VGA_MEMORY[i] = …;` freely | `unsafe { *VGA_BUFFER.add(i) = … }` + safety comment |
| On panic/corruption | undefined behavior / whatever happens | mandatory `#[panic_handler]` you write |
| Build target | `-m32` i386 ELF | `x86_64-unknown-none` ELF |

The column that changes everything is the **entry point** and the **panic
path**. C gives you the freedom and none of the guardrails; Rust fences the
dangerous parts behind `unsafe` and *demands* you handle the impossible case.
Neither is "better" — they are two philosophies for the same job, and this hub
teaches you C *first* so you can appreciate exactly what Rust is protecting you
from.

### Ordered build/run summary you can keep

```bash
# STABLE — the verified kernel build:
rustup target add x86_64-unknown-none
cargo build --target x86_64-unknown-none          # -> ELF (verified, 0 errors)

# NIGHTLY — make that ELF bootable:
rustup toolchain install nightly
cargo +nightly install bootimage                  # or add llvm-tools-preview
cargo +nightly bootimage --target x86_64-unknown-none   # -> .bin disk image
qemu-system-x86_64 -drive format=raw,file=target/x86_64-unknown-none/debug/bootimage-example_os_rust.bin
```

> **Why `cargo bootimage`?** It prepends a small BIOS bootloader to your ELF,
> then pads and packs the result into the raw-disk format QEMU boots. See
> [`bootimage`](../../GLOSSARY/bootimage.md "The cargo subcommand that packs your ELF with a bootloader into a bootable disk image") and
> [`bootloader-crate`](../../GLOSSARY/bootloader-crate.md "Rust's bootloader library that hands control to your kernel").
> The toolchain is pinned in [`rustup`](../../GLOSSARY/rustup.md "Rust's toolchain installer — how you add the bare-metal target")
> via `rust-toolchain.toml`.

### Where the `unsafe` really should go (a design hint)

This minimal kernel keeps `unsafe` scattered through `vga_putchar`. The *real*
lesson from Phil Opp's series: **encapsulate all the `unsafe` in one small
module**, then expose a fully safe API. The kernel above is the "frontier"
version where raw pointers are everywhere; the professional version hides them
behind a `Writer` type (see the next-step map below). Keeping `unsafe`
small and isolated is the single most important Rust OS-dev discipline — it
contains the blast radius of any memory bug.

### A tiny glossary walk

- [`no_std`](../../GLOSSARY/no_std.md "The crate attribute that drops the standard library") — the crate attribute that removes `std`.
- [`no_main`](../../GLOSSARY/no_main.md "The crate attribute that removes the Rust main() runtime") — removes the `main` runtime.
- [`panic-handler`](../../GLOSSARY/panic-handler.md "The function Rust calls when a kernel panics") — what runs when things go wrong.
- [`freestanding`](../../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists") — the umbrella concept.
- [`extern-c`](../../GLOSSARY/extern-c.md "The C ABI linkage `extern \"C\"` provides") — why the ABI must match the bootloader.

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
<details class="video-embed">
<summary>▶ Watch: Rust — what is unsafe and when do you need it?</summary>
<iframe src="https://www.youtube-nocookie.com/embed/9E2v8pCUc48" title="Writing Unsafe Rust (Let's Get Rusty)" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>An introduction to Rust's `unsafe` keyword — raw pointers, dereferencing, and the 'safety contract' a programmer takes on — exactly the tool this kernel uses to reach the VGA framebuffer.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: Ownership in Rust — Full Crash Tutorial for Beginners</summary>
<iframe src="https://www.youtube-nocookie.com/embed/9VBLOwmNE1g" title="Ownership in Rust - Full Crash Tutorial for Beginners" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>A step-by-step crash course on the three ownership rules, moves vs. clones, and how they map to the stack and heap — the memory model that lets a kernel omit a garbage collector entirely.</p>
</details>
<details class="video-embed">
<summary>▶ Watch: References and Borrowing in Rust</summary>
<iframe src="https://www.youtube-nocookie.com/embed/Q_0yoX07Fhs" title="References and Borrowing in Rust - Full Crash Tutorial" width="100%" height="400" style="border:0;border-radius:8px;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<p class=video-caption>References (&amp;) vs. ownership, borrowing, and the rules that prevent data races at compile time — why a kernel's shared data (like a global VGA cursor) must live behind explicit synchronization in real Rust.</p>
</details>

> **Next-step map:** this kernel stops at raw framebuffer writes. The Phil Opp
> series (the `Writing an OS in Rust` videos above) turns it into a *safe*
> `Writer` type in Part 3, adds a `println!` macro and testing, then moves into
> CPU exceptions, the [IDT](../../GLOSSARY/idt.md "The table that tells the CPU where each interrupt handler lives"), [paging](../../GLOSSARY/paging.md "The memory-mapping mechanism that gives each process virtual memory") and
> [heap allocation](../../GLOSSARY/heap-allocation.md "Kernel memory that can grow and be handed out at runtime"). Each of those maps to a concept chapter in this hub
> (concepts/03 interrupts, concepts/02 memory management). Start with the VGA
> Writer — it's the smallest step that makes the framebuffer actually *safe*.

---

## 🧪 Exercises & Projects

The Rust track got a hello-world kernel past the hard `no_std`/bare-metal ceremony. These exercises lock in the toolchain choices (target, `no_mangle`, lack of libc) and prove you can port concepts independently of habitat. Prereq: the Rust build loop from this README.

### Graded exercises

**Easy**

- [ ] **E1. Rebuild the kernel from scratch, closed-book** (~20–40 min). Close this page
      and the reference. Recreate `Rust`'s boot + kernel skeleton from memory:
      assembly that sets the stack and calls into the kernel, the kernel's VGA write, and
      the infinite loop. Build using the chapter's exact command sequence. If you stall,
      peek at [`Example_OS_Project`](../../Example_OS_Project/) only for the *toolchain
      flags*, not the code — then re-close it.
- [ ] **E2. Reproduce the five-step recipe in your words** (~20 min). Write (comments or a
      gist) the five steps — assemble, compile, link, ISO, boot — *in this language's*
      syntax. Note the one tool/flag that made this track different from C.
- [ ] **E3. Change the banner to prove ownership** (~20 min). Edit the kernel's message to
      a unique string, rebuild, boot in QEMU, and confirm your string in the output.
      This kills the "it's a template, not mine" feeling for good.

**Medium**

- [ ] **M1. Add a second color/attr** (~1 hr). Extend the VGA write beyond one
      color: print your banner in *bright green on black* and an error line in red on
      white. Practice the `Rust` way of writing to a typed hardware pointer
      (whichever layer your track uses).
- [ ] **M2. Read the fault, don't guess** (~1 hr). Boot with `-d int,cpu_reset` and a
      deliberately broken kernel (e.g. no stack setup). Capture the fault, fix, re-run.
      Write a one-line "what a missing-stack fault looks like here" note.
- [ ] **M3. Deterministic build + clean tree** (~45 min). `make clean && make`, hash the
      `kernel.bin`, re-run, and confirm an identical hash. Then move your build to a second
      machine/VM and reproduce from the repo — proving your toolchain notes are complete.

- [ ] **M4. Nightly vs. stable, mapped** (~1 hr). Identify what in your track needs nightly (interrupt/`#[
o_mangle]`-adjacent runtime pieces) versus what you can keep stable. Write a one-paragraph boundary—it stops confusion later when a build flip-flops `--release`/`--debug`.

**Hard**

- [ ] **H1. Port a concept back in** (~3 hr). Take this language's hello-world kernel and
      add one subsystem from the concept chapters: a PIT timer ISR
      ([concept 03](../concepts/03-interrupts-and-the-idt.md)) or a frame allocator
      ([concept 02](../concepts/02-memory-management.md)). This proves the concepts are
      language-independent.
- [ ] **H2. Compare against C side-by-side** (~1.5 hr). Put your kernel's `Rust`
      source next to `Example_OS_Project/c/kernel.c`. Annotate the *same logical steps*
      (stack, VGA write, loop) across both. Where did the language impose ceremony? Where
      did it save you a line?

### ⭐ Mini-project — Port the Example kernel to a fresh Rust crate

**Goal.** Recreate—new crate, memory, deliberate—a Rust kernel that boots, then grow
it toward a `Writer`-style safe VGA layer. **Estimated time:** 2–4 hr (more if your target
setup is fresh). **Prereq:** the Rust README + toolchain chapter.

1. **Scaffold a bare crate.** `Cargo` project with `#![no_std]`, `#![no_main]`, a
      `#[no_mangle] pub extern "C" fn _start` entry, and `core::panic::panic_fmt`-minimal
      handling so a panic is visible (halt, not UB). See `Example_OS_Project/rust/`.
2. **Wire the linker.** Use the hub's `linker.ld` (entry `_start`, base 1 MiB, `.multiboot`
      first) through the Makefile's `-T` and `-nostdlib` flags — confirm `readelf -h` shows
      the right entry and ELF class.
3. **Raw VGA write.** Write to `0xB8000` via an `unsafe` pointer cast, printing your banner.
      Where the `unsafe` lives—and *why*—is a deliberate placement decision; put it in one
      small function and document the invariant.
4. **Panic is a boot test.** Make panicking tail into an infinite loop that stays visible;
      trigger it once intentionally and confirm QEMU shows it. A defined panic is a
      debugging gift later.
5. **Make it safe.** Wrap the buffer in a `Writer` type with `put_char`/`write_str`, and a
      `term_putchar`; now the raw pointer is contained behind one safe-looking API. This is
      the chapter's promised "safe VGA" step.
6. **Add one concept.** Port the PIT timer ISR (concept 03) *in Rust* — note exactly where
      stable vs. nightly matters (interrupt tables are unstable; your handler can stay
      stable). Print uptime.
7. **Reproduce on a clean machine.** `cargo build` + Makefile from a fresh clone; your
      README (target name, flags, `rust-toolchain.toml`) must be the only guide.

*(Reference: [`Example_OS_Project/rust/`](../../Example_OS_Project/rust/) only when stuck.)*

**Checklist**

- [ ] closed-book kernel rebuild succeeds without the page open
- [ ] self-chosen banner string boots and is visible in QEMU
- [ ] at least one distinct color/attr customisation verified on screen
- [ ] `make clean && make` reproduces an identical `kernel.bin` hash
- [ ] second machine/VM reproduces the build from the repo alone
- [ ] a chosen concept (timer or allocator) is ported and boots

