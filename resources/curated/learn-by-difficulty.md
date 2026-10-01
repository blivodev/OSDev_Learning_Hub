# Learning by Difficulty — A Ladder for OS Development

This page re-presents everything in the hub's curated resource library (tutorials, books, video series, language-specific material, and architecture references) as a **difficulty ladder**. OS development is a long climb, and the biggest mistake beginners make is jumping into a "full kernel from scratch" series before they can read an instruction, boot a bare-bones kernel, or describe what the GDT/IDT/paging are. Use the tiers below to pick resources that match your current skill level, then move up.

## How to use this ladder

1. **Start at Beginner and don't skip.** The tiers are cumulative — each one assumes the conceptual vocabulary the tier below it teaches. If a term in a section's description is unfamiliar, that section is probably still a step ahead of you.
2. **Pick one lane per tier, not all of them.** Within each tier, "OSDev tutorials/series" and "Books" overlap heavily. Choose either the series *or* the book/tutorial route (matching your preferred language), not both, or you'll be re-reading the same concepts.
3. **Language-specific and Architecture sections are companions, not prerequisites.** They reinforce whatever tier they sit in. Use the language sections to get fluent before writing that tier's kernel code, and the architecture sections to understand the hardware your kernel runs on.
4. **"Hard" and "Very Hard" are study targets, not assigned reading.** Real, industrial-strength operating systems (Linux, SerenityOS, Theseus, Redox) are *huge*. At those tiers you read their source and papers for understanding, not to reproduce them.
5. **Verify as you go.** Every link below is copied verbatim from the hub's curated pages (all verified reachable). When a tutorial gives you code, type it — don't copy-paste — and boot it with QEMU ([https://www.qemu.org/](https://www.qemu.org/)) as you go.

---

## Beginner

*Assumes: you can write a small program in C or your language of choice, and know roughly what assembly is. Goal: boot *something* and get text on screen.*

### OSDev tutorials/series
- [OSDev Wiki — Getting Started](https://wiki.osdev.org/Getting_Started) — the recommended first page; prerequisite knowledge and a reading order.
- [OSDev Wiki — Required Knowledge](https://wiki.osdev.org/Required_Knowledge) — what you should know before starting (C, assembly, PC architecture).
- [OSDev Wiki — Bare Bones](https://wiki.osdev.org/Bare_Bones) — the canonical minimal 32-bit C kernel booted by GRUB + Multiboot. The classic "first kernel".
- [OSDev Wiki — Beginner Mistakes](https://wiki.osdev.org/Beginner_Mistakes) — the pitfalls every new OSdev hits. Read this before you start writing code.
- [cfenollosa/os-tutorial](https://github.com/cfenollosa/os-tutorial) — "How to create an OS from scratch": short, incremental READMEs from boot sector to a simple shell (no GRUB).
- [Nanobyte — Building-an-OS example code (nanobyte_os)](https://github.com/nanobyte-dev/nanobyte_os) — the complete source and build scripts for Nanobyte's from-floppy upward video series.
- [Nanobyte's site/devlog](https://nanobyte.dev/) — transcripts and extra material for the series.

### Books
- [The Little OS Book](https://littleosbook.github.io/) — a concise, friendly guide to building a minimal OS in C; the archived site of the littleosbook.
- [Writing a Simple Operating System — From Scratch (PDF)](https://www.cs.bham.ac.uk/~exr/teaching/lectures/opsys/2005_06/notes/OS3-BareMetal.pdf) — the classic University of Birmingham bare-metal PDF walkthrough by Nick Blundell.
- [Operating Systems: From 0 to 1 (tuhdo/os01)](https://github.com/tuhdo/os01) — starts you from assembly and brings you toward a working x86_64 kernel in pure C. Best-seller for beginners who like to read + code.
- [os01 — web edition](https://tuhdo.github.io/os01/) — the HTML-served version of the "From 0 to 1" book.

### Video courses/playlists
- [Write your own Operating System](https://www.youtube.com/playlist?list=PLHh55M_Kq4OApWScZyPl5HhgsTJS9MZ6M) — classic 28-video starter series piggybacking on the OSDev wiki bare-bones path.
- [Nanobyte — Building an OS (playlist)](https://www.youtube.com/playlist?list=PLFjM7v6KGMpiH2G-kT781ByCNC_0pKpPN) — end-to-end series: dev environment, bootloader, FAT filesystem, memory detection. Slow and thorough.
- [Write your own Operating System in 1 hour](https://www.youtube.com/watch?v=1rnA6wpF0o4) — Nanobyte's compressed crash course; great orientation before committing to a long series.

### Language-specific (C/C++/Rust/Go/C#)
- [Learn-C.org](https://www.learn-c.org/) — interactive, browser-based C tutorial; start here if you've never written C.
- [freeCodeCamp: C Programming Handbook](https://www.freecodecamp.org/news/the-c-beginners-handbook/) — thorough written walkthrough of C for absolute beginners.
- [CS50x: Introduction to Computer Science (Harvard)](https://cs50.harvard.edu/x/) — its C weeks are the fastest way to learn proper C from scratch.
- [Learn C++ (learncpp)](https://www.learncpp.com/) — widely considered the best free C++ tutorial for beginners.
- [A Tour of Go](https://go.dev/tour) — the official interactive introduction to Go; start here for the Go OS-dev route.
- [C# Guide (Microsoft Learn)](https://learn.microsoft.com/en-us/dotnet/csharp/) — official C# documentation; canonical course for learning C# before Cosmos.
- [The Rust Programming Language ("The Book")](https://doc.rust-lang.org/book/) — the official free Rust book; read cover to cover as your foundation.

### Architecture (x86/RISC-V/ARM)
- [Ben Eater](https://www.youtube.com/@BenEater) — builds an 8-bit computer and a 6502 machine on breadboards; teaches digital logic and assembly from the ground up. The essential mental model for OS dev.
- [Crash Course Computer Science](https://www.youtube.com/@crashcourse) — 40-episode intro; episodes on logic gates, memory, CPUs, and operating systems are ideal warm-ups.
- [Assembly (OSDev Wiki)](https://wiki.osdev.org/Assembly) — getting started with x86 assembly in an OS context.
- [x86-64 (Wikipedia)](https://en.wikipedia.org/wiki/X86-64) — AMD64/Intel 64 overview, long mode, and the 64-bit programming model.

---

## Beginner-Intermediate

*Assumes: you have booted a bare-bones kernel and gotten "Hello, world" on screen. Goal: understand the boot path, segmentation (GDT), interrupts (IDT), and write a working shell.*

### OSDev tutorials/series
- [OSDev Wiki — Tutorials Index](https://wiki.osdev.org/Tutorials) — hub for all the wiki's guided tutorials, from GDT to VGA and beyond.
- [OSDev Wiki — Meaty Skeleton](https://wiki.osdev.org/Meaty_Skeleton) — a clean, well-organized template OS with a kernel/libk split to copy.
- [OSDev Wiki — GCC Cross-Compiler](https://wiki.osdev.org/GCC_Cross-Compiler) — building the cross-compiler you need before serious bare-metal work.
- [OSDev Wiki — Going Further on x86](https://wiki.osdev.org/Going_Further_on_x86) — the boot sequence and the path past bare bones (including Multiboot).
- [OSDev Wiki — GDT Tutorial](https://wiki.osdev.org/GDT_Tutorial) — the Global Descriptor Table and entering protected mode.
- [OSDev Wiki — Roll Your Own Bootloader](https://wiki.osdev.org/Roll_Your_Own_Bootloader) — crafting a bootloader from scratch (after Meaty Skeleton).
- [Writing an OS in Rust (phil-opp)](https://os.phil-opp.com/) — the flagship Rust OS series: freestanding binary → vga → interrupts → paging → heap → multitasking. Gentler than it looks early on.
- [phil-opp/blog_os source](https://github.com/phil-opp/blog_os) — the complete companion source for the Rust series.
- [Nanobyte "Building an OS" YouTube series](https://www.youtube.com/playlist?list=PL2EFpV2KRMAoHmzi4x7dWnZ8zH8Q5vRJl) — build your own OS and bootloader from scratch, from floppy hello-world upward.
- [BrokenThorn OS Development Series](http://www.brokenthorn.com/Resources/OSDevIndex.html) — a step-by-step series from bootloader to a fully working kernel and filesystem.

### Books
- [Operating Systems: From 0 to 1 (tuhdo/os01)](https://github.com/tuhdo/os01) — if you worked through the first chapters at Beginner, continue here through linking/loading and x86_64 kernel setup.
- [os01 — web edition](https://tuhdo.github.io/os01/) — the HTML version of the same book.

### Video courses/playlists
- [Nanobyte — Building an OS](https://www.youtube.com/playlist?list=PLFjM7v6KGMpiH2G-kT781ByCNC_0pKpPN) — continue deeper into the bootloader and kernel steps.
- [Nanobyte (@NanobyteDev)](https://www.youtube.com/@NanobyteDev) — the channel behind the series; long, thorough walks.

### Language-specific
- [OSDev Wiki: C](https://wiki.osdev.org/C) — language-specific guidance, freestanding details and gotchas for writing C kernels.
- [OSDev Wiki: C++](https://wiki.osdev.org/C%2B%2B) — C++ guidance: freestanding headers, globals/DWARF gotchas, new/delete and exceptions in-kernel.
- [OSDev Wiki: Rust](https://wiki.osdev.org/Rust) — Rust-specific OS-dev guidance (targets, crates, pitfalls).
- [The Embedded Rust Book](https://docs.rust-embedded.org/book/) — official intro to Rust on microcontrollers; covers the `no_std` ecosystem you'll use in a kernel.
- [Go Bare Bones (OSDev Wiki)](https://wiki.osdev.org/Go_Bare_Bones) — booting a Go kernel (multiboot + a `noos` freestanding harness).
- [Bare Bones (C++)](https://wiki.osdev.org/Bare_Bones_C%2B%2B) — the canonical C++ minimal kernel.

### Architecture
- [OSDev Wiki — x86](https://wiki.osdev.org/X86) — index of x86 articles (modes, GDT, IDT, ports, paging).
- [Protected mode (Wikipedia)](https://en.wikipedia.org/wiki/Protected_mode) — the x86 32-bit privileged mode.
- [Long mode (Wikipedia)](https://en.wikipedia.org/wiki/Long_mode) — 64-bit mode with flat segmentation + mandatory paging.
- [x86-64 — OSDev Wiki](https://wiki.osdev.org/X86-64) — how to enable long mode, GDT setup, code models.
- [RISC-V (Wikipedia)](https://en.wikipedia.org/wiki/RISC-V) — the open ISA used by xv6, rCore, and many teaching kernels.

---

## Intermediate

*Assumes: you can boot a real kernel with interrupts and paging set up. Goal: write a usable kernel — a working shell, physical/virtual memory management, and your first drivers.*

### OSDev tutorials/series
- [James Molloy's Kernel Development Tutorials](http://www.jamesmolloy.co.uk/tutorial_html/) — the famous old series (build a working shell/task preemption). Historic; expect bugs — great for concepts, not copy-paste.
- [cfenollosa/os-tutorial](https://github.com/cfenollosa/os-tutorial) — if you used it at Beginner, continue through its keyboard/disk/scheduling steps to a simple shell.
- [David Callanan / CodePulse — Write Your Own 64-bit OS Kernel](https://github.com/davidcallanan/os-series) — the repo companion to CodePulse's polished C/assembly 64-bit kernel series.
- [Poncho OSDev series code (Jmallone/os-dev)](https://github.com/Jmallone/os-dev) — community companion code for Poncho's videos (#2–#25).
- [Writing an OS in Rust (phil-opp)](https://os.phil-opp.com/) — push through its paging, heap, and multitasking chapters here.
- [rust-osdev/bootloader](https://github.com/rust-osdev/bootloader) — the reusable Rust bootloader used by the phil-opp series.

### Books
- [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) — the famous free textbook on OS concepts (virtualization, concurrency, persistence). The conceptual companion to everything you write here.
- [OSTEP projects repo](https://github.com/remzi-arpacidusseau/ostep-projects) — coding projects that go with OSTEP.

### Video courses/playlists
- [Write Your Own 64-bit Operating System Kernel From Scratch](https://www.youtube.com/playlist?list=PLZQftyCk7_SeZRitx5MjBKzTtvk0pHMtp) — CodePulse/David; boots with Multiboot and builds up a 64-bit kernel.
- [Poncho — OS Dev Season 1](https://www.youtube.com/playlist?list=PLxN4E629pPnJxCQCLy7E0SQY_zuumOVyZ) — a well-liked 64-bit OS-from-scratch series (C++ and graphics).
- [OS Dev – S2 (David Callanan)](https://www.youtube.com/playlist?list=PLxN4E629pPnJxCQCLy7E0SQY_zuumOVyZ) — part two of the how-to-make-an-OS series: graphics, C++, and the kernel.

### Language-specific
- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) — official book on *unsafe* Rust — essential for low-level/kernel work.
- [rust-osdev/x86_64](https://github.com/rust-osdev/x86_64) — the low-level x86_64 crate (paging, interrupts, GDT/IDT, port I/O).
- [A Tutorial on Pointers and Arrays in C (Ted Jensen / ptrtut13)](https://github.com/jflaherty/ptrtut13) — the famous multi-part pointer tutorial — pointer mastery directly relevant to writing kernel structures.
- [C++ in Kernel Development — A Comprehensive Guide](https://dev.to/trish_07/c-in-kernel-development-a-comprehensive-guide-564d) — practical article on writing C++ kernel code (freestanding, linking, portability).
- [FontaineOS](https://github.com/alistairfontaine/FontaineOS) — a lightweight freestanding C++20 x86 kernel built directly on registers and VGA with zero stdlib — ideal minimal C++ kernel example.

### Architecture
- [OSDev Wiki — Paging](https://wiki.osdev.org/Paging) — page tables, the MMU, and virtual→physical translation.
- [OSDev Wiki — Memory Management](https://wiki.osdev.org/Memory_Management) — terminology and structure for managing RAM.
- [OSDev Wiki — Interrupts](https://wiki.osdev.org/Interrupts) — the IDT, exceptions, IRQs, and the interrupt lifecycle.
- [OSDev Wiki — The PIC (8259A)](https://wiki.osdev.org/Programmable_Interrupt_Controller) — the legacy interrupt controller you remap early on.
- [OSDev Wiki — VGA Hardware](https://wiki.osdev.org/VGA_Hardware) — text-mode and framebuffer graphics programming.
- [OSDev Wiki — Getting Keyboard Input](https://wiki.osdev.org/Getting_Keyboard_Input) — reading the keyboard controller / PS2 scancodes.
- [OSDev Wiki — Memory Mapped I/O](https://wiki.osdev.org/Memory_Mapped_IO) — MMIO vs port I/O.

---

## Intermediate-Hard

*Assumes: you have a running kernel with memory management, interrupts, and a console. Goal: add processes/threads, a scheduler, system calls, and a real filesystem — the core of a "real" OS.*

### OSDev tutorials/series
- [James Molloy's Kernel Development Tutorials](http://www.jamesmolloy.co.uk/tutorial_html/) — its task-switching/preemption half lives here (user mode, VFS).
- [BrokenThorn OS Development Series](http://www.brokenthorn.com/Resources/OSDevIndex.html) — the later stages build a full working kernel, filesystem, and memory manager.
- [Bran's Kernel Development Tutorial](https://www.osdever.net/bkerndev/Docs/title.htm) — classic C kernel tutorial (GDT/IDT, ISRs, paging); many hobbyists start midway here.
- [MIT 6.828 / 6.S081 — Operating System Engineering (xv6)](https://pdos.csail.mit.edu/6.828/) — build the small xv6 kernel; MIT's legendary OS course. The best structured way to hit this tier.
- [xv6-public source (mit-pdos)](https://github.com/mit-pdos/xv6-public) — the clean, readable Unix-like teaching kernel source.
- [xv6 book (rev11, PDF)](https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf) — the concise xv6 "RISC-V book" explaining the kernel line by line.
- [Princeton COS 318 — Operating Systems](https://www.cs.princeton.edu/courses/archive/fall18/cos318/) — archived OS course with labs and lecture notes.
- [Rice COMP 310 — Operating Systems](https://www.clear.rice.edu/comp310/) — a classic OS course with a famously fun choice of projects.

### Books
- [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) — the scheduling/process/virtualization chapters map directly onto this tier.
- [xv6 book (PDF)](https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf) — free manual for a tiny real teaching OS; read alongside the source.
- [Operating Systems: Three Easy Pieces — homework div](https://github.com/remzi-arpacidusseau/ostep-homework) — the homework/labs associated with OSTEP.

### Video courses/playlists
- [MIT 6.S081 / xv6 talk material via the course](https://pdos.csail.mit.edu/6.828/) — lecture videos & labs for a full OS course.
- [ops-class live lecture videos](https://www.ops-class.org/) — recorded, self-paced OS lectures (SUNY Buffalo full course).
- [hhp3 (Harry Porter)](https://www.youtube.com/@hhp3) — professor-level walkthroughs of the MIT xv6 kernel (RISC-V) and RISC-V architecture.

### Language-specific
- [rCore-Tutorial-v3](https://github.com/rcore-os/rCore-Tutorial-v3) — Tsinghua's famous course: write a RISC-V OS in Rust from scratch — a complete, tested teaching kernel with docs.
- [rust-embedded/rust-raspberrypi-OS-tutorials](https://github.com/rust-embedded/rust-raspberrypi-OS-tutorials) — a complete OS-dev series for the Raspberry Pi in safe Rust (great ARM alternative to the x86 blog).
- [The Rust Unsafe Code Guidelines (UCG)](https://github.com/rust-lang/unsafe-code-guidelines) — defines exactly what unsafe Rust can and can't guarantee — critical reading at this tier.
- [Rust Atomics and Locks (Mara Bos)](https://marabos.nl/atomics/) — free book on Rust concurrency: atomics, mutexes, channels, lock-free structures — directly relevant to a multi-core kernel.

### Architecture
- [OSDev Wiki — Processes and Threads](https://wiki.osdev.org/Processes_and_Threads) — the difference and how to model them.
- [OSDev Wiki — Scheduling Algorithms](https://wiki.osdev.org/Scheduling_Algorithms) — round-robin, priorities, and friends.
- [OSDev Wiki — Context Switching](https://wiki.osdev.org/Context_Switching) — saving/restoring CPU state between tasks.
- [OSDev Wiki — System Calls](https://wiki.osdev.org/System_Calls) — the interface between user code and the kernel.
- [OSDev Wiki — File Systems](https://wiki.osdev.org/File_Systems) — how to design and implement an FS.
- [OSDev Wiki — APIC & Local APIC](https://wiki.osdev.org/APIC) — modern interrupt routing for SMP.

---

## Hard

*Assumes: you have a multi-process kernel with scheduling, system calls, and a filesystem. Goal: production-ish subsystems — real device drivers, SMP/multicore, paging-heavy virtual memory, a microkernel design — and studying what real kernels look like.*

### OSDev tutorials/series
- [OSDev Wiki — Inter-Processor Interrupts (IPI)](https://wiki.osdev.org/IPI) — sending interrupts between cores for SMP.
- [OSDev Wiki — Multiprocessor Scheduling](https://wiki.osdev.org/Multiprocessor_Scheduling) — scheduling across multiple cores.
- [OSDev Wiki — SMP](https://wiki.osdev.org/SMP) — symmetric multiprocessing boot and coordination.
- [OSDev Wiki — Memory Allocation](https://wiki.osdev.org/Memory_Allocation) — heap allocators and why they matter.
- [OSDev Wiki — Page Frame Allocation](https://wiki.osdev.org/Page_Frame_Allocation) — physical-memory frame managers.
- [Operating Systems: From 0 to 1 (tuhdo/os01)](https://github.com/tuhdo/os01) — its advanced chapters (USB, multitasking) sit here; read once you're past the beginner bootstrapping.
- [Osdev-Notes (dreamportdev)](https://github.com/dreamportdev/Osdev-Notes) — highly detailed, well-structured notes on x86 OS development — a great hard-tier reference.

### Books
- [linux-insides (0xAX)](https://github.com/0xAX/linux-insides) — a book explaining the Linux kernel boot internals in detail.
- [linux-insides — web edition](https://0xax.gitbooks.io/linux-insides/content/) — the same Linux-internals book rendered as a readable GitBook.
- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/) — official Linux kernel docs (process, admin, driver & core API).
- [The Lost Art of Structure Packing (Eric S. Raymond)](https://www.catb.org/esr/structure-packing/) — struct layout/padding for memory-efficient kernel structures.

### Video courses/playlists
- [Andreas Kling](https://www.youtube.com/andreaskling) — SerenityOS creator's sessions building and explaining OS internals at production scale.
- [Low Level Learning](https://www.youtube.com/@LowLevelTV) — low-level / systems programming, reverse engineering, bare-metal explainers.
- [NCommander](https://www.youtube.com/@NCommander) — OS archaeology and reverse engineering (bootstrapping old toolchains, kernel history).

### Language-specific
- [Rust for Linux (kernel)](https://github.com/Rust-for-Linux/linux) — the effort adding Rust as a second kernel language in Linux — the most realistic large-scale demonstration of systems Rust.
- [Theseus OS](https://github.com/theseus-os/Theseus) — a research OS in Rust built around cell/state-based isolation — advanced reading for how far Rust OS design can go.
- [The Rust Performance Book](https://nnethercote.github.io/perf-book/) — practical advice on making Rust fast — useful for squeezing your kernel's hot paths.
- [thor-os (C++)](https://github.com/wichtounet/thor-os) — a C++ operating system (bootloader, GUI, drivers) as a reference project.
- [Cosmos (C# OS kit)](https://github.com/CosmosOS/Cosmos) — a C# operating-system toolkit; the IL2CPU compiler turns C# IL into native code.
- [IL2CPU (CosmosOS)](https://github.com/CosmosOS/IL2CPU) — the C#→native AOT compiler behind every Cosmos kernel.
- [Cosmos — Write an OS in modern C#](https://www.gocosmos.org/) — official site for the C#/managed OS construction kit.
- [go-dav-os](https://github.com/dmarro89/go-dav-os) — a hobby OS kernel written in Go.
- [eggos — a Go unikernel](https://github.com/alexflint/eggos) — a small OS written in Go that runs Go programs.

### Architecture
- [OSDev Wiki — Going Further on x86](https://wiki.osdev.org/Going_Further_on_x86) — the path past bare bones into serious subsystem work.
- [Agner Fog's optimization resources](https://www.agner.org/optimize/) — authoritative manuals on x86 microarchitecture.
- [OSDev Wiki — Resources page](https://wiki.osdev.org/Resources) — hundreds of hardware datasheets and specifications for real driver work.
- [MIT 6.172 Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/) — how CPU/memory actually behave under real code (cache misses, vectorization).

---

## Very Hard

*Assumes: you are comfortable reading large OS codebases and papers. Goal: advanced systems design — microkernels, formal verification, compiler-driven OS structure, and industrial-scale real-world kernels. These are study targets; treat them as reference material rather than "follow along" tutorials.*

### OSDev tutorials/series
- [The Linux Kernel "How to" (development process)](https://www.kernel.org/doc/html/latest/process/howto.html) — how the kernel is actually developed and how to contribute.
- [The Linux source (torvalds/linux)](https://github.com/torvalds/linux) — the kernel itself, the ultimate read-only reference.

### Books
- [linux-insides (0xAX)](https://github.com/0xAX/linux-insides) — deep Linux kernel boot & internals book.

### Video courses/playlists
- [Developed From Scratch](https://www.youtube.com/@DevelopedFromScratch) — live dev streams building an OS, a compiler, and a build system entirely from scratch.
- [Olivier — Creating My Own Operating System](https://www.youtube.com/watch?v=eys5TpLWdgQ) — a candid, low-level live attempt at an OS from scratch.

### Language-specific
- [Theseus OS](https://github.com/theseus-os/Theseus) — intralingual design: shifting OS responsibilities into the compiler/Rust's type system. Research-grade.
- [Redox OS](https://github.com/Redox-os/redox) — the best-known general-purpose Rust OS; microkernel + userspace, a full real-world example of large-scale system Rust.
- [SerenityOS](https://github.com/SerenityOS/serenity) — an ambitious, Unix-like, graphical OS in modern C++ with a browser, ports, drivers, and fuzzing — a huge real-world corpus.
- [gVisor (Google)](https://github.com/google/gvisor) — a user-space kernel and sandbox written entirely in Go, implementing the Linux syscall ABI — an outstanding large-scale example of "an OS in Go".
- [Compiler (Wikipedia)](https://en.wikipedia.org/wiki/Compiler) — the compiler/ABI angle intersects advanced kernel work; pair with the hub's compiler-tooling channels (Matt Godbolt, CppCon) listed in videos.md.

### Architecture
- [RISC-V ISA Specifications](https://riscv.org/technical/specifications/) — the free, open standard ISA with ratified unprivileged & privileged specs.
- [Intel® 64 and IA-32 Architectures Software Developer's Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) — the full multi-volume x86 reference (Vol 3 system programming guide in particular).
- [System V AMD64 ABI](https://gitlab.com/x86-psABIs/x86-64-ABI) — the canonical spec for registers, calling conventions, and ELF on x86-64.
- [MIT 6.004: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) — how digital systems and processors are built, from transistors to RISC-V.

---

## Beyond the ladder — where to keep going next

Once you can place yourself on this ladder, the trick is not running out of material but knowing **what the next level actually requires**. Each tier above links forward to the next. When you finish a tier, re-read the "How to use this ladder" note, pick the next lane, and move up one rung — the hub's other curated pages (os-development.md, videos.md, language-*.md, computer-architecture.md) carry the full, un-tiered versions of all these resources plus the deep-dive links referenced above.

*Longest-running companion: [OSDev Forum](https://forum.osdev.org/) — read threads at your level, ask focused questions, and never be afraid to have your design choices critiqued. It's where every serious OSdev eventually learns the discipline.*
