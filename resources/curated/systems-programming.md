# Systems Programming — Verified Resource List

Curated, verified links for the **systems side** of OS development: linkers & loaders, ELF/binaries, calling conventions, stacks, concurrency/threads, compilers & bootstrapping, low-level debugging (gdb, QEMU), paging/virtual-memory deep dives, POSIX/Linux systems programming, and unikernels. Every URL below was checked as reachable.

> Note: URLs returning `403`/`406` to a plain HTTP probe (GNU, gdb, OSDev Wiki, agner.org) are bot-blocks, not dead links — the pages render fine in a browser and were verified reachable via their canonical content.

---

## Linkers, loaders & binary formats

- **Linker (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Linker_(computing) — what a linker does: symbol resolution, relocation, section combining.
- **Loader (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Loader_(computing) — how an OS places an executable into memory.
- **Dynamic linker** (Wikipedia) — https://en.wikipedia.org/wiki/Dynamic_linker — runtime linking of shared libraries.
- **Position-independent code (PIC)** (Wikipedia) — https://en.wikipedia.org/wiki/Position-independent_code — code that runs at any address; needed for `.so`/PIE.
- **Shared library** (Wikipedia) — https://en.wikipedia.org/wiki/Shared_library
- **Library (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Library_(computing) — static vs dynamic.
- **Object file** (Wikipedia) — https://en.wikipedia.org/wiki/Object_file
- **Executable and Linkable Format (ELF)** (Wikipedia) — https://en.wikipedia.org/wiki/Executable_and_Linkable_Format — the format behind Linux/BSD kernels and binaries.
- **ELF — OSDev Wiki** — https://wiki.osdev.org/ELF — how to *load* an ELF kernel/module yourself: header, program headers, PT_LOAD segments.
- **man7: elf(5)** — https://man7.org/linux/man-pages/man5/elf.5.html — the canonical Unix man page for the ELF format.
- **Linkers and Loaders (John R. Levine, online)** — https://www.iecc.com/linker/ — the classic free online book on linkers, loaders, and object formats (ELF, PE/COFF, Mach-O), by the book's author.
- **How shared libraries work (begriffs)** — https://begriffs.com/posts/2021-07-04-shared-libraries.html — a clear deep-dive into ELF, symbol tables, `.got`/`.plt`, and dynamic linking.
- **GNU binutils** — https://www.gnu.org/software/binutils/ — the tool suite (`ld`, `as`, `objdump`, `readelf`, `nm`, `objcopy`, `strip`, `ar`) you'll live in.
- **GNU ld (linker) manual** — https://sourceware.org/binutils/docs/ld/ — linker scripts, memory layout, and relocations — essential for placing your kernel at the right address.
- **GNU ld docs (sourceware)** — https://sourceware.org/binutils/docs/ld/ — the same linker manual in clean HTML.
- **GNU Assembler (as) docs** — https://sourceware.org/binutils/docs/as/

## Calling conventions, stack & ABI

- **Calling convention** (Wikipedia) — https://en.wikipedia.org/wiki/Calling_convention
- **x86 calling conventions** (Wikipedia) — https://en.wikipedia.org/wiki/X86_calling_conventions
- **System V AMD64 ABI** — https://gitlab.com/x86-psABIs/x86-64-ABI — the authoritative x86-64 ABI: argument/machine registers, stack alignment, struct passing, red zone.
- **Call stack** (Wikipedia) — https://en.wikipedia.org/wiki/Call_stack — stack frames, prologue/epilogue, return addresses.
- **Stack machine** (Wikipedia) — https://en.wikipedia.org/wiki/Stack_machine
- **Calling Conventions — OSDev Wiki** — https://wiki.osdev.org/Calling_Conventions — System V vs Microsoft x64 cheat sheet plus kernel-specific traps (16-byte alignment, red zone).
- **Agner Fog — Calling Conventions** — https://www.agner.org/optimize/calling_conventions.pdf — exhaustive per-compiler ABI tables.
- **DWARF** (Wikipedia) — https://en.wikipedia.org/wiki/DWARF — the debug info format gdb/strace use to map addresses back to source.

## Concurrency, threads & processes

- **Process (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Process_(computing)
- **Thread (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Thread_(computing) — threads vs processes; kernel vs user threads.
- **Concurrency (computer science)** (Wikipedia) — https://en.wikipedia.org/wiki/Concurrency_(computer_science)
- **Thread safety** (Wikipedia) — https://en.wikipedia.org/wiki/Thread_safety
- **Mutex** (Wikipedia) — https://en.wikipedia.org/wiki/Mutex
- **Semaphore (programming)** (Wikipedia) — https://en.wikipedia.org/wiki/Semaphore_(programming)
- **Lock (computer science)** (Wikipedia) — https://en.wikipedia.org/wiki/Lock_(computer_science)
- **Race condition** (Wikipedia) — https://en.wikipedia.org/wiki/Race_condition
- **Deadlock** (Wikipedia) — https://en.wikipedia.org/wiki/Deadlock
- **Context switch** (Wikipedia) — https://en.wikipedia.org/wiki/Context_switch — saving/restoring CPU state between threads/processes (you'll implement this in your kernel).
- **Process control block (PCB)** (Wikipedia) — https://en.wikipedia.org/wiki/Process_control_block
- **Scheduling (computing)** (Wikipedia) — https://en.wikipedia.org/wiki/Scheduling_(computing) — the algorithms that pick the next runnable task.
- **Inter-process communication (IPC)** (Wikipedia) — https://en.wikipedia.org/wiki/Inter-process_communication — pipes, shmem, sockets, signals.
- **System call** (Wikipedia) — https://en.wikipedia.org/wiki/System_call — the user↔kernel interface.

## Compilers & bootstrapping

- **Compiler** (Wikipedia) — https://en.wikipedia.org/wiki/Compiler
- **Compiler bootstrapping** (Wikipedia) — https://en.wikipedia.org/wiki/Compiler_bootstrapping — how a compiler compiles itself.
- **Retargetable compiler** (Wikipedia) — https://en.wikipedia.org/wiki/Retargetable_compiler
- **Intermediate representation (IR)** (Wikipedia) — https://en.wikipedia.org/wiki/Intermediate_representation
- **Lexical analysis** (Wikipedia) — https://en.wikipedia.org/wiki/Lexical_analysis — tokenizing source.
- **Semantic analysis (compilers)** (Wikipedia) — https://en.wikipedia.org/wiki/Semantic_analysis_(compilers)
- **GCC** — https://gcc.gnu.org/ — the C/C++/Rust… compiler you'll cross-compile your kernel with.
- **Clang** — https://clang.llvm.org/ — LLVM's C-family frontend (great diagnostics for low-level code).
- **LLVM Project** — https://llvm.org/ — the compiler infrastructure; its [codegen](https://github.com/llvm/llvm-project) is the best real-world IR/backend to read.
- **xz-style "make your own compiler" bootstraps** — see the `os-tutorial` and `rCore-Tutorial-v3` entries below for kernel+compiler-side bootstrapping in practice.

## Low-level debugging (gdb, QEMU)

- **GDB: The GNU Project Debugger** — https://www.gnu.org/software/gdb/ — the debugger for bare-metal and user-space alike.
- **GDB Documentation (online manuals)** — https://www.sourceware.org/gdb/documentation/ — full gdb manual; single-PDF copy at https://sourceware.org/gdb/current/onlinedocs/gdb.pdf.
- **Debugging** (Wikipedia) — https://en.wikipedia.org/wiki/Debugging
- **Core dump** (Wikipedia) — https://en.wikipedia.org/wiki/Core_dump — the post-mortem memory image gdb opens.
- **GDB Cheat Sheet (darkdust)** — https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf — a printable reference of the most-used gdb commands.
- **QEMU** — https://www.qemu.org/ — the emulator you boot/test kernels in; supports gdb remote debugging of your kernel in real time.
- **OSDev Wiki — QEMU** — https://wiki.osdev.org/QEMU — running and debugging OSdev kernels under QEMU.
- **OSDev Wiki — GDB / Debug builds** — see the wiki's per-toolchain guides; start at https://wiki.osdev.org/GDB.

## Paging & virtual memory deep dives

- **Virtual memory** (Wikipedia) — https://en.wikipedia.org/wiki/Virtual_memory — full treatment: paging, demand paging, copy-on-write, swapping.
- **Paging** (Wikipedia) — https://en.wikipedia.org/wiki/Paging
- **Memory management unit (MMU)** (Wikipedia) — https://en.wikipedia.org/wiki/Memory_management_unit
- **Translation lookaside buffer (TLB)** (Wikipedia) — https://en.wikipedia.org/wiki/Translation_lookaside_buffer — including TLB shootdown across cores.
- **OSDev Wiki — Paging** — https://wiki.osdev.org/Paging — implementing page tables on x86/x86-64, CR3, higher-half.
- **OSDev Wiki — Memory Management** — https://wiki.osdev.org/Memory_Management — from physical frames to a virtual heap.
- **OSDev Wiki — Memory-mapped IO / Allocation** — https://wiki.osdev.org/Memory_Map — the physical memory layout your kernel must respect.
- **Linux kernel docs: Memory Management** — https://www.kernel.org/doc/html/latest/mm/index.html — how a real OS structures virtual memory (VMAs, page tables, KSM, swap).
- **Linux kernel docs: Admin Guide / MM** — https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html — user-facing view of paging, overcommit, and swap.
- **Linux-insides (0xAX)** — https://github.com/0xAX/linux-insides — a free book reading the Linux kernel, with detailed paging/virtual-memory chapters. Readable at https://0xax.gitbooks.io/linux-insides/content/.

## POSIX / Linux systems programming

- **POSIX** (Wikipedia) — https://en.wikipedia.org/wiki/POSIX — the standard your OS aims to be compatible with.
- **Systems programming** (Wikipedia) — https://en.wikipedia.org/wiki/System_programming
- **man7.org Linux manual pages** — https://man7.org/linux/man-pages/ — the canonical online Linux man pages (syscalls in section 2, libc in section 3).
- **syscalls(2)** — https://man7.org/linux/man-pages/man2/syscall.2.html — the full Linux syscall list and ABI.
- **mmap(2)** — https://man7.org/linux/man-pages/man2/mmap.2.html — mapping files/devices into memory; core to virtual-memory understanding.
- **fork(2)** — https://man7.org/linux/man-pages/man2/fork.2.html — creating processes.
- **execve(2)** — https://man7.org/linux/man-pages/man2/execve.2.html — loading programs (the user-space loader).
- **The Linux Programming Interface (man7, free sample/manual)** — https://man7.org/tlpi/ — Michael Kerrisk's site with errata and many freely readable chapters.
- **GNU C Library manual** — https://sourceware.org/glibc/manual/ — the complete libc reference (syscalls, threads, memory allocation) in browsable HTML.
- **POSIX Base Specifications (Open Group)** — https://pubs.opengroup.org/onlinepubs/9699919799/ — the authoritative POSIX standard, free online.
- **Beej's Guide to C Programming** — https://beej.us/guide/bgc/
- **Beej's Guide to Network Programming** — https://beej.us/guide/bgnet/ — sockets, the de-facto intro to BSD sockets.
- **Beej's Guide to IPC** — https://beej.us/guide/bgipc/ — Unix IPC: shared memory, semaphores, queues.
- **Linux Kernel Documentation (docs.kernel.org)** — https://docs.kernel.org/ — the official kernel docs, including loader/ELF and paging internals.
- **Linux source (torvalds/linux)** — https://github.com/torvalds/linux — the reference implementation of everything above.
- **GNU Make manual** — https://www.gnu.org/software/make/manual/ — the build tool that assembles every OS toolchain.
- **cfenollosa/os-tutorial** — https://github.com/cfenollosa/os-tutorial — a pragmatic from-scratch x86 OS tutorial that glues assembly, linker scripts, and C together.

## Operating systems courses & books (systems-programming side)

- **Operating Systems: Three Easy Pieces (OSTEP)** — https://pages.cs.wisc.edu/~remzi/OSTEP/ — Remzi & Andrea Arpaci-Dusseau's free, widely-used OS textbook (chapters: virtualization, concurrency, persistence, paging, linking).
- **MIT 6.S081 / 6.828: Operating System Engineering** — https://pdos.csail.mit.edu/6.S081/2021/overview.html — the famous xv6 course: implement system calls, paging, and scheduling in a RISC-V OS.
- **xv6, a simple Unix-like teaching OS** — https://pdos.csail.mit.edu/6.S081/2020/xv6.html — the source + book (Chapters booklet) for the course OS. Source: https://github.com/mit-pdos/xv6-riscv, book: https://github.com/mit-pdos/xv6-riscv-book.
- **MIT 6.033 Computer System Engineering** — https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/ — systems fundamentals including OS and networking layers.
- **rCore Tutorial (Rust, RISC-V)** — https://rcore-os.github.io/rCore-Tutorial-Book-v3/ — a full from-scratch RISC-V OS in Rust, with paging, traps, and file systems; code at https://github.com/rcore-os/rCore-Tutorial-v3.
- **The Little OS Book** — https://littleosbook.github.io/ — a short, beginner-friendly guide to a minimal OS in C, walking through booting, interrupts, and memory management.
- **Linux-insides (0xAX)** — see *Paging & virtual memory*.

## Unikernels & minimal VMs (systems-programming pinnacle)

- **Unikernel** (Wikipedia) — https://en.wikipedia.org/wiki/Unikernel — the OS-as-a-library model.
- **MirageOS** — https://github.com/mirage/mirage — the canonical OCaml unikernel; a full OS targeting the Xen/Virtio interface. Overview: https://en.wikipedia.org/wiki/MirageOS.
- **Unikraft** — https://github.com/unikraft/unikraft — a modular, POSIX-ish unikernel framework in C.
- **Unik (Solo.io, Go)** — https://github.com/solo-io/unik — build and run unikernels from Python/Node/Go sources.
- **Nanos (NanoVMs)** — https://nanos.org/ — a tiny unikernel that runs unmodified POSIX binaries.
- **IncludeOS** — https://github.com/includeos/includeos — a C++ unikernel.
- **HermitCore (Rust/C)** — https://github.com/hermitcore/rusty-hermit — a Rust unikernel; older C++ version at https://github.com/hermit-os/hermit-rs. (pair with the `hermitcore` org: https://github.com/hermit-os/hermit-rs).
- **gVisor** — https://github.com/google/gvisor — a user-space kernel implementing the Linux syscall surface (great for syscall ABI study).
- **Firecracker** — https://github.com/firecracker-microvm/firecracker — AWS's minimal VMM; a clean, readable systems-programming codebase (KVM, Virtio).
- **Cloud Hypervisor** — https://github.com/cloud-hypervisor/cloud-hypervisor — a lightweight VMM in Rust (KVM + Virtio).

---

## Putting it together (integrated learning paths)

- **x86 Bare-Metal Examples (cirosantilli)** — https://github.com/cirosantilli/x86-bare-metal-examples — dozens of minimal x86-64 bare-metal examples (paging, interrupts, GDT/IDT) to compile and run in QEMU.
- **OSDev Wiki** — https://wiki.osdev.org/ — the hub that ties it all together: wiki + forums at https://forum.osdev.org/.
