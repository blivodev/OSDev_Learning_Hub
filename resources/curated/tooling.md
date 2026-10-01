# Tooling & Developer Toolchain — Verified Resource List

A long, categorized, verified list of free/real tools for OS & systems development: build systems, assemblers, compilers & cross-toolchains, linkers, debuggers & disassemblers, emulators, hex editors, binary/ELF inspection tools, kernel-debugging tooling, static analysis & sanitizers, profilers, version control, low-level CI, and OS/container build tooling. Everything here is free, public, and was verified reachable at curation time. (As elsewhere in this library, the OSDev-wiki and a few GNU/man7 URLs return bot-block `403`/`418` to scripts but render fine in a browser.)

---

## Build systems

- **[GNU Make]** — the de-facto build tool for every OS toolchain; drives kernel/iso builds and Makefiles. — https://www.gnu.org/software/make/
- **[GNU Make manual]** — the official manual; ch. 6 (recipes) & 10 (functions) are the ones you'll live in. — https://www.gnu.org/software/make/manual/make.html
- **[CMake]** — cross-platform build generator with great C/C++ (and Rust) support; the modern default for portable projects. — https://cmake.org/
- **[CMake documentation]** — official docs; start with the step-by-step Tutorial. — https://cmake.org/documentation/
- **[CMake tutorial (step-by-step version)]** — the guided ten-step introduction to CMake. — https://cmake.org/cmake/help/latest/guide/tutorial/
- **[Ninja]** — the fast, minimal build system CMake/Meson generate into; near-instant incremental kernel builds. — https://ninja-build.org/
- **[Ninja manual]** — the concise rules/edge/depfile model explained. — https://ninja-build.org/manual.html
- **[Bazel]** — Google's build system (hermetic, sandboxed, language-agnostic); heavier but great for reproducible cross builds. — https://bazel.build/
- **[Meson]** — a fast, readable, Python-free-while-friendly build system common in C/C++ systems projects. — https://mesonbuild.com/
- **[Meson reference manual]** — the full function/object reference. — https://mesonbuild.com/Reference-manual.html
- **[xbstrap]** — a shell-native build orchestration tool (used by managarm) mixing "recipes" for ports + a toolchain. — https://github.com/managarm/xbstrap
- **[Cargo (Rust's build system)]** — the default for Rust projects; cross-compile to bare-metal with `no_std` targets. — https://doc.rust-lang.org/cargo/
- **[Gradle (native plugin)]** — JVM-based build tool with a C/C++ "native" plugin; heavier option if you already know Gradle. — https://gradle.org/

## Assemblers & assembly tooling

- **[NASM]** — the Intel-syntax assembler used by nearly every x86 OS-dev tutorial. — https://www.nasm.us/
- **[NASM documentation]** — official manual (`nasmdoc0.html` is the chapter index). — https://www.nasm.us/doc/nasmdoc0.html
- **[FASM]** — the flat assembler; one of the smallest, fastest assemblers, popular for bootloaders and demoscene code. — https://flatassembler.net/
- **[FASM message board]** — active community/Q&A for FASM. — https://board.flatassembler.net/
- **[YASM]** — a rewrite of NASM for even faster assembly and better 64-bit support (maintained on GitHub). — https://github.com/yasm/yasm
- **[GNU Assembler (as) docs]** — the AT&T/Intel-syntax GNU assembler; comes with binutils/your cross-toolchain. — https://sourceware.org/binutils/docs/as/
- **[LLVM integrated assembler]** — the assembler built into clang (`.s` → object); see the clang command-line docs. — https://clang.llvm.org/docs/ClangCommandLineReference.html

## Compilers & cross-toolchains

- **[GCC]** — the GNU Compiler Collection (C/C++/Ada/Fortran…); what you normally cross-compile a kernel with. — https://gcc.gnu.org/
- **[GCC cross-compiler (OSDev Wiki)]** — the canonical walkthrough for building your own `i686-elf`/`x86_64-elf` GCC (anti-bot 403 to scripts; live in a browser). — https://wiki.osdev.org/GCC_Cross-Compiler
- **[Clang]** — LLVM's C-family frontend; excellent diagnostics and a single binary that also hosts the cross-assembler + link. — https://clang.llvm.org/
- **[LLVM Project]** — the compiler infrastructure (IR, backend/codegen, lld, lldb, clang-tools). — https://llvm.org/
- **[LLVM monorepo (GitHub)]** — the whole LLVM/clang/lld/lldb source in one tree; the best real-world IR/backend to read. — https://github.com/llvm/llvm-project
- **[Zig (zig cc)]** — a single-file compiler + drop-in C compiler (`zig cc`) that can also cross-compile C/C++ anywhere from one machine. — https://ziglang.org/
- **[Zig downloads]** — prebuilt binaries incl. cross-target toolchains. — https://ziglang.org/download/
- **[TCC — Tiny C Compiler]** — a tiny, blazing-fast C compiler good for rapid experiments and scripting-style C. — https://bellard.org/tcc/
- **[Rust / rustc]** — the Rust compiler; pairs with `rustc`/`cargo` bare-metal targets for OS dev. — https://www.rust-lang.org/
- **[musl.cc]** — prebuilt musl-based cross-compilation toolchains for many targets (a practical shortcut vs. building your own). — https://musl.cc/

## Linkers

- **[GNU ld manual]** — linker scripts, memory layout, symbol resolution; essential for placing your kernel at the right address. — https://sourceware.org/binutils/docs/ld/
- **[LLD (LLVM linker)]** — the fast LLVM linker used by clang builds by default; robust for OS-dev link scripts. — https://lld.llvm.org/
- **[mold]** — a drop-in, extremely fast linker for Linux; great for big kernel builds. — https://github.com/rui314/mold
- **[GNU binutils]** — the tool suite (`ld`, `as`, `objdump`, `readelf`, `nm`, `objcopy`, `strip`, `ar`) you'll live in. — https://www.gnu.org/software/binutils/

## Debuggers & disassemblers

- **[GDB]** — the GNU debugger; connects to QEMU's gdb-stub so you can debug your kernel live. — https://www.gnu.org/software/gdb/
- **[GDB documentation]** — full online manuals (see also the single-PDF copy in the sidebar). — https://sourceware.org/gdb/documentation/
- **[LLDB]** — LLVM's debugger; scriptable in Python, great with clang-built code. — https://lldb.llvm.org/
- **[WinDbg]** — Microsoft's kernel/user-mode debugger for Windows (also hunts down Windows kernel bugs). — https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/
- **[radare2]** — a powerful, scriptable reverse-engineering framework (disassembler, debugger, hex view, ESIL). — https://rada.re/n/
- **[radare2 (GitHub)]** — source + releases. — https://github.com/radareorg/radare2
- **[Ghidra]** — NSA's free reverse-engineering suite: disassembler, decompiler, scripting. — https://ghidra-sre.org/
- **[Ghidra (GitHub)]** — source + releases (redirect target of ghidra-sre.org). — https://github.com/NationalSecurityAgency/ghidra
- **[Capstone]** — a lightweight multi-arch disassembly *engine* (outputs machine code → assembly) you can embed. — https://www.capstone-engine.org/
- **[objdump (binutils docs)]** — disassemble object/kernel files; `-d` for code, `-s` for hex-dump of sections. — https://sourceware.org/binutils/docs/binutils/objdump.html

## Emulators & virtual machines

- **[QEMU]** — the key testing tool: boot your kernel without rebooting; gdb-stub, TCG, and KVM backends. — https://www.qemu.org/
- **[QEMU docs]** — user/system mode manuals. — https://www.qemu.org/docs/master/
- **[QEMU system gdb (docs)]** — using QEMU's `-s`/`-gdb` remote-debugging stub on a kernel. — https://www.qemu.org/docs/master/system/gdb.html
- **[Bochs]** — a highly configurable x86 emulator with a built-in debugger; good for very low-level testing. — https://bochs.sourceforge.net/
- **[DOSBox]** — runs legacy DOS software/apps; handy for vintage-OS testing. — https://www.dosbox.com/
- **[DOSBox-X]** — a more advanced, actively maintained DOSBox fork (better hardware & debug support). — https://dosbox-x.com/
- **[VirtualBox]** — Oracle's free desktop hypervisor (type-2); convenient cross-OS testing. — https://www.virtualbox.org/
- **[86Box]** — cycle-accurate emulation of old x86 hardware; great for testing real bootloaders/OSes. — https://86box.net/
- **[VMware Workstation Player]** — free-for-personal-use desktop hypervisor (redirects to the current product page). — https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion
- **[Unicorn Engine]** — a CPU emulator *framework* based on QEMU's cores, scriptable from Python/etc. — https://www.unicorn-engine.org/
- **[Quickemu]** — a friendly CLI wrapper around QEMU for running real OS ISOs if you want to guest-test your kernel in a distro. — https://github.com/quickemu-project/quickemu

## Hex editors

- **[ImHex]** — a modern, pattern-searchable hex editor with a custom data-inspection language. — https://imhex.werwolv.net/
- **[ImHex (GitHub)]** — source + releases. — https://github.com/WerWolv/ImHex
- **[wxHexEditor]** — a free hex editor designed for editing large disk/image files. — https://www.wxhexeditor.org/
- **[HxD]** — a polished freeware Windows hex editor (binary/boot-sector inspection). — https://mh-nexus.de/en/hxd/
- **[GHex]** — GNOME's simple hex editor for examining raw bytes of a file. — https://wiki.gnome.org/Apps/Ghex
- **[Bless]** — a full-featured GTK hex editor (large files, plugins). — https://github.com/afrantzis/bless
- **[binwalk]** — firmware/disk-image analysis: scans for embedded filesystems & signatures (great for OS images). — https://github.com/ReFirmLabs/binwalk

## Binary / ELF inspection tools

- **[readelf (binutils docs)]** — dump ELF headers, section/program headers, symbols — the key tool for understanding a kernel image. — https://sourceware.org/binutils/docs/binutils/readelf.html
- **[objcopy (binutils docs)]** — copy/transform object files (extract `.text` to flat binary, strip sections). — https://sourceware.org/binutils/docs/binutils/objcopy.html
- **[nm (binutils docs)]** — list symbols from an object/kernel (addresses for `System.map`). — https://sourceware.org/binutils/docs/binutils/nm.html
- **[strip (binutils docs)]** — remove debug/symbol tables to shrink kernels. — https://sourceware.org/binutils/docs/binutils/strip.html
- **[pyelftools]** — a pure-Python ELF parser for scripting your own binary analysis. — https://github.com/eliben/pyelftools
- **[pwntools]** — a CTF/exploit-dev toolkit with ELF parsing, assembly/disassembly, and process control. — https://github.com/Gallopsled/pwntools
- **[pwntools docs]** — the official documentation. — https://docs.pwntools.com/
- **[strace]** — trace system calls and signals of a process — invaluable for testing a kernel's syscalls. — https://strace.io/
- **[ltrace (man page)]** — trace library calls on top of strace's syscalls. — https://man7.org/linux/man-pages/man1/ltrace.1.html
- **[file(1) (man page)]** — identify file types/formats instantly when you're not sure what you've built. — https://man7.org/linux/man-pages/man1/file.1.html

## Kernel debugging tooling

- **[kgdb / kdb (Linux docs)]** — the kernel debugger: gdb attached to a live kernel over serial (current docs location). — https://docs.kernel.org/process/debugging/kgdb.html
- **[Debugging kernel & modules via gdb (Linux docs)]** — `gdb` against a running Linux kernel / vmlinux. — https://docs.kernel.org/process/debugging/gdb-kernel-debugging.html
- **[kprobes (Linux docs)]** — dynamically instrument arbitrary kernel functions. — https://www.kernel.org/doc/html/latest/trace/kprobes.html
- **[ftrace (Linux docs)]** — the kernel's built-in function tracer — zero-setup profile/breakpoint alternative. — https://www.kernel.org/doc/html/latest/trace/ftrace.html
- **[BPF Compiler Collection (BCC)]** — eBPF-based dynamic tracing tools (biosnoop, execsnoop, etc.). — https://github.com/iovisor/bcc
- **[bpftrace]** — a high-level one-liner language for eBPF tracing. — https://github.com/bpftrace/bpftrace
- **[crash utility]** — the post-mortem kernel crash-dump analyzer (reads vmcores with vmlinux). — https://github.com/crash-utility/crash

## Static analysis & sanitizers

- **[AddressSanitizer (ASan)]** — memory-error detector; pairs with QEMU/gdb to catch kernel heap bugs early. — https://clang.llvm.org/docs/AddressSanitizer.html
- **[GCC instrumentation options]** — GCC's `-fsanitize=…` flags (asan/tsan/ubsan) for your C builds. — https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
- **[clang static analyzer]** — LLVM's source-level analyzer built into clang. — https://clang-analyzer.llvm.org/
- **[clang-tidy]** — clang-based linter/analyser for C/C++ (modernize, bugprone checks). — https://clang.llvm.org/extra/clang-tidy/
- **[cppcheck]** — a fast standalone C/C++ static analyser (no build required). — https://cppcheck.sourceforge.io/
- **[Valgrind]** — dynamic analysis: Memcheck (errors), Callgrind (profiling) for user-space systems code. — https://valgrind.org/

## Profilers

- **[perf]** — the Linux perf profiler (sampling, hardware counters, tracepoints) for kernel & user code. — https://perf.wiki.kernel.org/
- **[FlameGraph]** — Brendan Gregg's scripts to turn `perf`/`strace` output into readable flame graphs. — https://github.com/brendangregg/FlameGraph
- **[gprof (binutils docs)]** — traditional call-graph profiling with `-pg` instrumented builds. — https://sourceware.org/binutils/docs/gprof/

## Version control

- **[Git]** — the standard VCS for kernel & systems work. — https://git-scm.com/
- **[Git documentation]** — book, references, and videos. — https://git-scm.com/doc
- **[GitHub]** — hosting + review + CI for most OS-dev projects. — https://github.com/
- **[GitLab]** — self-hostable Git hosting (home of Redox OS and many others). — https://about.gitlab.com/
- **[Fossil SCM]** — SQLite-backed all-in-one SCM with built-in tickets/wiki/CI. — https://fossil-scm.org/
- **[Mercurial]** — a fast, friendly DVCS (still used by some low-level projects). — https://www.mercurial-scm.org/

## CI for low-level / cross-compiled code

- **[GitHub Actions]** — free CI; *the* standard place to auto-cross-compile and even `qemu`-test a kernel on every push. — https://github.com/features/actions
- **[SourceHut builds]** — SourceHut's CI-by-email; minimal, git-first, good for from-scratch cross builds (returns anti-bot `418` to scripts; live in a browser). — https://builds.sr.ht/
- **[cross (Rust)]** — prebuilt cross-compilation environments for Rust targets, great inside CI. — https://github.com/cross-rs/cross
- **[crosstool-NG]** — the build tool used to generate your own cross-compilation toolchains for CI/OS dev. — https://crosstool-ng.github.io/
- **[phil-opp `blog_os` (example CI setup)]** — a real kernel repo that runs QEMU-based tests in CI; see its `.github/workflows/`. — https://github.com/phil-opp/blog_os

## Container / OS build tooling

- **[Buildroot]** — the standard tool for building a complete embedded/OS root filesystem + cross-toolchain + kernel from source. — https://buildroot.org/
- **[Buildroot manual]** — the official step-by-step manual. — https://buildroot.org/downloads/manual/manual.html
- **[Buildroot (GitHub)]** — source. — https://github.com/buildroot/buildroot
- **[Yocto Project]** — the big, layer-based embedded Linux build framework (BitBake + OpenEmbedded). — https://www.yoctoproject.org/
- **[Yocto docs]** — official documentation. — https://docs.yoctoproject.org/
- **[Linux From Scratch]** — build your own Linux system entirely from source — the ultimate hands-on "build your own OS" installation. — https://www.linuxfromscratch.org/
- **[LFS 12.x book]** — the current stable LFS book online. — https://www.linuxfromscratch.org/lfs/view/stable/
- **[Docker]** — containers for reproducible build environments/toolchains. — https://www.docker.com/
- **[Podman]** — a daemonless Docker-compatible container runtime. — https://podman.io/

---

*Maintained for the OSDev Learning Hub. Links verified September 2026; OSDev-wiki/sourcehut/noproxy-man7 URLs return anti-bot `403`/`418` to scripts but are confirmed live in a browser.*
