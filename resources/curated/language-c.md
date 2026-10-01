# C — Curated Learning & OS-Dev Resources

C is the language the OSDev world is built on: the reference implementation of almost every real kernel (Linux, the BSDs, Windows kernel internals) is C, and it's the language the OSDev Wiki's canonical **Bare Bones** and **Meaty Skeleton** tutorials are written in. All links below are free and verified reachable.

## C Language Tutorials (beginner-friendly)
- **Learn-C.org** — https://www.learn-c.org/ — interactive, browser-based C tutorial; start here if you've never written C.
- **freeCodeCamp: C Programming Handbook** — https://www.freecodecamp.org/news/the-c-beginners-handbook/ — thorough written walkthrough of C fundamentals for absolute beginners.
- **GeeksforGeeks: C Programming Language** — https://www.geeksforgeeks.org/c/c-programming-language/ — huge structured reference/tutorial hub covering syntax, control flow, functions, pointers, memory.
- **W3Schools: C Tutorial** — https://www.w3schools.com/c/ — quick, example-first introduction with an online compiler.
- **K&R "The C Programming Language" (official PDF from U. of Utah)** — https://www.math.utah.edu/computing/compilers/c/Kernighan-CTutorial.pdf — the classic first-edition reference, freely mirrored.

## Pointers & Memory Mastery
- **c-faq: Pointers** — https://c-faq.com/ptrs/ — authoritative answers to the classic "C pointer questions" from the comp.lang.c FAQ.
- **A Tutorial on Pointers and Arrays in C (Ted Jensen / ptrtut)** — https://github.com/jflaherty/ptrtut13 — the famous multi-part pointer tutorial that generations of C learners use; also mirrored at https://sites.cs.ucsb.edu/~mikec/cs16/misc/ptrtut12/pointers.htm.
- **UIC C Course Notes: Pointers** — https://www.cs.uic.edu/~jbell/CourseNotes/C_Programming/Pointers.html — clear, university-grade notes on pointers, arrays, pointer arithmetic and memory.

## C Algorithms & Data Structures
- **GeeksforGeeks: Learn DSA in C** — https://www.geeksforgeeks.org/c/learn-dsa-in-c/ — data structures and algorithms implemented in C (linked lists, stacks, queues, trees, sorting), directly relevant to writing low-level kernel data structures.
- **cppreference: C standard library headers** — https://en.cppreference.com/w/c/header — full reference for the C standard library (`stdlib.h`, `string.h`, `stdint.h`, etc.) you'll use in userspace and bare-metal ports.

## Language Reference & Standards
- **C standard (WG14)** — https://www.open-std.org/jtc1/sc22/wg14/ — the official C standardization committee project; get current and draft C standards here.
- **GCC documentation** — https://gcc.gnu.org/onlinedocs/gcc/ — the compiler you'll most likely use to build your kernel; covers flags, attributes and freestanding/multiboot-relevant options.

## C System Programming
- **USI Lugano: Getting Started with C and Systems Programming** — https://www.inf.usi.ch/faculty/carzaniga/edu/sysprog22f/introduction.html — university course intro mapping C to operating-system concepts (files, processes, signals, memory).
- **Beej's Guide to Network Programming** — https://beej.us/guide/bgnet/ — the classic free guide to sockets and networking in C; useful for system-level and driver work.
- **Beej's Guide to Unix IPC** — https://beej.us/guide/bgipc/ — pipes, FIFOs, message queues, semaphores and shared memory in C — the canonical companion for system programming.

## C OS-Dev Series & Tutorials
- **OSDev Wiki: Bare Bones** — https://wiki.osdev.org/Bare_Bones — the canonical C kernel hello-world (multiboot + VGA text) — start here.
- **OSDev Wiki: Meaty Skeleton** — https://wiki.osdev.org/Meaty_Skeleton — clean C project structure for a real kernel (kernel + libk split).
- **OSDev Wiki: C** — https://wiki.osdev.org/C — language-specific guidance, freestanding details and gotchas for writing C kernels.
- **OSDev Wiki: Raspberry Pi Bare Bones** — https://wiki.osdev.org/Raspberry_Pi_Bare_Bones — if you'd rather learn OS-dev on ARM hardware in C.
- **Operating Systems: From 0 to 1 (tuhdo/os01)** — https://github.com/tuhdo/os01 — a full, free ebook walking you from bootloader to a working OS in C/assembly.
- **Baeldung: How to Start Building an OS** — https://www.baeldung.com/cs/building-os — concise high-level orientation with per-language pointers.
- **dev.to: Build Your Own Operating System from Scratch in C** — https://dev.to/farhadrahimiklie/-how-to-build-your-own-operating-system-from-scratch-in-c-1112 — a practical from-scratch C walkthrough.

## Kernel Build Toolchain (companions to the above)
- **GRUB (bootloader)** — https://www.gnu.org/software/grub/ — the free GNU bootloader your OSDev images boot from.
- **QEMU (emulator)** — https://www.qemu.org/ — emulates x86 so you can boot/test your kernel safely.
- **NASM (assembler)** — https://www.nasm.us/ — the assembler used alongside C in almost every OSDev series.
- **Linux kernel source (read it!)** — https://github.com/torvalds/linux — the largest real corpus of production C in the world; study drivers, memory management and process code.
