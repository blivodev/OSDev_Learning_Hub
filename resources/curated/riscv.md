# RISC-V — Curated Resources

A long, categorized, verified list of free RISC-V resources for anyone learning operating-system development and low-level programming on the open ISA: the official specs, books and tutorials, assembly intros, bare-metal & kernel-dev guides, QEMU emulation, real boards & SoCs, toolchains, embedded Rust, and video courses. Every link below was verified reachable at curation time.

> Note: `wiki.osdev.org` and a couple of other sites return `403`/a Cloudflare challenge to plain HTTP probes — that is a *bot-block*, not a dead link; the pages render fine in a normal browser. All were verified reachable.

---

## ISA specifications & official documentation

### RISC-V International & the specs
- [RISC-V International (riscv.org)](https://riscv.org/) — the non-profit that owns/maintains the standard; news, blog, and pointers to every official document.
- [RISC-V — Technical Specifications](https://riscv.org/technical/specifications/) — the hub page for all ratified specs (unprivileged, privileged, and the extension specs).
- [Unprivileged ISA spec (v2.2, PDF)](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf) — the free official PDF of the base integer ISA + extensions; the classic entry point.
- [Privileged ISA spec (v1.10, PDF)](https://riscv.org/wp-content/uploads/2017/05/riscv-privileged-v1.10.pdf) — machine/supervisor/user privilege levels, CSRs, MMU/paging, and traps — essential for OS work.
- [riscv-isa-manual (GitHub source)](https://github.com/riscv/riscv-isa-manual) — the Asciidoc/LaTeX source of the ISA manual and its PDF releases; the living spec.
- [riscv-asm-manual](https://github.com/riscv-non-isa/riscv-asm-manual) — the unofficial-but-canonical RISC-V assembly language reference (pseudo-instructions, directives, relocations).
- [riscv-elf-psabi-doc](https://github.com/riscv-non-isa/riscv-elf-psabi-doc) — the RISC-V ELF psABI & calling convention spec: registers, C ABI, relocation types, stack layout.
- [riscv-toolchain-conventions](https://github.com/riscv-non-isa/riscv-toolchain-conventions) — how RISC-V toolchains are named and configured (`-march`/`-mabi` strings, multilib).
- [riscv-arch-test](https://github.com/riscv-non-isa/riscv-arch-test) — the official architectural compliance test-suite (for verifying cores and emulators against the spec).
- [riscv.org blog](https://riscv.org/blog/) — news and technical write-ups from the ecosystem.

### Background & founding documents
- [RISC-V (Wikipedia)](https://en.wikipedia.org/wiki/RISC-V) — a solid high-level overview of the ISA, its history, and the ecosystem.
- [The RISC-V Instruction Set Manual Volume I (Berkeley tech report, PDF)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-54.pdf) — the original 2014 Berkeley technical report by Waterman et al. that launched the ISA.

---

## Reference books, courses & tutorials

### Books
- [The RISC-V Reader: An Open Architecture Atlas](https://riscv.org/learn/) — Patterson & Waterman's slim intro to the ISA (a pocket guide with a RISC-V reference card and instruction glossary). *The book's own site (riscvbook.com) is intermittently offline; riscv.org/learn/ is the working portal — search it for the free language editions.*
- [xv6: a simple, Unix-like teaching OS (RISC-V book, PDF)](https://pdos.csail.mit.edu/6.S081/2023/xv6/book-riscv-rev3.pdf) — the official xv6 book for the RISC-V port, explaining a real kernel line by line.
- [xv6-riscv-book (source)](https://github.com/mit-pdos/xv6-riscv-book) — LaTeX source of the RISC-V xv6 book.

### University courses (RISC-V based)
- [MIT 6.S081: Operating System Engineering (xv6 on RISC-V)](https://pdos.csail.mit.edu/6.S081/2023/) — MIT's OS course, labs and lectures built entirely on the RISC-V xv6 kernel.
- [xv6-riscv (kernel source)](https://github.com/mit-pdos/xv6-riscv) — the clean, readable teaching kernel ported to RISC-V that the 6.S081 labs modify.
- [Berkeley CS61C: Great Ideas in Computer Architecture (RISC-V)](https://cs61c.org/) — the famous Berkeley machine-structures course taught on RISC-V assembly and C.
- [MIT 6.004: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — OCW course that teaches digital systems and ends with a RISC-V CPU (β processor).
- [Illinois CS 425: Operating Systems (xv6-riscv labs)](https://courses.grainger.illinois.edu/cs425/fa2022/) — a full semester wiring up xv6-riscv labs (based on the MIT iteration).

### Self-paced / open learning
- [riscv/learn — official education tracker](https://github.com/riscv/learn) — RISC-V International's running list of courses, workshops, and learning material across the ecosystem.
- [Easy RISC-V](https://easyriscv.dram.page/) — an interactive, in-browser intro to RISC-V assembly (RV32I + PRIV) with a live emulator side-by-side.
- [Writing an OS in 1,000 Lines (Seiya Nuta)](https://github.com/nuta/operating-system-in-1000-lines) — the celebrated walkthrough that boots a small RISC-V OS (riscv64, targeting QEMU) in about a thousand lines of C.
- [Seiya Nuta's blog](https://seiya.me/blog) — author's blog; "Writing an OS in 1,000 Lines" plus low-level RISC-V posts.

---

## Assembly & ISA introductions

- [Easy RISC-V](https://easyriscv.dram.page/) — see above: a gentle interactive intro to registers, branches, memory, and traps (also a good pre-cursor to OS work).
- [RARS — RISC-V Assembler and Runtime Simulator](https://github.com/TheThirdOne/rars/) — a GUI assembler/simulator (like MARS for MIPS) for teaching RV32/RV64 assembly; great for stepping through instructions.
- [RISC-V Assembly Tutorial: Your First Program](https://lucaberton.com/blog/risc-v-assembly-language-tutorial) — a beginner-friendly, no-hardware tutorial: registers, formats, and a hello-world run in QEMU user mode.
- [andymccall/riscv-asm-tutorial (Codeberg)](https://codeberg.org/andymccall/riscv-asm-tutorial) — an assembly tutorial track that includes bare-metal hellos run on the QEMU `virt` machine.
- [riscv-asm-manual](https://github.com/riscv-non-isa/riscv-asm-manual) — the reference for assembler syntax, pseudo-instructions, and directives (also listed under specs).

---

## Bare-metal & OS-development on RISC-V

### OSDev Wiki (RISC-V pages)
- [OSDev Wiki — RISC-V](https://wiki.osdev.org/RISC-V) — the community wiki's main RISC-V overview: privilege levels, base ISAs, extensions, and pointers to bare-bones guides.
- [OSDev Wiki — RISC-V Bare Bones](https://wiki.osdev.org/RISC-V_Bare_Bones) — the minimal RISC-V kernel tutorial (build a serial-printing kernel with GCC + entry assembly).
- [OSDev Wiki — QEMU RISC-V Virt Bare Bones](https://wiki.osdev.org/QEMU_RISC-V_Virt_Bare_Bones) — the go-to "hello world" kernel for the QEMU `virt` machine, with a linker script and `-bios none` recipe.
- [OSDev Wiki — RISC-V Meaty Skeleton](https://wiki.osdev.org/RISC-V_Meaty_Skeleton) — a well-organized template kernel (kernel/libk split) for RISC-V to build on.
- [OSDev Wiki — HiFive-1 Bare Bones](https://wiki.osdev.org/HiFive-1_Bare_Bones) — get a kernel running on the SiFive HiFive1 board.

### Written bare-metal / from-scratch guides
- [Bare metal programming with RISC-V (popovicu)](https://popovicu.com/posts/bare-metal-programming-risc-v/) — clear write-up of the QEMU `riscv64 virt` boot sequence (ZSBL ROM, OpenSBI, `0x80000000`, UART) with a working freestanding example.
- [RISC-V bare metal (dynamicmalloc)](https://www.dynamicmalloc.com/riscv_bare_metal.html) — two practical posts: bare metal *without* OpenSBI and bare metal *with* OpenSBI/SBI, dumping the device tree and talking to the NS16550 UART.
- [RISC-V from scratch (Twilko, GitHub)](https://github.com/twilco/riscv-from-scratch) — a multi-part series booting bare-metal RISC-V on QEMU `virt`: devicetree, linker scripts, crt0, and a UART driver in assembly/freestanding C.
- [RISC-V from scratch 3: UART driver in assembly](https://twilco.github.io/riscv-from-scratch/2019/07/08/riscv-from-scratch-3.html) — one of the working parts of the above series (NS16550A driver + assembly ABI basics).
- [PLCTLab riscv-operating-system-mooc](https://github.com/plctlab/riscv-operating-system-mooc) — an open RISC-V OS course (Chinese/English) walking through writing a RISC-V OS from scratch, with slides and code.
- [rv32emu (sysprog21)](https://github.com/sysprog21/rv32emu) — a cleanly written RV32IMC emulator in C; reading it is a great way to learn RISC-V execution semantics while doing systems programming.
- [Writing an OS in 1,000 Lines (Seiya Nuta)](https://github.com/nuta/operating-system-in-1000-lines) — boots a working RISC-V OS on QEMU `virt`; also listed under tutorials.
- [skyzh/core-os-riscv](https://github.com/skyzh/core-os-riscv) — a minimal RISC-V teaching OS with a companion book, aimed at OS-dev beginners.

---

## QEMU: running RISC-V virtually

- [QEMU RISC-V documentation (wiki)](https://wiki.qemu.org/Documentation/Platforms/RISCV) — the community wiki page covering QEMU's RISC-V machines (incl. the `virt` board) and how to boot them.
- [QEMU RISC-V system emulation docs](https://www.qemu.org/docs/master/system/target-riscv.html) — the official manual for RISC-V emulation modes (system vs. user), boards, and options.
- [QEMU source: `virt` machine docs (`docs/system/riscv/virt.rst`)](https://github.com/qemu/qemu/blob/master/docs/system/riscv/virt.rst) — in-tree documentation of the `virt` board memory map, device layout, and boot.
- [QEMU main repository](https://github.com/qemu/qemu) — source for `qemu-system-riscv32/64` and `qemu-riscv32/64` user-mode emulation (branch/tag per release).

### QEMU quick-reference (from the verified guides above)
- Boot a bare kernel on the `virt` board with `qemu-system-riscv64 -machine virt -bios none -kernel kernel.elf -serial mon:stdio`.
- RAM base for hand-written code is `0x80000000` (OpenSBI/fw loads there too); the NS16550-compatible UART is at `0x10000000`.

---

## Boards, SoCs, and hardware targets

### Low-cost embedded / dev boards
- [SiFive HiFive1 Rev B](https://www.sifive.com/boards/hifive1-rev-b) — the canonical RV32IMAC Feather-form board (SiFive FE310) used by the OSDev HiFive-1 bare-bones tutorial.
- [SiFive boards overview](https://www.sifive.com/boards) — SiFive's HiFive family (HiFive1, Unmatched, Premier P550) page.
- [SiFive HiFive Unmatched](https://www.sifive.com/boards/hifive-unmatched) — a Linux-capable RV64 dev board (FU740), the affordable "real machine" OS target.
- [SparkFun RED-V (RedBoard)](https://www.sparkfun.com/products/15574) — a low-cost RV32 dev board (DABoard / FE310 class) that runs the freedom-e-sdk and the RISC-V GNU toolchain.
- [SiFive FE310 documentation](https://www.sifive.com/documentation) — datasheets and program manuals for SiFive silicon (incl. the FE310 used on HiFive/RED-V).

### K210 / Kendryte (RV64 dual-core MCU)
- [Kendryte K210](https://kendryte.com/) — the RV64GC dual-core AI MCU found on many cheap boards (Sipeed Maix, others).
- [kendryte-standalone-sdk](https://github.com/kendryte/kendryte-standalone-sdk) — the bare-metal C SDK for the K210 (freestanding, no kernel).
- [Sipeed MaixPy](https://github.com/sipeed/MaixPy) — MicroPython + firmware for the K210-based Maix boards (useful for quick experiments before going bare metal).

### Linux-capable single-board computers
- [StarFive VisionFive / JH7100/JH7110](https://starfivetech.com/) — vendor page for the VisionFive & VisionFive 2 RV64 SBCs (Linux-capable).
- [StarFive documentation (RVspace)](https://doc-en.rvspace.org/) — the official StarFive documentation hub (VisionFive 2 user guides, SDKs, schematics).
- [starfive-tech (GitHub org)](https://github.com/starfive-tech) — StarFive's open source: kernels, buildroots, U-Boot, and board support.
- [MilkV (milkv.io)](https://milkv.io/) — Milk-V boards (Milk-V Jupiter, Duo) — budget RISC-V Linux SBCs for real-hardware OS work.

### FPGA / open cores
- [riscv-mini (ucb-bar)](https://github.com/ucb-bar/riscv-mini) — a small, clean, educational RISC-V RV32I core in Chisel; great for understanding pipelining/control.
- [Chipyard (ucb-bar)](https://github.com/ucb-bar/chipyard) — the Berkeley SoC framework for building and testing RISC-V SoCs on FPGAs/ASICs.

---

## Toolchains & low-level build tools

- [riscv-gnu-toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain) — builds `riscv64-unknown-elf-*` (bare-metal GCC/ld/as) and `riscv64-linux-gnu-*` (for Linux user-mode); the standard toolchain. Build with `--enable-multilib` to target both rv32/rv64.
- [riscv-isa-sim (Spike)](https://github.com/riscv-software-src/riscv-isa-sim) — the reference ISA simulator (functional model of the core), useful alongside a real toolchain.
- [riscv-pk (proxy kernel)](https://github.com/riscv-software-src/riscv-pk) — the proxy kernel / bootloader that lets bare Spike or QEMU run Linux-style binaries (also a good small piece of RISC-V firmware to read).
- [OpenSBI](https://github.com/riscv-software-src/opensbi) — the open Supervisor Binary Interface firmware QEMU and many boards use to boot; understanding it clarifies M-mode → S-mode handoff for OS init.
- [riscv-tests](https://github.com/riscv-software-src/riscv-tests) — the canonical instruction and privileged-mode test suite used to validate tools/emulators/cores.
- [riscv-toolchain-conventions](https://github.com/riscv-non-isa/riscv-toolchain-conventions) — naming/`-march`/`-mabi` conventions for building and selecting RISC-V toolchains (also under specs).

### Linker-script & freestanding notes (from the verified guides above)
- A bare RISC-V kernel uses `-mcmodel=medany`, `-ffreestanding -nostdlib`, and a linker script with `. = 0x80000000;` (QEMU `virt` RAM base), `ENTRY(_start)`, and a reserved stack region — see the OSDev QEMU RISC-V Virt Bare Bones and popovicu guides above for exact recipes.

---

## Embedded Rust on RISC-V

- [riscv-rt (rust-embedded)](https://github.com/rust-embedded/riscv-rt) — the standard `#[riscv_rt::entry]` minimal runtime/startup crate for bare-metal RISC-V.
- [riscv (rust-embedded)](https://github.com/rust-embedded/riscv) — low-level Rust register/instruction access for RISC-V (`riscv` crate: CSR ops, `asm!`, traps).
- [`riscv` crate docs (docs.rs)](https://docs.rs/riscv/latest/riscv/) — the crate documentation for reading/writing CSRs and executing privileged instructions from Rust.
- [The Embedonomicon](https://docs.rust-embedded.org/embedonomicon/) — the official rust-embedded book on the *very* low-level details (startup, linker scripts, atomics) — architecture-agnostic but essential context for no_std RISC-V kernels.
- [esp-hal (esp-rs)](https://github.com/esp-rs/esp-hal) — Espressif's HAL covering their RISC-V cores (ESP32-C3/C6/H2); a modern, maintained embedded-Rust-on-RISC-V reference.
- [esp-rs / rust-build](https://github.com/esp-rs/rust-build) — prebuilt Rust toolchains targeting the Espressif RISC-V chips (quick no_std RISC-V setup).

> Note: the popular rust-embedded `Discovery` book and `rust-raspberrypi-OS-tutorials` are excellent but target **ARM** (STM32/BCM2711), so they are intentionally not listed here — see the general language/OS-dev pages instead.

---

## Video courses & playlists on RISC-V

- [RISC-V International (YouTube channel)](https://www.youtube.com/c/RISC-V_International) — the official channel: spec deep-dives, summit talks, and introductions by the ISA's designers.
- [MIT 6.004: Computation Structures (OCW videos)](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — recorded lectures covering digital logic, assembly, pipelining, and RISC-V.
- [Linux and RISC-V: From Concept to Real Systems](https://www.youtube.com/watch?v=IqLOPZWOOvw) — a concise video mapping the RISC-V ISA up to a running Linux kernel (good "big picture" start).
- [Berkeley CS61C (RISC-V architecture) lecture archive](https://cs61c.org/) — the course pages link the RISC-V lecture videos/slides.
- [xv6-riscv source walkthroughs (various)](https://github.com/mit-pdos/xv6-riscv) — pair the kernel source with the community's video walkthroughs of the RISC-V xv6 code (search "xv6 riscv" on YouTube for the Low Byte Productions Source Dive series referenced by the community).

---

*All links lead to free, publicly accessible resources. URLs were verified reachable at curation time (2026-09-30). Sites that show `403`/CAPTCHA to scripts (notably wiki.osdev.org) are still live in a normal browser.*
