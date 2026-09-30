# Synthesized Tutorials — The Beginner's Guide to Writing Your Own OS

> **Everything here is original, consolidated content** written for this hub. It is *not* copy-pasted from any source book. It distills the shared ideas from the resources in `path_*_os/` into one beginner-friendly guide that takes you from **basic language syntax** to **real OS concepts** ([bootloaders](../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it"), [memory management](../GLOSSARY/memory-management.md "How a kernel tracks used and free RAM and hands it out safely"), [interrupts](../GLOSSARY/interrupt.md "A hardware signal that makes the CPU run a registered handler") — and more).

## How to read this guide

```
synthesized_tutorials/
├── README.md                     ← you are here
├── 00-introduction/              ← start here
│   └── 01-how-a-computer-boots.md    (BIOS, bootloader, Multiboot)
│   └── 02-your-toolchain.md          (compiler, assembler, linker, QEMU)
├── concepts/                     ← shared ideas used by every language
│   └── 01-bootloaders-and-multiboot.md
│   └── 02-memory-management.md
│   └── 03-interrupts-and-the-idt.md
│   └── 04-vga-text-mode.md
│   └── 05-the-hello-world-of-oses.md   (the one kernel we'll build everywhere)
├── 01-c/                         ← C  version
├── 02-rust/                      ← Rust version
├── 03-cpp/                       ← C++ version
├── 04-go/                        ← Go  version
└── 05-csharp/                    ← C#  version (why it's different)
```

## The one idea behind all five languages

Every OS has a **boot sequence** and a **way to talk to the screen**. No matter the language, the recipe is always the same:

1. **Boot** — a bootloader (GRUB, Limine, or the Rust `bootloader` crate) loads your [kernel](../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") at **1 MiB** and jumps to your [entry point](../GLOSSARY/entry-point.md "The symbol (usually _start) the bootloader jumps to").
2. **Write to VGA text memory at `0xB8000`** — the 80×25 [text framebuffer](../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written"). Each cell is 2 bytes: the character and its color.
3. **Loop forever** (or `hlt`) — a kernel never returns; there's no OS underneath to return to.

The only thing that changes between languages is **how you compile [freestanding](../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists") code** and **how the entry point is called**. Everything else — [paging](../GLOSSARY/paging.md "Translates virtual addresses to physical RAM via page tables"), interrupts, memory allocation — is language-agnostic *concept* work.

## Chapter map (each is original)

| # | Language | You learn | Code file |
|---|----------|-----------|-----------|
| 00 | — | How a computer boots, your toolchain | — |
| concepts | — | Bootloaders, memory, interrupts, VGA | — |
| 01 | C | Freestanding C, `_start`, VGA driver | `kernel.c` + `boot.s` |
| 02 | Rust | `no_std`, panic handler, `bootimage` | `main.rs` |
| 03 | C++ | `extern "C"`, `-fno-exceptions`, VGA driver | `kernel.c++` |
| 04 | Go | gccgo, runtime stubs, multiboot | `kernel.go` |
| 05 | C# | Why C# needs a framework (Cosmos) | `Kernel.cs` template |

> **Mermaid diagrams** are embedded inline throughout — most Markdown renderers (including GitHub, Gitea, and Phoenix Code's preview) draw them natively. Where a real screenshot belongs (e.g. "what QEMU shows"), a `![Screenshot]` placeholder tells you exactly what to add.

---

**Start with [`00-introduction/01-how-a-computer-boots.md`](00-introduction/01-how-a-computer-boots.md).**
