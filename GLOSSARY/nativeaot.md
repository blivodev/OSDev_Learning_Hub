<!-- Glossary page — NativeAOT. Grounded in OSDev_Learning_Hub docs. -->

# NativeAOT

> **[Back to glossary index](README.md)** · Category: Toolchain & build

NativeAOT is .NET's ahead-of-time (AOT) compiler that turns managed Intermediate Language (IL) into native machine code — the mechanism Cosmos uses to make a C# kernel bootable.

## The short version
For a bare-metal kernel you can't run the .NET JIT — there's no OS to host it. NativeAOT compiles your C# IL *ahead of time* into a native executable with no runtime JIT necessary. It's what lets Cosmos ship actual machine code for the target CPU instead of IL that needs a runtime interpreter.

## Detailed explanation
Cosmos historically used **IL2CPU** — its own IL-to-x86 compiler — to translate managed code into native x86. Modern Cosmos builds on **NativeAOT**, .NET's ahead-of-time compilation technology (part of the .NET 7+ SDK), which takes the same IL and produces a native image. The result is that a Cosmos OS is real machine code running on the bare metal, not interpreted IL.

For ordinary .NET apps NativeAOT is a deployment option: `dotnet publish -r <rid> -p:PublishAot=true` emits a self-contained native executable with no JIT and faster startup. For Cosmos, that native-image capability is what turns the C# kernel (`Kernel.cs`) into code that can run without an OS. The hub compares it to C/C++/Rust/Go, which always compile to native machine code; C# *needs* this AOT step because its normal path is managed IL on a runtime.

The key contrast shown in `Example_OS_Project/csharp/README.md`: while C/C++/Rust/Go compile to *"native machine code"* with no runtime, C# compiles to *"managed IL"* and *"needs a runtime — yes (GC + BCL)."* NativeAOT is the bridge that removes the runtime for bare-metal deployment.

```mermaid
flowchart LR
    IL[Managed IL (C#)] --> AOT[NativeAOT / IL2CPU]
    AOT --> NAT[Native x86 machine code]
    NAT --> K[Bootable kernel on bare metal]
```

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/csharp/README.md` — the table that brands C# as needing *"Cosmos/NativeAOT"* for a bare-metal path.
- `Example_OS_Project/csharp/Kernel.cs` — the C# source that Cosmos + NativeAOT compiles to native.
- `Example_OS_Project/csharp/ExampleOS.csproj` — the Cosmos project shape.

## Watch / listen
- [Microsoft Learn — NativeAOT deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/) — free, authoritative
- [Microsoft Learn — .NET AOT compilation overview](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/tutorial) — free tutorial

## Related terms
- [il2cpu](il2cpu.md)
- [managed-il](managed-il.md)
- [cosmos](cosmos.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
