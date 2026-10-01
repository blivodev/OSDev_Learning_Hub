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
