# C++ — Curated Learning & OS-Dev Resources

C++ gives you low-level control with high-level abstraction — which is exactly why several hobby OSes (thor-os, NanOS, LemonOS) are written in it. Real OS-dev in C++ means freestanding code with no standard library; these resources cover both modern C++ and that freestanding world. All links verified reachable.

## Modern C++ Tutorials (beginner → intermediate)
- **Learn C++ (learncpp)** — https://www.learncpp.com/ — widely considered the best free C++ tutorial for beginners; start at https://www.learncpp.com/cpp-tutorial/introduction-to-these-tutorials/.
- **cppreference.com** — https://en.cppreference.com/ — the definitive free reference for the C++ language and standard library; keep it open constantly.
- **isocpp.org** — https://isocpp.org/ — the official C++ foundation site; news, FAQs and standards documents. Get-started page: https://isocpp.org/get-started.
- **Hacking C++** — https://hackingcpp.com/ — modern, visually dense cheatsheets and articles for C++11/14/17/20 — great for fast reference.
- **GeeksforGeeks: C++** — https://www.geeksforgeeks.org/c-plus-plus/ — comprehensive structured tutorials across the language, STL and OOP.

## Modern C++ / Low-Level & Systems Programming
- **simplifycpp.org: C or C++ for Systems Programming?** — https://www.simplifycpp.org/ — reasoning about when C++ is the right tool for systems-level work.
- **GitHub: systems-programming-c (Cameron-Dubois)** — https://github.com/Cameron-Dubois/systems-programming-c — low-level systems programming in modern C++: process control, IPC, event-driven networking, threading and RAII on POSIX/Linux — an excellent modern-C++ systems primer.

## C++ OS-Dev Series & Tutorials
- **OSDev Wiki: Bare Bones (C++)** — https://wiki.osdev.org/Bare_Bones — the canonical C++ kernel hello-world (multiboot + VGA + a kernel-entry C++ stub); start here.
- **OSDev Wiki: C++** — https://wiki.osdev.org/C%2B%2B — language-specific C++ guidance: freestanding headers, globals/DWARF gotchas, new/delete and exceptions in-kernel.
- **OSDev Wiki: Meaty Skeleton** — https://wiki.osdev.org/Meaty_Skeleton — clean C++-capable project structure for a real kernel.
- **dev.to: C++ in Kernel Development — A Comprehensive Guide** — https://dev.to/trish_07/c-in-kernel-development-a-comprehensive-guide-564d — practical article on writing C++ kernel code (freestanding, linking, portability).

## Complete C++ OS Projects to Study
- **thor-os** — https://github.com/wichtounet/thor-os — a well-known simple C++ OS written from scratch (kernel, memory management, scheduler, drivers); regularly studied as a C++ OS-dev reference.
- **NanOS (NanOS-labs)** — https://github.com/NanOS-labs/NanOS — a hobby C++ microkernel-oriented OS used in universities; clean, readable modern C++.
- **LemonOS** — https://github.com/LemonOSProject/LemonOS — a featureful C++ hobby OS with GUI, networking and a ported userspace — great for reading "what a full C++ OS looks like".
- **MeetixOS** — https://github.com/MarcoCicognani/MeetixOS — Unix-like hobby OS written in modern C++20.
- **FontaineOS** — https://github.com/alistairfontaine/FontaineOS — a lightweight freestanding C++20 x86 kernel built directly on hardware registers and VGA with zero stdlib — ideal minimal C++ kernel example.
- **MaxOS** — https://github.com/maxtyson123/MaxOS — a 64-bit hobby OS written in C++ (long mode, paging, interrupts).
- **osdev-barebones (rslay)** — https://github.com/rslay/osdev-barebones — a compact, commented C++ bare-bones kernel implementation.
- **barebones (fwsGonzo)** — https://github.com/fwsGonzo/barebones — minimal C++/x86-64 bare-bones with clear step-by-step commits.

## Freestanding & Kernel-Linker Companions
- **OSDev Wiki: Getting Started** — https://wiki.osdev.org/Getting_Started — prerequisites and mindset before you write a C++ kernel.
- **OSDev Wiki: Raspberry Pi Bare Bones** — https://wiki.osdev.org/Raspberry_Pi_Bare_Bones — a C++-friendly ARM OS-dev path if you prefer that hardware.
- **Birmingham CS: OS Design PDF** — https://www.cs.bham.ac.uk/~exr/lectures/opsys/10_11/lectures/os-dev.pdf — a classic university lecture slide deck on writing an OS (using C/C++ assembly).
