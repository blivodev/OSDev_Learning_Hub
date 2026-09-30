<!-- GLOSSARY PAGE TEMPLATE — copy this structure for every <slug>.md page.
     Replace every {{PLACEHOLDER}}. Do not rename the file; it must be <slug>.md. -->

# `extern "C"`

> **[Back to glossary index](README.md)** · Category: CPU & interrupts

`extern "C"` is a C++ (and Rust, via `#[no_mangle]`/`extern "C"`) language construct that gives a function C linkage so its exported symbol name is not mangled.

## The short version
C++ and Rust mangle function names to encode their arguments and namespaces, but the [assembler](assembler.md) entry point in `boot.s` calls a plain symbol like `kernel_main`. Declaring or defining that function with `extern "C"` (or `#[no_mangle]`) keeps its exported name unmangled, so the linker can resolve the `call kernel_main` in `boot.s` to the high-level function.

## Detailed explanation
Compiled, a function becomes a symbol the [linker](linker.md) matches across object files. C++ decorates symbols with its type-mangling scheme (e.g. `_Z11kernel_mainv`), and Rust similarly mangles by default (e.g. `_ZN3foo10kernel_main17h...E`). But `boot.s` emits a bare `call kernel_main`:

```asm
call kernel_main   /* jump into the C/C++/Go kernel */
```

For that call to link, the kernel's entry function must be exported under the unmangled symbol `kernel_main`. In C++ you write `extern "C" void kernel_main()` (or wrap in `extern "C" { ... }`); in Rust you mark it `#[no_mangle] pub extern "C" fn kernel_main()`. The `extern "C"` part also fixes the calling convention, which the assembly call relies on.

The same principle generalizes beyond the entry point: any function the assembly or a foreign ABI must call — an [ISR](isr.md) stub, a syscall handler, a callback handed to C code — should be `extern "C"`. This is why the glossary groups it under interrupts: the CPU-facing glue that the [IDT](idt.md) points at is typically written with C linkage so the addresses the descriptors reference match exactly the symbols the assembler and linker expect.

Note the Rust interrupt snippet in the tutorial uses a different-but-related annotation: `extern "x86-interrupt"` — that fixes the *interrupt* calling convention (compiler emits `iret`, proper register save), while `extern "C"`/`#[no_mangle]` fixes the *name* and the ordinary C ABI.

## Why it matters here (OSDev_Learning_Hub)
`Example_OS_Project/c/boot.s` calls `kernel_main` by its raw C symbol name — this works out of the box in the C version, but the C++ and Rust ports need `extern "C"`/`#[no_mangle]` so that same `call kernel_main` resolves. It's the glue that lets a single shared `boot.s` (which the project comments note is "shared by the C, C++ and GO kernels") serve every language.

## Watch / listen
- [Wikipedia — Name mangling](https://en.wikipedia.org/wiki/Name_mangling) — free, authoritative
- [OSDev Wiki — C++](https://wiki.osdev.org/C%2B%2B) — free, authoritative

## Related terms
- [Entry Point (`_start`)](entry-point.md)
- [Assembler (NASM / GAS)](assembler.md)
- [Linker / Linker Script](linker.md)
- [Kernel](kernel.md)
- [Interrupt Descriptor Table (IDT)](idt.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
