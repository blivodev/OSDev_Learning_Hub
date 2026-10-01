# Operating System Development — Curated Resources

A long, categorized, verified list of free OS-development material: wikis, from-scratch tutorials, books, bootloader/bare-bones guides, deep kernel topics, and video channels/playlists. Every link below was verified reachable at curation time.

## General OS-dev wikis & guides

### The canonical wiki
- [OSDev Wiki (Expanded Main Page)](https://wiki.osdev.org/Main_Page) — *the* community reference: 700+ articles on everything from first boot to full kernel design.
- [OSDev Wiki — Getting Started](https://wiki.osdev.org/Getting_Started) — the recommended first page; prerequisite knowledge and a reading order.
- [OSDev Wiki — Required Knowledge](https://wiki.osdev.org/Required_Knowledge) — what you should know before starting (C, assembly, PC architecture).
- [OSDev Wiki — Beginner Mistakes](https://wiki.osdev.org/Beginner_Mistakes) — the classic pitfalls every new OSdev hits, and how to avoid them.
- [OSDev Wiki — Tutorials Index](https://wiki.osdev.org/Tutorials) — hub for all the wiki's guided tutorials, from GDT to VGA and beyond.
- [OSDev Wiki — Expanded Main Page](https://wiki.osdev.org/Expanded_Main_Page) — the long-form wiki front page covering every subsystem.
- [OSDev Forum](https://forum.osdev.org/) — the community Q&A board (200k+ posts); the best place to get help from experienced devs.
- [OSDev Wiki — Books on OS Development](https://wiki.osdev.org/Books) — the wiki's own curated list of OS-dev books and academic references.

### Project templates & skeletons
- [OSDev Wiki — Meaty Skeleton](https://wiki.osdev.org/Meaty_Skeleton) — a clean, well-organized template OS with a kernel/libk split to copy.
- [OSDev Wiki — Bare Bones](https://wiki.osdev.org/Bare_Bones) — the canonical minimal 32-bit C kernel booted by GRUB + Multiboot.
- [OSDev Wiki — Bare Bones (C++)](https://wiki.osdev.org/Bare_Bones_C%2B%2B) — same minimal kernel written in C++.
- [OSDev Wiki — Go Bare Bones](https://wiki.osdev.org/Go_Bare_Bones) — minimal kernel stub for the Go language.
- [OSDev Wiki — Raspberry Pi Bare Bones](https://wiki.osdev.org/Raspberry_Pi_Bare_Bones) — get a kernel running on bare-metal ARM (Pi).
- [OSDev Wiki — Limine Bare Bones](https://wiki.osdev.org/Limine_Bare_Bones) — modern 64-bit higher-half kernel booted with the Limine protocol.
- [OSDev Wiki — Stivale Bare Bones](https://wiki.osdev.org/Stivale_Bare_Bones) — a 64-bit higher-half kernel using the stivale boot protocol.
- [OSDev Wiki — Higher Half Bare Bones](https://wiki.osdev.org/Higher_Half_Bare_Bones) — kernel mapped into the upper virtual address range.

### Aggregated link-lists ("awesome" style)
- [leap0x7b/awesome-osdev](https://github.com/leap0x7b/awesome-osdev) — a curated list of OS-dev tutorials, projects, bootloaders, and libraries.
- [devse-org/awesome-osdev](https://github.com/devse-org/awesome-osdev) — another great OS-dev resource list (tutorials, courses, manuals, videos).
- [Osdev-Notes (dreamportdev)](https://github.com/dreamportdev/Osdev-Notes) — highly detailed, well-structured notes on x86 OS development.

## Full "OS from scratch" tutorials & series

### Classic beginner C series
- [James Molloy's Kernel Development Tutorials](http://www.jamesmolloy.co.uk/tutorial_html/) — the famous old 3-part series (build a working shell/task preemptives). Historic; expect bugs — great for concepts, not copy-paste.
- [BrokenThorn OS Development Series](http://www.brokenthorn.com/Resources/OSDevIndex.html) — a step-by-step series from bootloader to a fully working kernel and filesystem.
- [cfenollosa/os-tutorial](https://github.com/cfenollosa/os-tutorial) — "How to create an OS from scratch": short, incremental READMEs from boot sector to a simple shell (no GRUB).
- [Writing a Simple Operating System — From Scratch (PDF)](https://www.cs.bham.ac.uk/~exr/teaching/lectures/opsys/2005_06/notes/OS3-BareMetal.pdf) — the classic University of Birmingham bare-metal PDF walkthrough by Nick Blundell.
- [The Little OS Book](https://littleosbook.github.io/) — a concise, friendly guide to building a minimal OS in C; the archived site of the littleosbook.

### os01 & bare-metal C
- [Operating Systems: From 0 to 1 (tuhdo/os01)](https://github.com/tuhdo/os01) — a celebrated free book bootstrapping you from assembly to a working x86_64 kernel in pure C.
- [os01 — web edition (tuhdo.github.io)](https://tuhdo.github.io/os01/) — the HTML-served version of the same "From 0 to 1" book.

### Modern video-led series
- [David Callanan / CodePulse — Write Your Own 64-bit OS Kernel](https://github.com/davidcallanan/os-series) — the repo companion to CodePulse's polished C/assembly 64-bit kernel series.
- [Nanobyte "Building an OS" YouTube series](https://www.youtube.com/playlist?list=PL2EFpV2KRMAoHmzi4x7dWnZ8zH8Q5vRJl) — build your own OS and bootloader from scratch, from floppy hello-world upward.
- [Nanobyte — building-an-os example code (nanobyte_os)](https://github.com/nanobyte-dev/nanobyte_os) — the complete source for Nanobyte's video series with build scripts.
- [Nanobyte's site/devlog](https://nanobyte.dev/) — Nanobyte's own site with transcripts and extra material for the series.
- [Poncho — OS Development Season 1](https://www.youtube.com/playlist?list=PLxN4E629pPnJxCQCLy7E0SQY_zuumOVyZ) — a well-liked 64-bit OS-from-scratch series.
- [Poncho OSDev series code (Jmallone/os-dev)](https://github.com/Jmallone/os-dev) — community companion code for Poncho's videos (videos #2–#25).

### Rust / modern-language series
- [Writing an OS in Rust (phil-opp)](https://os.phil-opp.com/) — the flagship Rust OS series: freestanding binary → vga → interrupts → paging → heap → multitasking.
- [phil-opp/blog_os source](https://github.com/phil-opp/blog_os) — the complete source code for the "Writing an OS in Rust" series.
- [rust-osdev/bootloader](https://github.com/rust-osdev/bootloader) — a reusable Rust bootloader used by the phil-opp series.
- [rust-osdev/uart_16550](https://github.com/rust-osdev/uart_16550) — tiny Rust crate for serial-port output, handy for kernel logging.

### Go, C++, and other languages
- [eggos — a Go unikernel](https://github.com/alexflint/eggos) — a small operating system written in Go that runs Go programs.
- [go-dav-os](https://github.com/dmarro89/go-dav-os) — a hobby OS kernel written in Go.
- [thor-os (C++)](https://github.com/wichtounet/thor-os) — a C++ operating system (bootloader, GUI, drivers) as a reference project.
- [Cosmos (C# OS kit)](https://github.com/CosmosOS/Cosmos) — a C# operating-system toolkit (see also gocosmos.org).

### Linux kernel docs & internals (for the "real OS" angle)
- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/) — the official Linux kernel docs (process, admin, driver & core API).
- [The Linux Kernel "How to" (development process)](https://www.kernel.org/doc/html/latest/process/howto.html) — how the kernel is actually developed and how to contribute.
- [linux-insides (0xAX)](https://github.com/0xAX/linux-insides) — a book explaining the Linux kernel boot internals in detail.
- [linux-insides — web edition](https://0xax.gitbooks.io/linux-insides/content/) — the same Linux-internals book rendered as a readable GitBook.
- [The Linux source (torvalds/linux)](https://github.com/torvalds/linux) — the kernel itself, the ultimate read-only reference.

### University / embedded-style tutorials
- [MIT 6.828 / 6.S081 — Operating System Engineering (xv6)](https://pdos.csail.mit.edu/6.828/) — build the small xv6 kernel; MIT's legendary OS course.
- [xv6-public source (mit-pdos)](https://github.com/mit-pdos/xv6-public) — the clean, readable Unix-like teaching kernel source.
- [xv6 book (rev11, PDF)](https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf) — the concise xv6 "RISC-V book" explaining the kernel line by line.
- [Princeton COS 318 — Operating Systems](https://www.cs.princeton.edu/courses/archive/fall18/cos318/) — archived OS course with labs and lecture notes.
- [Rice COMP 310 — Operating Systems](https://www.clear.rice.edu/comp310/) — a classic OS course with a famously fun choice of projects.
- [ops-class.org](https://www.ops-class.org/) — a complete, self-paced OS course with videos, slides, and projects from SUNY Buffalo.
- [Core OS (skyzh) — a tiny RISC-V OS & teaching repo](https://github.com/skyzh/core-os-riscv) — a minimal RISC-V OS and its book, great for ARM/RISC-V learners.

## Books (free / online)

### Classic concept books
- [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) — the famous free textbook on OS concepts (virtualization, concurrency, persistence) by Remzi & Andrea Arpaci-Dusseau.
- [OSTEP projects repo](https://github.com/remzi-arpacidusseau/ostep-projects) — coding projects that go with OSTEP.
- [OSTEP homework repo](https://github.com/remzi-arpacidusseau/ostep-homework) — the homework/labs associated with OSTEP.

### OS-dev specific books
- [The Little OS Book (site)](https://littleosbook.github.io/) — free, short book that takes you from zero to a running kernel in C.
- [Operating Systems: From 0 to 1 (tuhdo)](https://github.com/tuhdo/os01) — the free self-learner's book (assembly → ELF → x86_64 kernel).
- [Writing a Simple OS — From Scratch (PDF)](https://www.cs.bham.ac.uk/~exr/teaching/lectures/opsys/2005_06/notes/OS3-BareMetal.pdf) — University of Birmingham's free bare-metal PDF tutorial.
- [linux-insides](https://github.com/0xAX/linux-insides) — free book on Linux kernel boot & internals.
- [xv6 book (PDF)](https://pdos.csail.mit.edu/6.828/2018/xv6/book-rev11.pdf) — free manual for a tiny real teaching OS.

## Bootloader & Multiboot resources

- [OSDev Wiki — Bootloader](https://wiki.osdev.org/Bootloader) — theory and practice of writing your own bootloader.
- [OSDev Wiki — Roll Your Own Bootloader](https://wiki.osdev.org/Roll_Your_Own_Bootloader) — a full walkthrough of crafting a bootloader from scratch.
- [OSDev Wiki — GDT Tutorial](https://wiki.osdev.org/GDT_Tutorial) — the Global Descriptor Table and entering protected mode.
- [OSDev Wiki — Going Further on x86](https://wiki.osdev.org/Going_Further_on_x86) — the boot sequence and the path past bare bones (including Multiboot).
- [OSDev Wiki — GCC Cross-Compiler](https://wiki.osdev.org/GCC_Cross-Compiler) — building the cross-compiler you need before any bare-metal work.
- [Limine bootloader](https://github.com/limine-bootloader/limine) — a modern, advanced multiprotocol bootloader (Multiboot 2, stivale).
- [Limine official site](https://limine-bootloader.org/) — Limine's homepage with docs and downloads.
- [GRUB — GNU bootloader](https://www.gnu.org/software/grub/) — the free GRand Unified Bootloader used by most OS-dev tutorials.
- [QEMU emulator](https://www.qemu.org/) — the key testing tool: boot your kernel without rebooting.
- [NASM assembler](https://www.nasm.us/) — the low-level assembler used across nearly every OS-dev tutorial.

## Kernel development topics (deep dives)

### Memory, paging & virtual memory
- [OSDev Wiki — Paging](https://wiki.osdev.org/Paging) — page tables, the MMU, and virtual→physical translation.
- [OSDev Wiki — Memory Management](https://wiki.osdev.org/Memory_Management) — terminology and structure for managing RAM.
- [OSDev Wiki — Memory Allocation](https://wiki.osdev.org/Memory_Allocation) — heap allocators and why they matter for a kernel.
- [OSDev Wiki — Page Frame Allocation](https://wiki.osdev.org/Page_Frame_Allocation) — physical-memory frame managers.

### Interrupts, PIT & PIC/APIC
- [OSDev Wiki — Interrupts](https://wiki.osdev.org/Interrupts) — the IDT, exceptions, IRQs, and the interrupt lifecycle.
- [OSDev Wiki — The PIC (8259A)](https://wiki.osdev.org/Programmable_Interrupt_Controller) — the legacy interrupt controller you remap early on.
- [OSDev Wiki — APIC & Local APIC](https://wiki.osdev.org/APIC) — modern interrupt routing for SMP.
- [OSDev Wiki — 8253/8254 PIT](https://wiki.osdev.org/Programmable_Interval_Timer) — the timer chip that drives scheduling.
- [OSDev Wiki — Getting Keyboard Input](https://wiki.osdev.org/Getting_Keyboard_Input) — reading the keyboard controller / PS2 scancodes.
- [OSDev Wiki — Inter-Processor Interrupts (IPI)](https://wiki.osdev.org/IPI) — sending interrupts between cores for SMP.

### Scheduling, processes & threads
- [OSDev Wiki — Processes and Threads](https://wiki.osdev.org/Processes_and_Threads) — the difference and how to model them.
- [OSDev Wiki — Scheduling Algorithms](https://wiki.osdev.org/Scheduling_Algorithms) — round-robin, priorities, and friends.
- [OSDev Wiki — Context Switching](https://wiki.osdev.org/Context_Switching) — saving/restoring CPU state between tasks.
- [OSDev Wiki — Multiprocessor Scheduling](https://wiki.osdev.org/Multiprocessor_Scheduling) — scheduling across multiple cores.
- [OSDev Wiki — SMP](https://wiki.osdev.org/SMP) — symmetric multiprocessing boot and coordination.
- [OSDev Wiki — System Calls](https://wiki.osdev.org/System_Calls) — the interface between user code and the kernel.

### Drivers, filesystems & hardware
- [OSDev Wiki — VGA Hardware](https://wiki.osdev.org/VGA_Hardware) — text-mode and framebuffer graphics programming.
- [OSDev Wiki — File Systems](https://wiki.osdev.org/File_Systems) — how to design and implement an FS.
- [OSDev Wiki — Memory Mapped I/O](https://wiki.osdev.org/Memory_Mapped_IO) — MMIO vs port I/O for talking to hardware.
- [OSDev Wiki — Serial ports / debugging](https://wiki.osdev.org/Troubleshooting) — using serial output to debug a kernel.
- [OSDev Wiki — Resources page](https://wiki.osdev.org/Resources) — hundreds of hardware datasheets and specifications.

### Real-world open-source kernels to study
- [SerenityOS](https://github.com/SerenityOS/serenity) — an ambitious Unix-like OS with a friendly community and rich codebase.
- [managarm](https://github.com/managarm/managarm) — a pragmatic microkernel-based OS with async I/O.
- [ToaruOS](https://github.com/klange/toaruos) — a from-scratch hobby OS with bootloader, kernel, driver, and GUI.
- [xv6 (mit-pdos)](https://github.com/mit-pdos/xv6-public) — the MIT teaching kernel, ideal for study.
- [eggOS (Go)](https://github.com/icexin/eggos) — a unikernel/OS written in Go.
- [MaslOS (C++)](https://github.com/marceldobehere/maslos) — a hobby C++ OS, bootstrapped from Poncho's guide, showcases how tutorials evolve.

## YouTube channels & playlists

### Whole channels dedicated to OS dev / systems
- [Nanobyte (@NanobyteDev)](https://www.youtube.com/@NanobyteDev) — long, thorough OS-from-scratch series; one of the best modern walks.
- [CodePulse](https://www.youtube.com/@CodePulse) — the channel behind David Callanan's "Write your own 64-bit OS Kernel" series.
- [Andreas Kling](https://www.youtube.com/andreaskling) — SerenityOS creator's stream/videos building and explaining OS internals.
- [Low Byte Productions](https://www.youtube.com/@LowByteProductions) — low-level systems topics, including the excellent "How does an OS boot?".
- [Poncho](https://www.youtube.com/@poncho2364) — the OS-dev series channel for building a 64-bit OS and UEFI bootloader.

### Specific playlists worth following
- [Nanobyte — Building an OS (playlist)](https://www.youtube.com/playlist?list=PL2EFpV2KRMAoHmzi4x7dWnZ8zH8Q5vRJl) — the main from-scratch series playlist.
- [David Callanan / CodePulse — 64-bit OS (series)](https://www.youtube.com/playlist?list=PL56L8NZTl0bWDYxckPiSVdNhYNq_vJlvr) — the full polished 64-bit kernel series.
- [Poncho — OS Dev Season 1 (playlist)](https://www.youtube.com/playlist?list=PLxN4E629pPnJxCQCLy7E0SQY_zuumOVyZ) — Poncho's complete first-season playlist with companion code on GitHub.

### Talks & learning-oriented videos
- [MIT 6.S081 / xv6 talk material via the course](https://pdos.csail.mit.edu/6.828/) — lecture videos & labs for a full OS course.
- [ops-class live lecture videos](https://www.ops-class.org/) — recorded, self-paced OS lectures.

## Linux kernel internals (deep-dive resources)

- [Linux Kernel Newbies](https://kernelnewbies.org/) — a community wiki for aspiring kernel developers: tutorials, a first-patch guide, a kernel glossary, and subsystem documentation.
- [Kernelnewbies — LinuxChanges](https://kernelnewbies.org/LinuxChanges) — a human-readable changelog of what is new in every Linux kernel release.
- [Kernelnewbies — First Kernel Patch](https://kernelnewbies.org/FirstKernelPatch) — the canonical step-by-step "how to get your first patch merged" tutorial.
- [Lore — the Linux kernel mailing list archive](https://lore.kernel.org/lkml/) — the modern web + NNTP archive of every LKML message; read kernel code review as it happens.
- [The Linux Kernel Documentation (docs.kernel.org)](https://docs.kernel.org/) — the generated, always-current API and subsystem docs (a fuller index than the HTML "latest" mirror).
- [Linux Kernel docs — Locking](https://www.kernel.org/doc/html/latest/locking/index.html) — how the real kernel does concurrency: spinlocks, mutexes, rcu, semaphores, and lock ordering rules.
- [Linux Kernel docs — Core Kernel API](https://www.kernel.org/doc/html/latest/core-api/index.html) — the core API reference (memory allocation, workqueues, printing, kobject) every driver/kernel author uses.
- [Linux Kernel docs — License & Process rules](https://www.kernel.org/doc/html/latest/process/license-rules.html) — how kernel licensing works and the contribution process (DCO, subsystem maintainers).
- [Bootlin — Linux kernel & driver development course (free PDF slides)](https://bootlin.com/doc/training/linux-kernel/) — a complete, free, self-paced training course covering kernel interfaces, memory management, and driver fundamentals.
- [Bootlin — Embedded Linux system development course](https://bootlin.com/doc/training/embedded-linux/) — free course material on bootloaders, kernel configuration, cross-compilation, and device trees.
- [LWN.net — Kernel section](https://lwn.net/Kernel/) — LWN's kernel coverage: merge-window summaries and technical writeups of the latest kernel changes. (Weekly edition is reader-supported.)
- [Memfault Blog](https://www.memfault.com/blog) — a high-quality embedded/systems engineering blog; the "Interrupt" series (see the systems page) covers boot, linkers, and low-level debugging deeply.

## OS-dev blogs & newsletters

- [Interrupt — Memfault's engineering blog](https://interrupt.memfault.com/) — practical firmware/OS-dev posts: bootloaders, linker scripts, startup code, and debugging, all with working code.
- [Interrupt — "Zero to main()"](https://interrupt.memfault.com/blog/zero-to-main-1) — a famous deep dive into what actually runs before `main()` on an embedded target (reset, vector table, .data/.bss, stack setup).
- [Interrupt — How to write a bootloader from scratch](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch) — a grounded walkthrough of a real (non-x86) bootloader, useful conceptually for any architecture.
- [Interrupt — How to write linker scripts for firmware](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware) — the clearest practical explanation of GNU ld linker scripts (MEMORY, SECTIONS, symbols) — essential for placing a kernel.
- [cpu.land](https://cpu.land/) — a modern, friendly, visual guide to how a CPU actually executes code (smol bare-metal experiments in a browser VM). Great warm-up before real OSdev.
- [book-os.org](https://book-os.org/) — an open collaborative book on operating-system engineering with practical from-scratch projects.

## More "OS from scratch" series & projects (incl. UEFI / other ISAs)

- [MikanOS — uchan-nos/mikanos](https://github.com/uchan-nos/mikanos) — a complete educational UEFI-based 64-bit kernel (bootloader + kernel) with the celebrated Japanese book "Zero kara Wakaru OS Jisaku Nyumon" (ゼロからのOS自作入門).
- [MikanOS companion book — zero.osdev.jp](https://zero.osdev.jp/) — the free homepage for the book that builds MikanOS step by step (UEFI, paging, keyboard, graphics).
- [Core OS (skyzh) — a tiny RISC-V OS & teaching repo](https://github.com/skyzh/core-os-riscv) — a minimal RISC-V OS and its book, great for ARM/RISC-V learners.
- [jor1k — a JavaScript OpenRISC 1000 emulator running Linux in the browser](https://github.com/s-macke/jor1k) — watch an OS boot inside a web page; useful for studying boot, MMU, and drivers interactively.

## Books (more free/OS-dev focused)

- [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) — see the classics section; included here again as a reminder that its paging/virtualization chapters are the best free conceptual intro before writing a kernel.
- [xv6 book — mastering a tiny teaching Unix (MIT)](https://pdos.csail.mit.edu/6.S081/2020/xv6.html) — the free manual + annotated source for a real 6k-line kernel; the fastest route to "read a real OS."
- [MINIX 3 — operating-system source & book companion site](https://minix3.org/) — Amoeba/Tanenbaum lineage: a small, inspectable Unix-like OS plus its classic OS-design textbook resources.

---

*Maintained for the OSDev Learning Hub. Links verified September 2026; OSDev-wiki/forum/GRUB URLs return anti-bot HTTP 403 to scripts but are confirmed live in a browser and via content extraction.*
