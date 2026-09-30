# ANNOTATION SPEC — how to convert technical terms into tooltip+glossary links

**Task:** Edit the Markdown docs in this hub so every technical keyword becomes a link with a
hover tooltip that takes the reader to its glossary page.

## The exact link format (use this everywhere)

```
[Term](GLOSSARY/slug.md "short hover tooltip")
```

- The `"..."` after the path is the **tooltip** shown on hover (GitHub/Gitea render Markdown
  link titles as native tooltips).
- Clicking goes to `GLOSSARY/slug.md` (a detailed page with diagrams). The GLOSSARY folder
  lives at the hub root: `D:/Projects/OSDev_Learning_Hub/GLOSSARY/`.

## Correct relative paths (IMPORTANT — the prefix depends on where the doc lives)

Compute it from the hub root. Examples that are ALREADY correct in this repo:
- Hub-root files (`README.md`)         → `GLOSSARY/multiboot.md`
- One folder deep (`path_c_os/...`)    → `../GLOSSARY/multiboot.md`
  (e.g. `path_c_os/README.md`, `path_c_os/Bare_Bones_C.md`, `resources/INDEX.md`)
- Two folders deep (`Example_OS_Project/*`, `synthesized_tutorials/*`) → `../../GLOSSARY/multiboot.md`
  (e.g. `Example_OS_Project/docs/setup.md`, `Example_OS_Project/csharp/README.md`,
  `synthesized_tutorials/README.md`, `synthesized_tutorials/concepts/*.md`,
  `synthesized_tutorials/02-rust/README.md`)

Every doc and its prefix is listed in the dispatch message for each annotation job — follow that.

## Rules (follow strictly)

1. **Only link genuine technical terms** — kernel-speak nouns/phrases like "Multiboot",
   "bootloader", "VGA text mode", "page tables", "IDT", "linker script", "QEMU",
   "no_std", "GDT", "ELF", "long mode", etc.
2. **Do NOT link** inside fenced code blocks (```...```), inline code (\`...\`), or within
   existing links. Leave code and filenames (e.g. \`boot.s\`, \`0xB8000\`) untouched.
3. **Do NOT edit headings** (lines starting with `#`).
4. **Do NOT alter or remove** any existing Markdown structure, tables, or content. You are
   ONLY wrapping terms. Preserve every character of the surrounding sentence. Change
   `VGA text mode` → `[VGA text mode](prefix/vga-text-mode.md "tooltip")` and nothing else.
5. **Tooltips:** use the exact tooltip from the glossary `_TERMS.md`. Keep them short
   (5-15 words). Do not paraphrase into something long.
6. **Don't over-link.** Link a term on its FIRST meaningful occurrence in a document, and
   again only where it's genuinely helpful later (e.g. once per section at most). A 150-line
   doc should have maybe 8-20 linked terms, not one per sentence.
7. **Only link terms from the approved slug list below.** If a term isn't on the list, leave it
   as plain text.
8. Preserve the exact casing/pluralization the term appears in, and put the link around the
   whole phrase (e.g. `[memory management](slug)` if the doc says "memory management").
9. The result must still read naturally. Do not wrap part of a hyphenated/qualified term
   unless it is the exact approved term.

## Approved terms → slugs (link target) → tooltip

bootloader.md: "A small program that loads your kernel into memory and jumps to it"
multiboot.md: "The protocol that lets a bootloader load any kernel; magic 0x1BADB002"
bios.md: "The motherboard firmware that starts the machine and finds a bootloader"
uefi.md: "Modern firmware that boots into 64-bit long mode natively"
firmware.md: "Software baked into the motherboard that runs first at power-on"
entry-point.md: "The symbol (usually _start) the bootloader jumps to"
real-mode.md: "The 16-bit CPU mode x86 starts in, with no memory protection"
protected-mode.md: "The 32-bit CPU mode Multiboot v1 kernels run in"
long-mode.md: "The 64-bit CPU mode modern kernels run in"
grub.md: "The free GNU bootloader that loads Multiboot kernels"
limine.md: "A modern bootloader supporting Multiboot 2 and 64-bit kernels"
kernel.md: "The core program that owns the machine and manages hardware"
freestanding.md: "Code compiled assuming no OS or standard library exists"
hosted.md: "A normal program that assumes an OS and libc exist underneath"
no_std.md: "A Rust attribute that disables the standard library for bare metal"
no_main.md: "A Rust attribute that disables the normal main() runtime"
panic-handler.md: "The function that runs when a Rust kernel panics (no OS to report to)"
memory-management.md: "How a kernel tracks used and free RAM and hands it out safely"
paging.md: "Translates virtual addresses to physical RAM via page tables"
heap-allocation.md: "Dynamically allocating memory at runtime; a kernel does it itself"
garbage-collection.md: "Automatic memory reclamation used by managed runtimes"
frame-allocator.md: "The simplest manager that tracks which 4 KiB physical pages are free"
physical-virtual-memory.md: "Real RAM addresses vs the addresses your code sees after paging"
interrupt.md: "A hardware signal that makes the CPU run a registered handler"
idt.md: "The kernel's table of where each interrupt handler lives"
isr.md: "The handler function run for a specific interrupt number"
pic-apic.md: "Chips that route hardware interrupts (timer, keyboard) to the CPU"
gdt.md: "A table of memory segments the CPU uses in protected mode"
hlt-instruction.md: "The CPU instruction that parks the CPU until an interrupt wakes it"
syscall.md: "The way user programs ask the kernel for services"
extern-c.md: "C++ keyword giving a function C linkage so its name isn't mangled"
vga-text-mode.md: "The 80x25 character display mode a minimal kernel writes to"
vga-framebuffer.md: "The memory at 0xB8000 where screen text is written"
cross-compiler.md: "A compiler that builds code for a different CPU/OS than the one it runs on"
assembler.md: "Turns assembly language into machine-code object files"
linker.md: "Merges object files into one image at a chosen address"
elf.md: "The executable format that lets a bootloader load your kernel"
qemu.md: "A free emulator you can boot your kernel in for testing"
make.md: "A build tool that runs compile commands from a Makefile"
bootloader-crate.md: "A Rust crate that wraps a kernel into a bootable disk image"
bootimage.md: "The tool that invokes the bootloader crate to make a bootable image"
cargo.md: "The Rust build tool and package manager"
gccgo.md: "GCC's Go front-end, used to compile Go kernels bare-metal"
cosmos.md: "An open-source C# operating-system kit"
nativeaot.md: ".NET's ahead-of-time compiler that turns IL into native code"
il2cpu.md: "Cosmos's original IL-to-x86 compiler"
managed-il.md: "The intermediate language C# compiles to, which needs a runtime"
rustup.md: "Rust's toolchain installer (for rustup/cargo)"
x86.md: "The CPU architecture family this hub targets"
memory-mapped-io.md: "Hardware controlled by writing to normal memory addresses"
text-mode-cursor.md: "The current write position in the VGA text buffer"

Matching is case-insensitive but PRESERVE the original casing/phrasing in the doc. Note
"VGA text mode" and the "VGA framebuffer"/"0xB8000" terms link to vga-text-mode.md /
vga-framebuffer.md. Shorten the tooltip only if the full one is awkward; keep meaning.

## Deliverable
Edit ONLY the files listed in your dispatch message. After editing, re-read each to confirm
Markdown still parses (links well-formed, no broken brackets). Report the files you changed
and how many terms you linked per file.
