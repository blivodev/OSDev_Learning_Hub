# C# kernel — build & run (Cosmos)

> This path is the **edge case** documented in the OSDev_Learning_Hub plan:
> C# has no practical hand-rolled bare-metal path for a beginner, so we
> use the **Cosmos OS kit** as the framework and explain why.

## Why C# is different from C/Rust/Go
| | C / C++ | Rust | Go | C# |
|---|---------|------|----|----|
| Compiles to | native machine code | native machine code | native (via gccgo) | **managed IL** |
| Needs a runtime? | no (`-ffreestanding`) | no (`no_std`) | minimal (stubs) | **yes — GC + BCL** |
| Can poke 0xB8000 directly? | yes | yes (`unsafe`) | yes (`unsafe`) | not as a beginner |
| Realistic bare-metal path | full control | full control | stub + gccgo | **needs Cosmos/NativeAOT** |

C# targets Microsoft's **.NET runtime**. Bootstrapping that runtime on bare
metal is a huge engineering project — which is exactly what **Cosmos OS**
already did. So the beginner-friendly C# path is: *let Cosmos do the
bootloader + runtime, and write your OS logic in familiar C#.*

## What's in this folder
- `Kernel.cs` — a complete Cosmos kernel (BeforeRun + Run lifecycle, with a tiny command loop).
- `ExampleOS.csproj` — the project file shape a Cosmos kernel uses.

## Build & run (requires Visual Studio 2022 + Cosmos DevKit)
```bash
# 1. Install the Cosmos DevKit (downloads from the Cosmos website)
#    This registers Cosmos project templates and local NuGet feeds.

# 2. Create a Cosmos project. With the DevKit installed:
dotnet new install Cosmos.Templates
dotnet new cosmos -n MyOS
#   -or- paste Kernel.cs / ExampleOS.csproj into a new project.

# 3. Build a bootable ISO (Cosmos compiles your C# to native + ISO):
dotnet build

# 4. Run it in a VM. Cosmos normally launches VMware; for QEMU:
qemu-system-i386 -cdrom bin/Debug/MyOS.iso
```

Then you'll see in QEMU:
```
Cosmos booted successfully. Let's go!
Hello World!
> _
```

## Realistic expectations
- The **Cosmos debugger** only fully works in Visual Studio (+ VMware), not QEMU.
- Building requires **Visual Studio 2022** for the smoothest experience.
- This gives you a *kit*-built OS, not a hand-rolled one — but it's the only
  honest free path to "an OS in C#" for a beginner.

> Full Cosmos source is vendored in `path_csharp_os/Cosmos/` if you want to
> read how the framework itself is built.
