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
