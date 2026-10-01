# Rust — Curated Learning & OS-Dev Resources

Rust is arguably the most active language for modern hobby OS-dev, largely thanks to *Writing an OS in Rust* and the `no_std` ecosystem (bootloader, x86_64 crates, Theseus, Redox). These resources cover learning Rust through a systems lens and building kernels in it. All links verified reachable.

## The Rust Book & Official Learning
- **The Rust Programming Language ("The Book")** — https://doc.rust-lang.org/book/ — the official free book; read it cover to cover as your foundation.
- **Rust by Example** — https://doc.rust-lang.org/rust-by-example/ — hundreds of runnable examples; also on GitHub at https://github.com/rust-lang/rust-by-example.
- **The Rust Reference** — https://doc.rust-lang.org/reference/ — the official language reference for precise semantics — indispensable once you hit borrowed/unsafe edges.
- **The Rustonomicon** — https://doc.rust-lang.org/nomicon/ — the official book on *unsafe* Rust and advanced implementation details — essential for low-level/kernel work.
- **Rust Playground** — https://play.rust-lang.org/ — run and share Rust snippets in the browser while you learn.

## Intermediate & Systems-Focused Rust
- **Rust for Rustaceans** — https://rust-for-rustaceans.com/ — Jon Gjengset's book for experienced developers going deep on the language internals (also on No Starch: https://nostarch.com/rust-rustaceans).
- **The Rust Unsafe Code Guidelines (UCG)** — https://github.com/rust-lang/unsafe-code-guidelines — the working repository defining exactly what unsafe Rust can and can't guarantee — critical reading for writing kernels.

## Embedded / no_std Rust
- **The Embedded Rust Book** — https://docs.rust-embedded.org/book/ — official intro to Rust on microcontrollers; covers the `no_std` ecosystem you'll use in a kernel. Index: https://docs.rust-embedded.org/.
- **The Embedonomicon** — https://docs.rust-embedded.org/embedonomicon/ — the official deep dive into writing the lowest-level Rust (target specs, no_std startup, vectors) — directly applicable to OS-dev.
- **Discovery (rust-embedded)** — https://docs.rust-embedded.org/discovery/ — hands-on microcontroller discovery book for learning embedded Rust by doing.
- **rust-embedded/rust-raspberrypi-OS-tutorials** — https://github.com/rust-embedded/rust-raspberrypi-OS-tutorials — a complete, well-structured OS-dev tutorial series for the Raspberry Pi written in safe Rust (a great ARM alternative to the x86 blog).
- **Microsoft Rust Training: no_std — Rust Without the Standard Library** — https://microsoft.github.io/RustTraining/c-cpp-book/ch15-no_std-rust-without-the-standard-library.html — a clear chapter on what it means to write freestanding Rust.

## Writing an OS in Rust (the main series)
- **Writing an OS in Rust** — https://os.phil-opp.com/ — *the* canonical free x86 OS-dev tutorial in Rust, by Philipp Oppermann; covers freestanding binary, VGA, interrupts, paging, heap, async.
- **blog_os source (github)** — https://github.com/phil-opp/blog_os — the complete companion repository for the series — read the code as you go.
- **OSDev Wiki: Rust** — https://wiki.osdev.org/Rust — OSDev Wiki's language page for Rust-specific OS-dev guidance (targets, crates, pitfalls).
- **OSDev Wiki: Raspberry Pi Bare Bones (Rust)** — https://wiki.osdev.org/Raspberry_Pi_Bare_Bones — an ARM bare-bones kernel route in Rust if you prefer Pi over emulated x86.

## Rust OS Ecosystems & Example Kernels
- **rust-osdev/bootloader** — https://github.com/rust-osdev/bootloader — the bootloader crate used by the blog series; gives you a ready-made boot path so you can focus on the kernel.
- **rust-osdev/x86_64** — https://github.com/rust-osdev/x86_64 — the low-level x86_64 crate (paging, interrupts, GDT/IDT, port I/O) used by almost every Rust OS-dev project.
- **rCore-Tutorial-v3** — https://github.com/rcore-os/rCore-Tutorial-v3 — Tsinghua's famous course: write a RISC-V OS in Rust from scratch — a complete, tested teaching kernel with docs.
- **Theseus OS** — https://github.com/theseus-os/Theseus — a research OS written in Rust built around cell/state-based isolation — advanced reading for how far Rust OS-design can go.
- **Redox OS** — https://github.com/Redox-os/redox — the best-known general-purpose Rust OS; microkernel + userspace, a full real-world example of large-scale system Rust.
- **rust-os-comparison (flosse)** — https://github.com/flosse/rust-os-comparison — a curated comparison of the major OSes written in Rust, with links to each project's docs.

## Interactive & Practice Rust
- **Rustlings** — https://github.com/rust-lang/rustlings — the official set of small exercises that fix the borrow checker and language mechanics into your muscle memory; the standard companion to The Book.
- **Comprehensive Rust (Google)** — https://google.github.io/comprehensive-rust/ — a free, deep, classroom-style course covering Rust from basics to unsafe, FFI, async and embedded — excellent after The Book.
- **Tour of Rust** — https://tourofrust.com/ — a chapter-by-chapter interactive tour of the language, structured around short runnable exercises.
- **Rust by Practice** — https://practice.rs/ — hundreds of tightly-scoped, runnable practice exercises covering every language feature, with solutions.
- **Exercism: Rust Track** — https://exercism.org/tracks/rust — mentor-reviewed coding exercises that build Rust fluency through real problems.

## Books & Further Reading
- **Learning Rust With Entirely Too Many Linked Lists** — https://rust-unofficial.github.io/too-many-lists/ — a book that implements linked lists in progressively more idiomatic and unsafe Rust — the ideal bridge from The Book to low-level ownership/unsafe thinking.
- **Rust Atomics and Locks (Mara Bos)** — https://marabos.nl/atomics/ — the free online version of the book on Rust concurrency: atomics, mutexes, channels and lock-free data structures — directly relevant to writing a multi-core kernel.
- **The Rust Performance Book** — https://nnethercote.github.io/perf-book/ — practical, evidence-based advice on making Rust fast — useful for squeezing your kernel's hot paths.

## More Official Documentation
- **rust-lang.org/learn** — https://www.rust-lang.org/learn — the official learning hub linking The Book, examples, the standard library docs and many official sub-books in one place.
- **The rustc Book** — https://doc.rust-lang.org/rustc/ — official docs for the compiler itself: target specs, codegen options, LTO and `-C` flags you'll need for freestanding kernel builds.
- **The Rust Standard Library docs** — https://doc.rust-lang.org/std/ — the authoritative, searchable reference for `core`/`alloc`/`std` — know exactly what is (and isn't) available in `no_std`.
- **The Cargo Book** — https://doc.rust-lang.org/cargo/ — official reference for Cargo, profiles, build scripts and target handling — how you assemble kernel binaries and build scripts.
- **The Rust Unstable Book** — https://doc.rust-lang.org/unstable-book/ — documentation of nightly-only features; many kernel-relevant features (e.g. inline asm, `#[no_mangle]` details, `naked_functions`) live here.
- **The Rust Async Book** — https://rust-lang.github.io/async-book/ — official guide to async/await — useful when you get to async drivers or an async scheduler.

## More Rust OS-Dev Tooling & Projects
- **Rust for Linux (kernel)** — https://github.com/Rust-for-Linux/linux — the ongoing upstream effort adding Rust as a second kernel language in the Linux kernel — the most realistic large-scale demonstration of systems Rust.
- **rust-osdev/uefi-rs** — https://github.com/rust-osdev/uefi-rs — the safe Rust wrapper around the UEFI firmware interface — the modern boot path for Rust kernels on real hardware.
- **rust-osdev/multiboot2** — https://github.com/rust-osdev/multiboot2 — Rust bindings + parser for the Multiboot2 boot protocol, used by many GRUB+rust kernels.
- **rust-osdev/bootimage** — https://github.com/rust-osdev/bootimage — the tool that packages a Rust kernel and a bootloader into a bootable disk image — the standard build step for the blog_os ecosystem.
- **cargo-binutils** — https://github.com/rust-embedded/cargo-binutils — a cargo wrapper around LLVM binutils (`size`, `nm`, `objdump`, `objcopy`) — indispensable for inspecting and stripping your kernel ELF.
- **awesome-embedded-rust** — https://github.com/rust-embedded/awesome-embedded-rust — the community's curated list of embedded/no_std Rust crates and projects.

## More Official Rust Docs & Learning
- **The Rust Edition Guide** — https://doc.rust-lang.org/edition-guide/ — the official guide to what each Rust edition (2015 → 2018 → 2021 → 2024) changed — essential for choosing and migrating your kernel's edition and understanding which features are available.
- **Rust API Guidelines** — https://rust-lang.github.io/api-guidelines/ — the official checklist for designing good Rust APIs, including the naming, traits and lifetimes conventions that keep a large `no_std` codebase coherent.
- **Rust Design Patterns** — https://rust-unofficial.github.io/patterns/ — an open, community-maintained catalogue of idiomatic Rust patterns (creational, structural, anti-patterns) — useful before structuring a large kernel crate tree.
- **Rust 100 Exercises** — https://rust-exercises.com/ — a free, structured set of 100 exercises that walk you through Rust by building on each answer — a strong practice path between The Book and Rustlings.
- **The Rustc Dev Guide** — https://rustc-dev-guide.rust-lang.org/ — the official guide to the rustc compiler internals — for understanding exactly how your `no_std` kernel is lowered, monomorphized and linked.
- **awesome-rust** — https://github.com/rust-unofficial/awesome-rust — the community's definitive curated list of Rust projects and libraries across every domain, including systems and embedded.
- **users.rust-lang.org** — https://users.rust-lang.org/ — the official Rust users forum — the best place to ask low-level and `unsafe`/`no_std` questions with knowledgeable, often core-team answers.

## Rust OS Ecosystems & Example Kernels (more)
- **Aero OS** — https://github.com/Andy-Python-Programmer/aero — a modern, experimental monolithic UNIX-like OS in Rust (long mode, 5-level paging, SMP, UEFI) — a large, well-organized example of a full-scale Rust kernel.
- **Tock** — https://github.com/tock/tock — a secure embedded Rust OS for microcontrollers, built in safe Rust with a memory-protecting kernel — the standard reference for Rust on resource-constrained hardware.
- **Hubris** — https://github.com/oxidecomputer/hubris — Oxide Computer's small, memory-safe microcontroller OS written in Rust — a production-grade example of discipline in embedded Rust OS design.
- **Nebulet** — https://github.com/nebulet/nebulet — a microkernel that runs WebAssembly in kernel space, written in Rust — a fascinating experiment in what a Rust/WASM OS could be.

## Embedded / no_std Rust (more)
- **esp-rs documentation** — https://docs.esp-rs.org/ — the official docs for running Rust on Espressif ESP32/RISC-V hardware (`no_std` targets, `esp-hal`, `esp-idf-hal`) — a practical embedded/OS-dev vector for Rust.
