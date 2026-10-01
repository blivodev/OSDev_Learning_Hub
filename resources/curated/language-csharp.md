# C# — Curated Learning & OS-Dev Resources

C# OS-dev centers on **Cosmos OS** and its `IL2CPU` compiler, which turns C# IL into native machine code so you can boot a C# kernel on bare metal. Modern .NET (Native AOT) and `unsafe` pointers make the low-level story increasingly relevant. All links verified reachable.

## C# Tutorials (beginner onward)
- **C# Guide (Microsoft Learn)** — https://learn.microsoft.com/en-us/dotnet/csharp/ — the official C# documentation hub; the canonical course for learning C#.
- **A Tour of C#** — https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp — the official interactive introduction to the language.
- **C# for Beginners (video course)** — https://learn.microsoft.com/en-us/shows/csharp-for-beginners — Microsoft's free video series for absolute beginners.
- **Tour of C#: Interactive tutorials** — https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/tutorials/ — hands-on, runnable intro lessons in the browser.
- **Codecademy: Learn C#** — https://www.codecademy.com/learn/learn-c-sharp — a structured interactive C# course.
- **C# language reference** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/ — the authoritative language reference for syntax and semantics.

## C# Low-Level, Pointer & .NET Internals
- **Microsoft Learn: Unsafe code, pointer types** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code — the official guide to `unsafe` blocks and direct pointer access in C# — where C# starts to meet bare metal.
- **Pointer-related operators** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/pointer-related-operators — `&`, `*`, `->`, `[]` on pointers in C# — the low-level toolkit.
- **Matt Warren: "Is C# a low-level language?"** — https://mattwarren.org/2019/03/01/Is-CSharp-a-low-level-language/ — an excellent analysis of how close C#/.NET actually sits to the metal.
- **System.Runtime.InteropServices (.NET API)** — https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices — the interop/P/Invoke API surface used for pre-existing native libraries and memory.
- **source.dot.net** — https://source.dot.net/ — Microsoft's browsable, source-linked view of the entire .NET runtime (CoreCLR) — read the real implementation of the CLR that runs your C#.

## .NET Native AOT & Runtime Engineering
- **Native AOT deployment overview** — https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/ — official documentation on compiling C# ahead-of-time into a native executable with no JIT — the modern path to running C# without an OS runtime.
- **NativeAOT compile pipeline (CoreCLR docs)** — https://github.com/dotnet/runtime/blob/main/src/coreclr/nativeaot/docs/compiling.md — the technical documentation of how NativeAOT compiles IL to native code — the direct conceptual cousin of IL2CPU.
- **.NET trimming / self-contained** — https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/trim-self-contained — reducing the runtime footprint, relevant when you want minimal C# boot images.
- **dotnet/runtime** — https://github.com/dotnet/runtime — the .NET runtime source: CoreCLR, managed libraries, NativeAOT — the foundation C# OS work builds upon.
- **dotnet/coreclr** — https://github.com/dotnet/coreclr — the historical CoreCLR repository (the runtime engine) for deep internal study.

## C# Compiler & Tooling
- **dotnet/roslyn** — https://github.com/dotnet/roslyn — the C# compiler (Roslyn) source — understand how your C# is broken down and lowered before compilation to native.
- **IL2CPU (CosmosOS)** — https://github.com/CosmosOS/IL2CPU — *the* C#→native AOT compiler that compiles IL into machine language so C# can run on bare metal — the engine behind every Cosmos kernel.
- **IL2CPU (Wikipedia)** — https://en.wikipedia.org/wiki/IL2CPU — background on the IL2CPU compiler and its role in C# OS development.

## Cosmos OS & C# OS-Dev
- **Cosmos — Write an OS in modern C#** — https://www.gocosmos.org/ — the official site for Cosmos, the C#/"managed" OS construction kit.
- **Cosmos (GitHub)** — https://github.com/CosmosOS/Cosmos — source and docs for the Cosmos kit (kernel, projects, compiler integration). Wiki: https://github.com/CosmosOS/Cosmos/wiki.
- **Cosmos: Getting Started** — https://github.com/CosmosOS/Cosmos/wiki/Getting-Started — the official first-steps tutorial to build and boot your first C# OS in a VM.
- **OSDev Wiki: C Sharp** — https://wiki.osdev.org/C_Sharp — the OSDev Wiki's language page for C# OS-dev guidance and history.
- **OSDev Wiki: C Sharp Bare Bones** — https://wiki.osdev.org/C_Sharp_Bare_Bones — the canonical OSDev tutorial for writing a minimal C# (Cosmos-style) kernel — start here for C# OS-dev.

## More C# Tutorials
- **W3Schools: C# Tutorial** — https://www.w3schools.com/cs/ — a quick, example-first C# introduction with a runnable online code editor.
- **Programiz: C# Tutorial** — https://www.programiz.com/csharp-programming — step-by-step C# tutorials from syntax through OOP, with runnable examples.

## C# Low-Level: Memory, Pointers & Span
- **Span\<T\> (.NET API)** — https://learn.microsoft.com/en-us/dotnet/api/system.span-1 — the zero-allocation, ref-struct memory type that makes C#'s most efficient low-level code (and unsafe interop) possible.
- **Memory and Span usage guidelines** — https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans/memory-t-usage-guidelines — official guidance on when and how to use `Memory<T>`/`Span<T>` — the modern idiom for writing high-performance C# near the metal.
- **Tasks & Parallel Programming (TPL)** — https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-parallel-library-tpl — the official documentation for .NET's concurrency model — tasks, async/await, parallel loops and cancellation.
- **C# asynchronous programming (Microsoft Learn)** — https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/ — the official overview of async/await in C#, including how the task-based model maps onto threads and the thread pool.

## C# Compiler, Runtime & IL Tooling
- **System.Reflection.Emit** — https://learn.microsoft.com/en-us/dotnet/api/system.reflection.emit — the API for generating IL at runtime — directly relevant to understanding (and writing) AOT/IL-transpiling toolchains like IL2CPU.
- **SharpLab** — https://sharplab.io/ — an online C# playground that shows the lowered IL and de-compiled output of any snippet — the best way to see exactly what your C# compiles down to.
- **Try .NET** — https://dotnet.microsoft.com/en-us/platform/try-dotnet — Microsoft's in-browser interactive C#/.NET environment for running snippets without installing anything.
- **dotnet/csharplang (proposals & spec)** — https://github.com/dotnet/csharplang — the official C# language design repository: current spec, accepted and in-progress proposals — how the language evolves.
- **ILSpy** — https://github.com/icsharpcode/ILSpy — the open-source .NET decompiler/assembly browser — read any compiled C#/IL back to readable source, ideal for studying how the runtime and Cosmos are built.
- **Common Intermediate Language (CIL) — Wikipedia** — https://en.wikipedia.org/wiki/Common_Intermediate_Language — a solid overview of the IL instruction set and metadata that every .NET language — and IL2CPU — compiles down to.

## .NET Internals Blogs
- **Matt Warren — .NET Internals series** — https://mattwarren.net/ — deep, well-cited articles on CLR internals, IL, JIT behavior and the GC.
- **Eric Lippert — Fabulous adventures in coding** — https://ericlippert.com/ — the former C# language-team member's blog on C# language design and semantics — essential for truly understanding the language.
- **Konrad Kokosa — .NET GC & Memory internals** — https://tooslowexception.com/ — authoritative articles and book excerpts on the .NET garbage collector and memory internals.

## More C# OS-Dev & Bare-Metal
- **MOSA (Mosa-Project)** — https://github.com/mosa/MOSA-Project — the Managed Operating System Alliance: an AOT compiler and toolkit for writing bare-metal OS code in C# (a counterpart to Cosmos/IL2CPU).
- **Cosmos gen3: NativeAOT patcher (valentinbreiz)** — https://github.com/valentinbreiz/nativeaot-patcher — the proof-of-concept that replaced Cosmos's IL2CPU transpiler with the official .NET NativeAOT compiler — the direct conceptual ancestor of modern Cosmos-gen3 bare-metal C#.
- **Medli3** — https://github.com/Arawn-Davies/medli3 — a bare-metal C# operating system built on Cosmos gen3 (NativeAOT), booting to a color console shell on x64/ARM64 — a clean, modern C# OS to read.

## More C# / .NET Internals Resources
- **The .NET Blog (devblogs.microsoft.com/dotnet)** — https://devblogs.microsoft.com/dotnet/ — Microsoft's official engineering blog covering .NET internals, new APIs, runtime and AOT improvements — a steady stream of deep, first-party content.
- **dotnet/corert** — https://github.com/dotnet/corert — the original CoreRT ahead-of-time compilation project that led to modern NativeAOT — useful history and technical detail on AOT IL-to-native compilation for bare-metal C#.
- **Microsoft Learn: .NET GC fundamentals** — https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals — the official explanation of the .NET garbage collector, generations, finalization and roots — understanding this is key to predictable behavior in a C# kernel.

## More C# Language Reference Topics
- **Microsoft Learn: C# iteration statements** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements — `for`, `foreach`, `while` — control-flow reference handy when writing tight kernel loops.
- **Microsoft Learn: C# selection statements** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/selection-statements — `if`, `switch` and pattern-matching reference.
- **Microsoft Learn: C# integral numeric types** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types — the `sbyte`→`ulong`/`byte`/`nint` type table — what you're using for registers, addresses and sizes in low-level C#.
- **Microsoft Learn: C# stackalloc** — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/stackalloc — allocating on the stack (fast, GC-free) — the C# idiom closest to writing C-style buffer code in-kernel.
- **Microsoft Learn: what's new in C# 12** — https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-12 — and the series for C# 9–11 (https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-11) — tracking the modern language features you can bring to bare-metal C#.
