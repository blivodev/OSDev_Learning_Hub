# Path C# — C# → Operating System Development (Beginner)

> ⚠️ **Important edge case (per project plan):** There is **no** complete free "from-scratch bare-metal" book that a beginner can realistically follow in C#. C# compiles to **[managed IL](../GLOSSARY/managed-il.md "The intermediate language C# compiles to, which needs a runtime")** and relies on a runtime; bringing it to bare metal requires a *massive* framework. So per the plan, we do **not** synthesize a full C# OS-dev book — we keep the framework as the primary reference and provide a well-commented boilerplate + an explanation of *why*.

## Primary Resource

### Cosmos OS — C# Open-Source Managed Operating System
- **Where:** https://www.gocosmos.org/ | https://github.com/CosmosOS/Cosmos
- **License:** Open source (BSD)
- **Local copy:** [`Cosmos/`](Cosmos/) (full source)
- **What it is:** An "Operating System **Kit**" (OS Legos). You author your kernel in modern C#; [Cosmos](../GLOSSARY/cosmos.md "An open-source C# operating-system kit") (via [NativeAOT](../GLOSSARY/nativeaot.md ".NET's ahead-of-time compiler that turns IL into native code") / [IL2CPU](../GLOSSARY/il2cpu.md "Cosmos's original IL-to-x86 compiler")) compiles it down to a bootable ISO loaded by the **[Limine](../GLOSSARY/limine.md "A modern bootloader supporting Multiboot 2 and 64-bit kernels")** bootloader. Supports x64 and ARM64. Includes its own GC, scheduler, drivers, network, filesystem.
- **Why it's the choice for C#:** It's the only practical free path to *shipping a C# OS*, even if you're not hand-writing a bootloader.

## What you'll build in this path
A **Cosmos-style** C# kernel template: `Kernel.cs` with `Kernel.BeforeRun()` / `Kernel.Run()` lifecycle methods that print to the console, plus the `.csproj` and instructions. Because a genuinely hand-rolled C# bare-metal "Hello World" isn't feasible for a beginner, we ship this boilerplate with extensive comments explaining the framework boundary.

## Supporting material already in this hub
- Well-commented Cosmos-style boilerplate → [`Example_OS_Project/csharp/`](../Example_OS_Project/csharp/)
- Synthesized consolidated beginner guide (C# chapter = *why C# is different*) → [`synthesized_tutorials/06-csharp/`](../synthesized_tutorials/06-csharp/)

## Toolchain needed (see `Example_OS_Project/docs/setup.md`)
`.NET SDK` (present on the host), Cosmos DevKit, **Visual Studio 2022** (for the debugger — recommended), [QEMU](../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing") or VMware for running.
