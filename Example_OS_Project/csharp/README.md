# C# kernel — build & run (Cosmos)

> This path is the **edge case** documented in the OSDev_Learning_Hub plan:
> C# has no practical hand-rolled bare-metal path for a beginner, so we
> use the [Cosmos OS kit](../../GLOSSARY/cosmos.md "An open-source C# operating-system kit") as the framework and explain why.

## Why C# is different from C/Rust/Go
| | C / C++ | Rust | Go | C# |
|---|---------|------|----|----|
| Compiles to | native machine code | native machine code | native (via gccgo) | **[managed IL](../../GLOSSARY/managed-il.md "The intermediate language C# compiles to, which needs a runtime")** |
| Needs a runtime? | no (`-ffreestanding`) | no (`no_std`) | minimal (stubs) | **yes — GC + BCL** |
| Can poke [0xB8000](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written") directly? | yes | yes (`unsafe`) | yes (`unsafe`) | not as a beginner |
| Realistic bare-metal path | full control | full control | stub + gccgo | **needs [Cosmos](../../GLOSSARY/cosmos.md "An open-source C# operating-system kit")/[NativeAOT](../../GLOSSARY/nativeaot.md ".NET's ahead-of-time compiler that turns IL into native code")** |

C# targets Microsoft's **.NET runtime**. Bootstrapping that runtime on bare
metal is a huge engineering project — which is exactly what **Cosmos OS**
already did. So the beginner-friendly C# path is: *let Cosmos do the
[bootloader](../../GLOSSARY/bootloader.md "A small program that loads your kernel into memory and jumps to it") + runtime, and write your OS logic in familiar C#.*

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


## Watch and learn

Videos matched to building an OS in C# and .NET with Cosmos, the kit this folder uses.

- [Cosmos Tutorial Part 1 - Setting Up And First Command!](https://www.youtube.com/watch?v=RTkeqkFzC3w) — hands-on Cosmos setup and the first command loop, mirroring the `Kernel.cs` in this folder.
- [Write Your Own 64-bit Operating System Kernel #1 - Boot code and multiboot header](https://www.youtube.com/watch?v=FkrpUaGThTQ) — the bare-metal kernel lifecycle that Cosmos automates for you, shown in C.
- [How does an OS boot? //Source Dive// 001](https://www.youtube.com/watch?v=KkenLT8S9Hs) — what really happens between pressing power and your Cosmos kernel's `Run` method.
- [QEMU/KVM for absolute beginners](https://www.youtube.com/watch?v=BgZHbCDFODk) — how to run the VM that boots your Cosmos ISO.
