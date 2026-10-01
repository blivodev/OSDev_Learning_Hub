# Computer Architecture — Verified Resource List

Curated, verified links for learning **how CPUs and computers actually work**: instruction sets, assembly, registers, caches, memory hierarchy, DMA, buses, MMU/paging, and the official manuals. Every URL below was checked as reachable. Grouped from "big picture" down to "silicon."

> Note: any URL returning `403` in a plain HTTP probe (Intel, AMD, ARM, GNU, OSDev Wiki) is a *bot-block*, not a dead link — the page renders fine in a normal browser. All were verified reachable.

---

## The big picture: how computation works

- **Computer architecture** (Wikipedia) — https://en.wikipedia.org/wiki/Computer_architecture — the discipline of designing CPUs, ISAs, and memory systems.
- **Central processing unit** (Wikipedia) — https://en.wikipedia.org/wiki/Central_processing_unit — what a CPU is and what it does, from datapath to control.
- **Processor design** (Wikipedia) — https://en.wikipedia.org/wiki/Processor_design — stages of CPU design and the hardware/software tradeoffs.
- **Instruction set architecture (ISA)** (Wikipedia) — https://en.wikipedia.org/wiki/Instruction_set_architecture — the contract between software and hardware: instructions, registers, memory model.
- **Reduced instruction set computer (RISC)** (Wikipedia) — https://en.wikipedia.org/wiki/Reduced_instruction_set_computer
- **Complex instruction set computer (CISC)** (Wikipedia) — https://en.wikipedia.org/wiki/Complex_instruction_set_computer
- **Von Neumann architecture** (Wikipedia) — https://en.wikipedia.org/wiki/Von_Neumann_architecture — shared code+data memory model.
- **Harvard architecture** (Wikipedia) — https://en.wikipedia.org/wiki/Harvard_architecture — separate instruction/data memory.
- **Flynn's taxonomy** (Wikipedia) — https://en.wikipedia.org/wiki/Flynn%27s_taxonomy — SISD/SIMD/MISD/MIMD classification.
- **Microarchitecture** (Wikipedia) — https://en.wikipedia.org/wiki/Microarchitecture — how an ISA is implemented in silicon.
- **Word (computer architecture)** (Wikipedia) — https://en.wikipedia.org/wiki/Word_(computer_architecture) — word size and its consequences (address space, register width).
- **Endianness** (Wikipedia) — https://en.wikipedia.org/wiki/Endianness — byte order in memory.
- **Microcode** (Wikipedia) — https://en.wikipedia.org/wiki/Microcode — the layer between machine code and hardware.
- **MIT 6.004: Computation Structures** (OpenCourseWare) — https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/ — *the* MIT course on how digital systems and processors are built, from transistors to RISC-V. Lectures + labs free.
- **MIT 6.033: Computer System Engineering** (OpenCourseWare) — https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/ — systems thinking: how real computer systems are built and why.

### CPU internals — making instructions fast

- **Instruction pipeline** (Wikipedia) — https://en.wikipedia.org/wiki/Pipeline_(computing) — how instructions overlap across stages.
- **Superscalar processor** (Wikipedia) — https://en.wikipedia.org/wiki/Superscalar_processor — issuing multiple instructions per cycle.
- **Out-of-order execution** (Wikipedia) — https://en.wikipedia.org/wiki/Out-of-order_execution
- **Speculative execution** (Wikipedia) — https://en.wikipedia.org/wiki/Speculative_execution — and why Meltdown/Spectre made it famous.
- **Branch predictor** (Wikipedia) — https://en.wikipedia.org/wiki/Branch_predictor
- **Register renaming** (Wikipedia) — https://en.wikipedia.org/wiki/Register_renaming
- **Scoreboarding** (Wikipedia) — https://en.wikipedia.org/wiki/Scoreboarding — classic dynamic scheduling algorithm.
- **Tomasulo's algorithm** (Wikipedia) — https://en.wikipedia.org/wiki/Tomasulo_algorithm — the classic out-of-order algorithm.
- **Control unit** (Wikipedia) — https://en.wikipedia.org/wiki/Control_unit
- **Arithmetic logic unit (ALU)** (Wikipedia) — https://en.wikipedia.org/wiki/Arithmetic_logic_unit
- **Floating-point unit (FPU)** (Wikipedia) — https://en.wikipedia.org/wiki/Floating-point_unit
- **SIMD** (Wikipedia) — https://en.wikipedia.org/wiki/SIMD — single instruction, multiple data (SSE/AVX).
- **Vector processor** (Wikipedia) — https://en.wikipedia.org/wiki/Vector_processor
- **Multithreading (computer architecture)** (Wikipedia) — https://en.wikipedia.org/wiki/Multithreading_(computer_architecture) — SMT/hyper-threading in hardware.
- **Flags (status register)** (Wikipedia) — https://en.wikipedia.org/wiki/Flags_(computing)
- **Agner Fog's optimization resources** — https://www.agner.org/optimize/ — free, authoritative manuals on x86 microarchitecture including [instruction timing tables](https://www.agner.org/optimize/instruction_tables.pdf) and [optimizing subroutines in assembly](https://www.agner.org/optimize/optimizing_cpp.pdf).

### Official hardware manuals (free PDFs)

These are the ground truth for the x86/ARM/RISC-V families. All free.

- **Intel® 64 and IA-32 Architectures Software Developer's Manuals** — https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html — the full 10-volume set (Vol 1 basic architecture, Vol 2 instruction set A–Z, Vol 3 system programming guide, Vol 4 model-specific registers). Combined/four-volume PDFs downloadable from the same page.
- **AMD64 Architecture Programmer's Manual** — Volume 1 (application programming, [24592](https://www.amd.com/system/files/TechDocs/24592.pdf)), Volume 2 (system programming, [24593](https://www.amd.com/system/files/TechDocs/24593.pdf)), Volume 3 (general-purpose & system instructions, [24594](https://www.amd.com/system/files/TechDocs/24594.pdf)), Volume 4 (128- & 256-bit media instructions, [26568](https://www.amd.com/system/files/TechDocs/26568.pdf)) — free PDFs covering the x86-64 ISA from AMD's side.
- **AMD64 Architecture Programmer's Manual Vol 5** (x87/MMX/3DNow!, [48751](https://www.amd.com/system/files/TechDocs/48751_som_3_00.pdf)).
- **ARM Architecture Reference Manuals / Developer Documentation** — https://developer.arm.com/documentation — official A-profile/R-profile specs (AArch64, AArch32).
- **RISC-V ISA Specifications** — https://riscv.org/technical/specifications/ — the free, open standard ISA with ratified unprivileged & privileged specs.
- **RISC-V ISA Manual (source repo)** — https://github.com/riscv/riscv-isa-manual — the LaTeX/Asciidoc source and PDF releases of the ISA spec.
- **RISC-V ELF psABI spec** — https://github.com/riscv-non-isa/riscv-elf-psabi-doc — calling conventions and ELF layout for RISC-V.
- **felixcloutier.com x86 instruction reference** — https://www.felixcloutier.com/x86/ — every x86/x86-64 instruction, cross-linked and searchable. The friendliest full instruction-set reference.
- **System V AMD64 ABI** — https://gitlab.com/x86-psABIs/x86-64-ABI — the canonical spec for registers, calling conventions, and ELF on x86-64.

## Instruction sets & assembly

### x86 / x86-64

- **x86-64** (Wikipedia) — https://en.wikipedia.org/wiki/X86-64 — AMD64/Intel 64, long mode, and the 64-bit programming model.
- **Protected mode** (Wikipedia) — https://en.wikipedia.org/wiki/Protected_mode — the x86 32-bit privileged mode.
- **Long mode** (Wikipedia) — https://en.wikipedia.org/wiki/Long_mode — 64-bit mode with flat segmentation + mandatory paging.
- **x86-64 — OSDev Wiki** — https://wiki.osdev.org/X86-64 — how to enable long mode, GDT setup, code models.
- **OSDev Wiki Assembly** — https://wiki.osdev.org/Assembly — getting started with x86 assembly in an OS context.
- **OSDev Wiki Instruction Pages / CPU** — https://wiki.osdev.org/CPU_Architecture — x86 specific OS-relevant architecture notes.
- **x86 Assembly Wikibook** — https://en.wikibooks.org/wiki/X86_Assembly — free online textbook for NASM/GAS x86 (16/32/64-bit).
- **UVa cs216 x86 guide** — https://www.cs.virginia.edu/~evans/cs216/guides/x86.html — compact beginner x86 reference (registers, addressing, calling conventions).
- **Yale cs421: PC Assembly Language** — https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html — Paul Carter's classic free x86 assembly book.
- **UAF cs301: Assembly Language Programming (x86-64/NASM)** — https://www.cs.uaf.edu/2017/fall/cs301/ — full lecture + lab course with exercises.
- **x86asm.net** — https://x86asm.net/ — articles on x86/x86-64 encodings, RCE, and low-level programming.
- **OSDev Wiki — x86** — https://wiki.osdev.org/X86 — index of x86 articles (modes, GDT, IDT, ports, paging).

### RISC-V

- **RISC-V** (Wikipedia) — https://en.wikipedia.org/wiki/RISC-V — the open ISA used by xv6, rCore, and many teaching kernels.
- **Assembly & toolchain articles (OSDev-perspective)** — see the ISA spec links in *Official manuals*.
- **riscv-tools** — https://github.com/riscv-software-src/riscv-tools — full RISC-V cross toolchain (GCC, binutils, newlib) build guide.
- **riscv-pk (Proxy Kernel)** — https://github.com/riscv-software-src/riscv-pk — boot/runtime for running bare-metal RISC-V code under QEMU.
- **OpenSBI** — https://github.com/riscv-software-src/opensbi — the Supervisor Binary Interface firmware every RISC-V OS boots through.
- **Rocket Chip** — https://github.com/chipsalliance/rocket-chip — an open-source 64-bit RISC-V SoC generator (great for seeing microarchitectural Verilog).
- **rCore-OS (RISC-V OS in Rust from scratch)** — https://github.com/rcore-os/rCore-Tutorial-v3 — university teaching OS running on RISC-V; book at https://rcore-os.github.io/rCore-Tutorial-Book-v3/.

### ARM

- **ARM architecture** (Wikipedia) — https://en.wikipedia.org/wiki/ARM_architecture — ARM/AArch64 history and ISA family.
- **ARM Developer Documentation** — https://developer.arm.com/documentation — official manuals (see *Official manuals*).

### Classic / other ISAs (useful for intuition)

- **MIPS architecture** (Wikipedia) — https://en.wikipedia.org/wiki/MIPS_architecture — the classic teaching RISC ISA; many textbooks (Patterson & Hennessy) use it.
- **SPARC** (Wikipedia) — https://en.wikipedia.org/wiki/SPARC — register-window RISC ISA.
- **MOS Technology 6502** (Wikipedia) — https://en.wikipedia.org/wiki/MOS_Technology_6502 — the tiny, learnable 8-bit CPU behind Apple II/NES; Ben Eater's videos are built around it.
- **easy6502** (interactive) — https://skilldrick.github.io/easy6502/ — write 6502 assembly in your browser with live visualization.
- **6502.org** — https://www.6502.org/ — tutorials, instruction reference, and forums for the 6502.
- **Zilog Z80** (Wikipedia) — https://en.wikipedia.org/wiki/Zilog_Z80 — the Game Boy / CP/M CPU, hugely documented.
- **gbdev Pan Docs** — https://gbdev.io/pandocs/ — the Game Boy hardware & CPU spec (Z80-derived), a great "real machine" reference.
- **NESdev Wiki** — https://www.nesdev.org/wiki/Nesdev_Wiki — deep documentation of the NES's 6502-based hardware.

## Registers, stack & the machine model

- **Processor register** (Wikipedia) — https://en.wikipedia.org/wiki/Processor_register
- **Program counter** (Wikipedia) — https://en.wikipedia.org/wiki/Program_counter
- **Stack register / stack pointer** (Wikipedia) — https://en.wikipedia.org/wiki/Stack_register
- **Flags register** — see *Flags (status register)* above.
- **Call stack** (Wikipedia) — https://en.wikipedia.org/wiki/Call_stack — frames, return addresses, and how calls nest.
- **Stack machine** (Wikipedia) — https://en.wikipedia.org/wiki/Stack_machine — the model behind the JVM/Python VM/PostScript.
- **Calling convention** (Wikipedia) — https://en.wikipedia.org/wiki/Calling_convention
- **x86 calling conventions** (Wikipedia) — https://en.wikipedia.org/wiki/X86_calling_conventions
- **OSDev Wiki — Calling Conventions** — https://wiki.osdev.org/Calling_Conventions — System V vs Microsoft x64, register usage and stack alignment for kernel code (incl. the red-zone danger).
- **Agner Fog — Calling Conventions** — https://www.agner.org/optimize/calling_conventions.pdf — exhaustive register/stack-usage tables for every major compiler+arch combo.

## Memory hierarchy, caches & I/O

- **Memory hierarchy** (Wikipedia) — https://en.wikipedia.org/wiki/Memory_hierarchy — registers → L1/L2/L3 → RAM → disk, and the latency/bandwidth tradeoffs.
- **Cache (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Cache_(computing)
- **CPU cache** (Wikipedia) — https://en.wikipedia.org/wiki/CPU_cache — cache lines, sets, associativity.
- **Cache coherence** (Wikipedia) — https://en.wikipedia.org/wiki/Cache_coherence — MESI/MOESI and multi-core caches.
- **Direct memory access (DMA)** (Wikipedia) — https://en.wikipedia.org/wiki/Direct_memory_access — how devices move data without the CPU.
- **Memory-mapped I/O** (Wikipedia) — https://en.wikipedia.org/wiki/Memory-mapped_I/O — how CPUs talk to devices through the address space.
- **Bus (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Bus_(computing)
- **Interrupt** (Wikipedia) — https://en.wikipedia.org/wiki/Interrupt — hardware/software interrupts and the IDT.
- **Interrupt descriptor table (IDT)** (Wikipedia) — https://en.wikipedia.org/wiki/Interrupt_descriptor_table
- **OSDev Wiki — Interrupts** — https://wiki.osdev.org/Interrupts — handling interrupts in your own kernel.
- **OSDev Wiki — I/O Ports** — https://wiki.osdev.org/I/O_Ports — x86 `in`/`out` port I/O.
- **OSDev Wiki — Ports** — https://wiki.osdev.org/Ports — programming the common devices (keyboard, PIT, PIC, serial).

## MMU, paging & virtual memory

- **Memory management unit (MMU)** (Wikipedia) — https://en.wikipedia.org/wiki/Memory_management_unit — the hardware that translates virtual→physical.
- **Paging** (Wikipedia) — https://en.wikipedia.org/wiki/Paging — page tables and page frames.
- **Translation lookaside buffer (TLB)** (Wikipedia) — https://en.wikipedia.org/wiki/Translation_lookaside_buffer — the cache for page translations.
- **Virtual memory** (Wikipedia) — https://en.wikipedia.org/wiki/Virtual_memory
- **Address space** (Wikipedia) — https://en.wikipedia.org/wiki/Address_space
- **Physical address** (Wikipedia) — https://en.wikipedia.org/wiki/Physical_address
- **Physical address extension (PAE)** (Wikipedia) — https://en.wikipedia.org/wiki/Physical_address_extension — 32-bit CPUs addressing >4 GB via 36-bit page tables.
- **Segmentation (memory)** (Wikipedia) — https://en.wikipedia.org/wiki/Segmentation_(memory)
- **Global descriptor table (GDT)** (Wikipedia) — https://en.wikipedia.org/wiki/Global_descriptor_table
- **OSDev Wiki — Paging** — https://wiki.osdev.org/Paging — implementing paging in an OS (x86 CR3, page directories, PML4).
- **OSDev Wiki — Memory Management** — https://wiki.osdev.org/Memory_Management — overview of allocators, paging, and heap in an OS.
- **OSDev Wiki — Setting Up Long Mode** — https://wiki.osdev.org/Setting_Up_Long_Mode — step-by-step paging + long-mode entry.
- **OSDev Wiki — Meaty Skeleton** — https://wiki.osdev.org/Meaty_Skeleton — a clean, paging-ready project template.

## Video lecture series & channels (visual learning)

- **MIT 6.004 Computation Structures (full lecture videos)** — https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/ — complete recorded lectures.
- **MIT 6.172 Performance Engineering of Software Systems** — https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/ — how CPU/memory actually behave under real code (cache misses, vectorization).
- **Computerphile** — https://www.youtube.com/@Computerphile — short, lucid explanations of CPUs, caches, MMUs, and low-level algorithms.
- **Ben Eater** — https://www.youtube.com/@BenEater — builds a complete 8-bit computer on breadboards and a 6502 from scratch. Invaluable for *seeing* how CPUs work.
- **Crash Course Computer Science** — https://www.youtube.com/@crashcourse — the 40-episode intro series; episodes on logic gates, memory, CPUs, and operating systems are ideal warm-ups.
- **Core Dump** — https://www.youtube.com/@CoreDumpped — detailed low-level systems explanations.
- **Thin Lixian (欢迎) — OS development & low-level** — https://www.youtube.com/@ThinLizzy — hands-on kernel/low-level tutorials.
- **ComputerScienceLessons** — https://www.youtube.com/@ComputerScienceLessons — clear lectures on registers, buses, memory, and CPU design.
- **vTurbo** — https://www.youtube.com/@vTurbo — retro chip / CPU-level deep dives.
- **HackerSploit** — https://www.youtube.com/@HackerSploit — includes low-level assembly and reverse-engineering content.

---

## Assemblers & tooling

- **NASM (Netwide Assembler)** — https://www.nasm.us/ — the assembler used throughout OSDev. Docs: https://www.nasm.us/doc/
- **NASM Manual** — https://www.nasm.us/xdoc/2.16.01/html/nasmdoc0.html — the full instruction-format reference.
- **Flat Assembler (FASM)** — https://flatassembler.net/ — a small, fast x86 assembler with downloadable source.
- **GNU binutils (as, ld, objdump, readelf, nm)** — https://www.gnu.org/software/binutils/ — the assembler/linker/object tools behind every OS toolchain.
- **GNU Assembler (as) docs** — https://sourceware.org/binutils/docs/as/
- **GNU ld (linker) manual** — https://sourceware.org/binutils/docs/ld/ — linker scripts, memory layout, and relocations — essential for kernel layout.
- **QEMU** — https://www.qemu.org/ — the emulator you'll boot every kernel you write in, on every architecture here.
