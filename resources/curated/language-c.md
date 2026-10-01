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

## University Courses & Structured Paths
- **CS50x: Introduction to Computer Science (Harvard)** — https://cs50.harvard.edu/x/ — the famous free first course in programming; its C weeks are the fastest way to learn proper C from scratch.
- **UIC C Course Notes (John Bell)** — https://www.cs.uic.edu/~jbell/CourseNotes/C_Programming/ — full university-grade C course notes covering pointers, memory, strings, recursion and more.

## More Beginner Tutorials
- **Programiz: Learn C** — https://www.programiz.com/c-programming — example-first, step-by-step C tutorials with a built-in online compiler.

## C Books (free)
- **The C Book (Banahan, Brady, Doran)** — https://publications.gbdirect.co.uk/c_book/ — the classic free full-length C textbook, still an excellent structured read many years on.
- **C Programming Wikibook** — https://en.wikibooks.org/wiki/C_Programming — a free, collaboratively maintained C textbook covering the language, the standard library and common idioms.

## C Reference & Standards
- **GNU C Library Reference Manual** — https://www.gnu.org/software/libc/manual/ — the official documentation for glibc, the de-facto POSIX/C library used by most real systems — essential for userspace and porting reference.
- **C99 draft standard (n1256)** — https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf — the free post-ballot C99 draft PDF — the precise spec behind the language you're writing.
- **c-faq (full site)** — https://c-faq.com/ — the complete comp.lang.c FAQ archive, covering pointers, arrays, memory, strings and all the classic C traps.

## C Memory, Layout & Concurrency
- **POSIX Threads Programming (Lawrence Livermore)** — https://hpc-tutorials.llnl.gov/posix/ — a clear, practical tutorial on pthreads: creating/joining threads, mutexes, condition variables; the basis for concurrency in your C kernel.
- **The Lost Art of Structure Packing (Eric S. Raymond)** — https://www.catb.org/esr/structure-packing/ — how C struct layout and padding work and how to pack them — vital for writing memory-efficient kernel data structures.
- **The C10K Problem (Dan Kegel)** — https://www.kegel.com/c10k.html — the classic systems-programming essay on handling ten thousand concurrent connections in C — great when you add a network stack.

## C Tools & Compilation
- **Compiler Explorer (godbolt)** — https://godbolt.org/ — compile C on any compiler/arch in your browser and watch the assembly — the single best way to see what your kernel code actually generates.

## More C OS-Dev Series & Projects
- **How to Make a Computer Operating System (SamyPesse)** — https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System — an open, step-by-step ebook walking you from bootloader to a small x86 OS in C/assembly.
- **Rolling your own UNIX-clone OS (os-tutorial / cfenollosa)** — https://github.com/cfenollosa/os-tutorial — a well-liked series of small, incremental commits that build up a working OS in C from the first boot sector.
- **James Molloy's Kernel Tutorial (OSDev Wiki archive)** — https://wiki.osdev.org/James_Molloy%27s_Kernel_Tutorial — the famous 10-part C tutorial covering segmentation, interrupts, paging, a heap, VFS and user mode (note: known bugs — read as a learning path, not a reference).
- **Bran's Kernel Development Tutorial** — https://www.osdever.net/bkerndev/Docs/title.htm — an old but classic C kernel tutorial (GDT/IDT, ISRs, paging) that many hobbyists start from.
- **OSDev Wiki: Memory Management** — https://wiki.osdev.org/Memory_Management — the wiki's overview of physical memory, paging and heap design — the system-level C you'll write after the hello-worlds.

## More C Beginner Tutorials
- **Codecademy: Learn C** — https://www.codecademy.com/learn/learn-c — a structured, interactive C course covering syntax, pointers and memory through hands-on browser exercises.
- **Zed Shaw: Learn C the Hard Way (free online)** — http://c.learncodethehardway.org/book/ — a practice-heavy free course that teaches C by building real programs; dated in parts but excellent for internalizing pointers and memory.
- **Beej's Guide to C** — https://beej.us/guide/bgc/ — an approachable, example-driven C tutorial and reference from the author of the widely-used Beej networking guides.

## More C Books & References
- **Modern C (Jens Gustedt)** — http://modernc.gforge.inria.fr/ — the free, official online edition of Gustedt's acclaimed C11 (now C23) textbook, written from a WG14 language-designer's perspective.
- **The GNU C Reference Manual** — https://www.gnu.org/software/gnu-c-manual/ — the Free Software Foundation's official reference for the C language as implemented by GCC, including GNU extensions.

## C Projects: Systems & Embedded
- **Build Your Own Text Editor (kilo / snaptoken)** — https://viewsourcecode.org/snaptoken/kilo/ — a complete walkthrough writing a real text editor in C from scratch — great practice with exactly the C you'll use in an OS.
- **Malloc Tutorial (Dan Luu)** — https://danluu.com/malloc-tutorial/ — implement your own `malloc` in C; the classic exercise for building memory allocators, directly relevant to writing a kernel heap.
- **FreeRTOS** — https://freertos.org/ — the most widely used free real-time kernel for microcontrollers, written in C — study its scheduler and memory management for small-scale OS patterns.

## Real C Kernels & University OS Courses
- **xv6 (MIT 6.S081)** — https://pdos.csail.mit.edu/6.S081/2023/schedule.html — MIT's undergraduate OS class centered on the xv6 teaching kernel written in C; includes lectures, labs and the full source.
- **xv6 source (mit-pdos/xv6-public)** — https://github.com/mit-pdos/xv6-public — the readable, fully commented xv6 kernel source — one of the best annotated real C kernels to study.
- **ToaruOS** — https://github.com/klange/toaruos — a polished, fully-featured hobby OS written in C (GUI, compositor, userspace) — an outstanding modern corpus of systems C.

## More C OS-Dev Series & Resources
- **The Little OS Book** — https://littleosbook.github.io/ — a short, approachable free ebook walking from the first boot sector to a small kernel in C/assembly.
- **64-bit OS Tutorial (gmarino2048)** — https://github.com/gmarino2048/64bit-os-tutorial — an easy-to-follow tutorial building a functional minimal 64-bit C kernel from zero.
- **MikeOS & How to Write a Simple OS** — https://mikeos.sourceforge.net/write-your-own-os.html — Mike Saunders' classic "write your own OS" primer (assembly + NASM + QEMU) that many C OS-dev folks read before adding the C layers.
- **OSDev Wiki: Limine Bare Bones** — https://wiki.osdev.org/Limine_Bare_Bones — the modern 64-bit higher-half C kernel hello-world using the Limine boot protocol (the recommended route over GRUB-style multiboot today).
- **OSDev Wiki: Higher Half x86 Bare Bones** — https://wiki.osdev.org/Higher_Half_x86_Bare_Bones — how to load and run a higher-half C kernel correctly.

## OSDev Wiki: Core Topics to Read Next
- **OSDev Wiki: GDT Tutorial** — https://wiki.osdev.org/GDT_Tutorial — the classic guide to the Global Descriptor Table your C kernel sets up on entering protected mode.
- **OSDev Wiki: Setting Up Paging** — https://wiki.osdev.org/Setting_Up_Paging — a step-by-step guide to enabling virtual addressing from C.
- **OSDev Wiki: Interrupts** — https://wiki.osdev.org/Interrupts — how interrupts work on x86 — the foundation for your IDT and interrupt-driven drivers in C.
- **OSDev Wiki: Port I/O** — https://wiki.osdev.org/Port_IO — talking to hardware through IN/OUT port instructions from C.
- **OSDev Wiki: Setting Up Long Mode** — https://wiki.osdev.org/Setting_Up_Long_Mode — switching your C kernel to 64-bit long mode.
- **OSDev Wiki: Creating a 64-bit kernel** — https://wiki.osdev.org/Creating_a_64-bit_kernel — compiling and linking a real 64-bit C kernel with the right flags (`-mcmodel=large`, `-mno-red-zone`, etc.).
- **OSDev Wiki: GCC Cross-Compiler** — https://wiki.osdev.org/GCC_Cross-Compiler — the canonical guide to building the C cross-compiler your kernel needs.
- **OSDev Wiki: Brendan's Memory Management Guide** — https://wiki.osdev.org/Brendan%27s_Memory_Management_Guide — a structured deep dive into memory management concepts for C kernels.
- **OSDev Wiki: Brendan's Multi-tasking Tutorial** — https://wiki.osdev.org/Brendan%27s_Multi-tasking_Tutorial — add preemptive multitasking to a C kernel, step by step.
