<!-- Glossary page — IL2CPU. Grounded in OSDev_Learning_Hub docs. -->

# IL2CPU

> **[Back to glossary index](README.md)** · Category: Toolchain & build

IL2CPU is Cosmos OS's original compiler that translates .NET Intermediate Language (IL) into native x86 machine code.

## The short version
Before Cosmos moved to NativeAOT, IL2CPU was the tool that made a C# OS possible: it walked the managed IL bytes of your assembly and emitted equivalent x86 machine code, replacing the need for a JIT or a .NET runtime on bare metal. It's now largely superseded by NativeAOT, but it remains the historical heart of Cosmos and the name beginners will still see.

## Detailed explanation
Cosmos compiles C# *ahead of time* — for a bare-metal OS there's no room for an interpreter or JIT. IL2CPU reads the IL of every method reachable from your kernel's entry point and translates it directly into x86 assembly/machine code, producing a native image that can run without the .NET runtime. This is what historically let `Kernel.cs` (a normal C# class subclassing `Cosmos.System.Kernel`) become a bootable OS.

The hub's own C# documentation references this lineage: `Example_OS_Project/csharp/Kernel.cs` explains that *"Cosmos (via NativeAOT / IL2CPU) compiles it down to a bootable OS."* The slash is deliberate — Modern Cosmos builds on NativeAOT, with IL2CPU as the earlier, now-superseded implementation of the same idea (translating IL → native x86).

Because a C# kernel pokes hardware through Cosmos abstractions (e.g. `Console.WriteLine`), it's the compiler (IL2CPU/NativeAOT) plus the Cosmos hardware-abstraction layer that bridges the managed code to the bare machine — this is fundamentally different from the C/C++/Rust/Go kernels here, which write to VGA memory directly at `0xB8000`.

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/csharp/Kernel.cs` — *"Cosmos (via NativeAOT / IL2CPU)"* is the documented path to a bootable C# OS.
- `Example_OS_Project/csharp/README.md` — the table that positions C# on the *"needs Cosmos/NativeAOT"* row.
- `Example_OS_Project/csharp/ExampleOS.csproj` — the Cosmos project that Cosmos's compiler would process.

## Watch / listen
- [Cosmos OS — Official site](https://www.gocosmos.org/) — free, authoritative
- [GitHub — Cosmos IL2CPU source](https://github.com/CosmosOS/IL2CPU) — free source

## Related terms
- [nativeaot](nativeaot.md)
- [managed-il](managed-il.md)
- [cosmos](cosmos.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
