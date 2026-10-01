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

## More C++ Tutorials
- **W3Schools: C++ Tutorial** — https://www.w3schools.com/cpp/ — quick, example-first introduction with an online compiler.
- **Programiz: C++ Tutorial** — https://www.programiz.com/cpp-programming — step-by-step modern C++ tutorials with runnable examples.
- **freeCodeCamp: How to Learn the C++ Programming Language** — https://www.freecodecamp.org/news/how-to-learn-the-c-programming-language/ — a written C++ introduction plus a curated list of the best free resources and video courses.

## C++ Guidelines & Style
- **C++ Core Guidelines** — https://isocpp.github.io/CppCoreGuidelines/ — the official, living set of rules for modern C++ (from Stroustrup & Sutter) — read the sections on memory, concurrency and resource management before writing systems code.
- **cppbestpractices (lefticus)** — https://github.com/lefticus/cppbestpractices — a practical, opinionated C++ best-practices collection distilled from years of C++ conference talks.
- **Google C++ Style Guide** — https://google.github.io/styleguide/cppguide.html — a widely-used, rigorous C++ style reference, including guidance on header hygiene and naming that keeps big codebases manageable.
- **isocpp.org C++ FAQ: Exceptions** — https://isocpp.org/wiki/faq/exceptions — the official FAQ on C++ exception handling, including the cost and stack-unwinding tradeoffs you must weigh before enabling exceptions in a freestanding kernel.

## Roadmap
- **roadmap.sh/cpp** — https://roadmap.sh/cpp — a visual, step-by-step C++ learning roadmap from basics through advanced/modern topics.

## More C++ OS Projects to Study
- **SerenityOS** — https://github.com/SerenityOS/serenity — one of the largest and most polished hobby OSes written almost entirely in modern C++, with a full GUI, browser and ports — an outstanding real-world corpus of systems C++.
- **WingOS** — https://github.com/Supercip971/WingOS — a small 64-bit microkernel hobby OS written in C++ with SMP support, a UAVF VFS, ext4/NVMe and its own UI library.

## C++ Freestanding & ABI Details
- **OSDev Wiki: Calling Global Constructors** — https://wiki.osdev.org/Calling_Global_Constructors — how to run C++ static constructors in a freestanding kernel by wiring up the `.init_array` — the missing runtime step the Bare Bones tutorial skips.
- **C++ Standards (WG21)** — https://www.open-std.org/jtc1/sc22/wg21/ — the official C++ standardization committee; track current and upcoming standards (C++20/23) that shape the language you write kernels in.

## C++ Tools & Compilation
- **Compiler Explorer (godbolt)** — https://godbolt.org/ — compile C++ on any compiler/version in the browser and inspect the generated assembly — essential for seeing RAII, virtual dispatch and exception overhead at the lowest level.
- **awesome-cpp** — https://github.com/fffaraz/awesome-cpp — the community's curated list of C++ libraries and frameworks across every domain.

## C++ Concurrency
- **cppreference: Concurrency support library** — https://en.cppreference.com/w/cpp/thread — the reference for `std::thread`, mutexes, condition variables, atomics, futures and async — the primitives you'll need when writing a multi-threaded kernel or scheduler.

## More C++ OS Projects to Study
- **managarm** — https://github.com/managarm/managarm — a pragmatic, capability-based microkernel OS written in C++ with fully asynchronous I/O, drivers and a userspace — a substantial real-world C++ kernel codebase.
- **skiftOS** — https://github.com/skiftOS/skift — a modern C++20 hobby OS (microkernel, graphics framework, UI toolkit, own stdlib) built from scratch — great modern-C++ OS reading.
- **PrintOS** — https://github.com/print3m/printos — a clean, educational 64-bit hobby kernel written in C++ (paging, IDT, heap, APIC, HPET) with readable, commented code.
- **hhuOS** — https://github.com/hhuOS/hhuOS — a small x86 OS written in C++ and assembler whose purpose is to show how OS-theory pieces fit together — often used in university OS courses.
- **awesome-osdev (leap0x7b)** — https://github.com/leap0x7b/awesome-osdev — a curated list of OS-dev resources including many C++ hobby kernels and tutorials.

## C++ Freestanding & ABI Details (more)
- **OSDev Wiki: C++ Exception Support** — https://wiki.osdev.org/C%2B%2B_Exception_Support — how to add (Itanium-ABI) C++ exception handling to your kernel by porting `libgcc_eh` / `libsupc++` — the runtime step after global constructors.
- **Itanium C++ ABI** — https://itanium-cxx-abi.github.io/cxx-abi/abi.html — the ABI most compilers (GCC/Clang) follow for exceptions, RTTI and symbol mangling — the spec you're implementing when you run C++ on bare metal.

## More C++ Tutorials & Channels
- **Handmade Hero** — https://handmadehero.org/ — Casey Muratori's famous complete game written from scratch in C/C++ with no libraries; the low-level, systems-first mindset transfers directly to OS-dev.
- **The Cherno (C++ YouTube course)** — https://www.youtube.com/@TheCherno — one of the most popular modern C++ YouTube series, teaching C++ from fundamentals up to engine-style low-level coding.
- **CppCon talks (YouTube)** — https://www.youtube.com/@CppCon — the official channel of the annual C++ conference; thousands of talks on modern C++, low-level and concurrency topics.
- **cppweekly (Jason Turner)** — https://www.youtube.com/@cppweekly — short, punchy weekly C++ news and technique videos, ideal for keeping up with modern-C++ idioms.
- **CPPQuiz** — https://cppquiz.org/ — a free interactive quiz that tests and teaches the subtle rules of C++ (value categories, overload resolution, casting) — great for systems-level precision.
- **C++ FQA** — http://yosefk.com/c++fqa/ — a sharp, opinionated critique of C++ and its design tradeoffs — useful for understanding the language's costs before committing a kernel to it.

## C++ Reference Topics (concurrency & lifecycle)
- **cppreference: Exceptions** — https://en.cppreference.com/w/cpp/language/exceptions — the language reference for exception handling, stack unwinding and `noexcept` — the rules behind the freestanding exceptions you'd add to a C++ kernel.
- **cppreference: RAII** — https://en.cppreference.com/w/cpp/language/raii — the reference for Resource Acquisition Is Initialization, the core idiom you'll lean on for leak-free kernel resource management.
- **Quick C++ Benchmark** — https://quick-bench.com/ — an online micro-benchmarking tool for comparing C++ compiler output and performance of snippets — handy for measuring kernel hot paths.
