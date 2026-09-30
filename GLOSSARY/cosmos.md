<!-- Glossary page — Cosmos OS. Grounded in OSDev_Learning_Hub docs. -->

# Cosmos OS

> **[Back to glossary index](README.md)** · Category: Toolchain & build

Cosmos (C# Open Source Managed Operating System) is an open-source kit that lets you write an operating system's logic in C#.

## The short version
C# compiles to managed IL and needs a runtime (a garbage collector, the JIT, and the base class library) — bootstrapping all that by hand is a huge engineering project. Cosmos already did it: you subclass the `Kernel` class, override `BeforeRun()` and `Run()`, and Cosmos (via NativeAOT / IL2CPU) turns your C# into a bootable OS. The hub uses Cosmos as the honest free path to *"an OS in C#"*.

## Detailed explanation
The C# kernel is the documented **edge case** of the OSDev_Learning_Hub plan. Unlike C/C++/Rust/Go — which compile to native machine code and can poke `0xB8000` directly — C# targets Microsoft's .NET runtime. The comparison table in `Example_OS_Project/csharp/README.md` is explicit: C# *"needs a runtime — yes (GC + BCL)"* and *"Realistic bare-metal path: needs Cosmos/NativeAOT."*

So a beginner writes normal C# that subclasses Cosmos's `Kernel`:

```csharp
public class Kernel : Cosmos.System.Kernel
{
    protected override void BeforeRun()
    {
        Console.WriteLine("Cosmos booted successfully. Let's go!");
    }
    protected override void Run()
    {
        Console.WriteLine("Hello World!");
        while (true)   // Run() never returns — it's your whole OS
        {
            Console.Write("> ");
            string input = Console.ReadLine();
            // handle "help", "hello", "clear" ...
        }
    }
}
```

Building requires the **Cosmos DevKit** (Visual Studio 2022 + a project template that registers local NuGet feeds), then:
```bash
dotnet new install Cosmos.Templates
dotnet new cosmos -n MyOS
dotnet build              # Cosmos compiles your C# to native + ISO
qemu-system-i386 -cdrom bin/Debug/MyOS.iso
```

What you can't fully do here: the Cosmos debugger only works in Visual Studio + VMware, not QEMU, and you need VS2022 for the smoothest experience. The result is a *kit*-built OS rather than a hand-rolled one — but per the README, *"it's the only honest free path to 'an OS in C#' for a beginner."*

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/csharp/README.md` — the edge-case rationale, the comparison table, and the full Cosmos build/run steps.
- `Example_OS_Project/csharp/Kernel.cs` — a complete commented Cosmos kernel with `BeforeRun`/`Run` and a command loop.
- `Example_OS_Project/csharp/ExampleOS.csproj` — the shape of a Cosmos project (`StartupObject` = `Kernel`).
- Cosmos source is vendored for reading at `path_csharp_os/Cosmos/`.

## Watch / listen
- [Cosmos OS — Official site](https://www.gocosmos.org/) — free, authoritative
- [GitHub — Cosmos](https://github.com/CosmosOS/Cosmos) — free source

## Related terms
- [nativeaot](nativeaot.md)
- [il2cpu](il2cpu.md)
- [managed-il](managed-il.md)
- [Kernel](kernel.md)
- [QEMU](qemu.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
