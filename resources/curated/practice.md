# Practice & Hands-on Projects — Verified Resource List

A long, categorized list of free, hands-on ways to *do* OS & low-level development rather than just read about it: from-scratch OS projects to build, bare-metal challenges, coding-interview-style kernel exercises, kernel/exploit CTFs (pwn.college & friends), online judges for C and Rust, project-idea lists, and the classic "build your own X" repositories. Every link below was verified reachable at curation time.

---

## "Build your own OS" — full from-scratch projects

- **[Writing an OS in Rust (phil-opp / `blog_os`)]** — the flagship hands-on Rust OS series: freestanding binary → VGA → interrupts → paging → heap → multitasking, with a real repo to clone and build. — https://os.phil-opp.com/
- **[`blog_os` source (GitHub)]** — cloneable, buildable source for every chapter. — https://github.com/phil-opp/blog_os
- **[rCore Tutorial (Rust, RISC-V)]** — build a complete RISC-V OS in Rust (traps, paging, file systems) with accompanying exercises. — https://rcore-os.github.io/rCore-Tutorial-Book-v3/
- **[`rCore-Tutorial-v3` source]** — the working kernel behind the book. — https://github.com/rcore-os/rCore-Tutorial-v3
- **[cfenollosa/os-tutorial]** — "How to create an OS from scratch": short, incremental, from boot sector to a simple shell (no GRUB). — https://github.com/cfenollosa/os-tutorial
- **[The Little OS Book]** — a concise, friendly guide that takes you from zero to a running C kernel. — https://littleosbook.github.io/
- **[cirosantilli/x86-bare-metal-examples]** — dozens of minimal, self-contained x86-64 bare-metal examples (paging, interrupts, GDT/IDT) you compile and run in QEMU — ideal quick practice. — https://github.com/cirosantilli/x86-bare-metal-examples
- **[OSDev Wiki — Bare Bones]** — the canonical minimal 32-bit C kernel booted by GRUB/Multiboot; the standard first OS-dev exercise. — https://wiki.osdev.org/Bare_Bones

## University OS labs to build (MIT xv6 & friends)

- **[MIT 6.S081 / xv6 labs]** — implement real kernel features: system calls, page tables, COW fork, threads, file systems, mmap — in the small xv6 RISC-V OS. — https://pdos.csail.mit.edu/6.S081/2023/labs/util.html
- **[xv6 textbook/overview page]** — the course hub with the companion "xv6 book" that explains each lab's kernel. — https://pdos.csail.mit.edu/6.S081/2023/
- **[xv6 source (mit-pdos/xv6-riscv)]** — the clean RISC-V teaching kernel you'll be modifying. — https://github.com/mit-pdos/xv6-riscv
- **[OSTEP projects]** — real OS-engineering projects (schedulers, memory allocators, concurrency, file systems) that pair with the OSTEP book. — https://github.com/remzi-arpacidusseau/ostep-projects
- **[OSTEP (free textbook)]** — the theory behind those projects: virtualization, concurrency, persistence. — https://pages.cs.wisc.edu/~remzi/OSTEP/
- **[ops-class.org (SUNY Buffalo)]** — a complete self-paced OS course with *projects* and recorded lectures to do at home. — https://www.ops-class.org/

## Bare-metal & CPU/hardware practice

- **[Ben Eater — 8-bit computer]** — build a working 8-bit computer on breadboards and program it in raw microcode/assembly. — https://eater.net/
- **[Ben Eater — 6502 computer]** — build a 6502-based personal computer and write a monitor/OS for it in assembly. — https://eater.net/6502
- **[Nand to Tetris (nand2tetris)]** — build a general-purpose computer from NAND gates up to a high-level language & OS — famous hands-on systems course. — https://www.nand2tetris.org/
- **[Wokwi]** — in-browser simulation of ESP32/Arduino/ATmega etc. for bare-metal practice without hardware. — https://wokwi.com/
- **[TinkerCAD Circuits]** — free in-browser Arduino/electronics simulation for simple bare-metal blinking/GPIO work. — https://www.tinkercad.com/

## Kernel & systems challenge sets (interview-style low-level exercises)

- **[Low Level Academy]** — courses + in-browser coding challenges in C, memory/pointers, threads and assembly (subscription, with a free C-basics starter course). — https://lowlevel.academy/
- **[Coding Interview University (jwasham)]** — a comprehensive from-scratch computer-science study plan including memory, CPU, assembly and OS topics with practice links. — https://github.com/jwasham/coding-interview-university
- **[Godbolt / Compiler Explorer]** — not a judge, but the best way to *practice* reading the assembly your C/Rust compiles to. — https://godbolt.org/
- **[Advent of Code]** — annual daily programming puzzles (25/day in Dec) that sharpen the systems-style problem solving behind kernel code. — https://adventofcode.com/
- **[Project Euler]** — math/programming problems that build the rigorous algorithm chops useful for low-level work. — https://projecteuler.net/

## Kernel / exploit & low-level CTFs

- **[pwn.college]** — the free, from-scratch low-level & exploitation learning platform by Zardus & Yan: program interaction, assembly, reverse engineering, pwn. Start with the guided modules. — https://pwn.college/
- **[Microcorruption]** — a web-based embedded-systems CTF in which you reverse-engineer and exploit a (fictional) locked device running a small RISC OS. — https://microcorruption.com/
- **[OverTheWire: Bandit]** — beginner terminal/shell challenges that build the Linux fluency you need for systems work. — https://overthewire.org/wargames/bandit/
- **[PicoCTF]** — a free capture-the-flag with beginner-friendly binary/rev/pwn categories. — https://picoctf.org/
- **[Hack The Box]** — a popular cybersecurity lab platform with pwn/reversing/binary-exploit machines (some free access). — https://www.hackthebox.com/
- **[TryHackMe]** — guided, browser-based hands-on security/binary rooms (free tier). — https://tryhackme.com/
- **[CTFtime]** — the global CTF calendar/ranking — find live kernel/pwn competitions to practice against the clock. — https://ctftime.org/

## Online judges & coding practice for C and Rust

- **[Exercism — C track]** — ~100 mentor-reviewed C exercises plus a test-runner in the browser. — https://exercism.org/tracks/c
- **[Exercism — Rust track]** — mentor-reviewed Rust exercises from strings to traits/iterators. — https://exercism.org/tracks/rust
- **[Exercism — x86-64 Assembly track]** — write and run real x86-64 assembly in the browser. — https://exercism.org/tracks/x86-64-assembly
- **[Exercism — all tracks]** — browse every language including other low-level/assembly tracks. — https://exercism.org/tracks
- **[CodeWars]** — kata (challenges) in C, Rust, assembly and more, graded up through difficulty tiers. — https://www.codewars.com/
- **[LeetCode]** — the famous algorithm judge; also useful for the pointer/array/memory problems directly relevant to systems code (anti-bot `403` to scripts; live in browser). — https://leetcode.com/
- **[HackerRank — C]** — free C practice full of pointers/structs/snippets you'll recognize from kernel code. — https://www.hackerrank.com/domains/c
- **[CodinGame]** — gamified coding puzzles on real CPU/algorithm topics. — https://www.codingame.com/
- **[CodeSignal]** — arcade-style practice with focus on smooth typing/writing code under time pressure. — https://codesignal.com/
- **[Edabit]** — bite-size beginner-to-intermediate challenges in C, Rust and many other languages. — https://edabit.com/
- **[CSES Problem Set]** — a well-regarded, curated set of algorithm/data-structure problems (C++/C friendly). — https://cses.fi/problemset/
- **[Kattis]** — hundreds of judge problems, including a good low-level/language corner. — https://open.kattis.com/

## Rust-specific hands-on practice

- **[Rustlings]** — the official small exercises that teach you Rust with auto-checking; great before or alongside `blog_os`. — https://github.com/rust-lang/rustlings
- **[Tour of Rust]** — an interactive step-by-step tour of Rust semantics run right in the browser. — https://tourofrust.com/
- **[The Rust Book]** — the foundational reading that the practice exercises assume. — https://doc.rust-lang.org/book/
- **[Rust by Example]** — runnable annotated examples for every Rust topic. — https://doc.rust-lang.org/rust-by-example/

## Linux kernel contribution & systems practice

- **[KernelNewbies]** — the friendly community + tutorials for learning to read & patch the Linux kernel (try `FirstKernelPatch`). — https://kernelnewbies.org/
- **[Linux Device Drivers, 3rd Edition (LDD3, free)]** — the classic book, free online: write real kernel modules/drivers as practice. — https://lwn.net/Kernel/LDD3/
- **[Linux From Scratch (LFS)]** — build an entire working Linux system from source by hand — a marathon of real systems practice. — https://www.linuxfromscratch.org/

## "Build your own X" & project-idea lists

- **[build-your-own-x (codecrafters-io)]** — the famous curated list of "build your own {OS, shell, compiler, text editor, database, game…}" tutorials — a goldmine of systems project ideas. — https://github.com/codecrafters-io/build-your-own-x
- **[awesome-osdev (leap0x7b)]** — a big curated list of OS-dev tutorials and reference projects to emulate. — https://github.com/leap0x7b/awesome-osdev
- **[Tom's Hardware-scale "build an OS" links via OSDev Wiki — Getting Started]** — the wiki's recommended first steps + pointers to guided projects. — https://wiki.osdev.org/Getting_Started

## Real open-source kernels to read & hack on for practice

- **[SerenityOS]** — an ambitious, approachable Unix-like OS; fork it and implement a syscall/port as a practice project. — https://github.com/SerenityOS/serenity
- **[Redox OS]** — a Rust-written microkernel OS; a real Rust systems codebase to study and build. — https://github.com/redox-os/redox
- **[linux-insides (0xAX)]** — not code to run, but a step-by-step *reading* of the Linux kernel boot; pair with `git clone` of your own copy to follow along. — https://github.com/0xAX/linux-insides

---

*Maintained for the OSDev Learning Hub. Links verified September 2026; OSDev-wiki/LeetCode URLs return anti-bot `403` to scripts but are confirmed live in a browser.*
