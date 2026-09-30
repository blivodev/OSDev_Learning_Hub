# Chapter 05 — Building "Hello World!" in C# (and why it's an edge case)

*Original content written for OSDev_Learning_Hub — walks through the real,
documented code in `Example_OS_Project/csharp/`.*

## What you'll have at the end
A C# [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware"), built with the **Cosmos OS kit**, that boots and drops you into
an interactive prompt:
```
Cosmos booted successfully. Let's go!
Hello World!
Welcome to your very own operating system (C# edition).
> _
```
Before anything else, the honest headline this chapter teaches: **C# has no
practical hand-rolled bare-metal path for a beginner.** Every language so far
(C, C++, Rust, Go) compiles to *native machine code* and hands you the raw
`0xB8000` framebuffer. C# compiles to **[managed IL](../../GLOSSARY/managed-il.md "The intermediate language C# compiles to, which needs a runtime")** and needs a runtime —
garbage collector, JIT, base class library — and bootstrapping that runtime on
bare metal is a huge project. So, per the OSDev_Learning_Hub plan, the C#
chapter is the **edge case**: you use the **[Cosmos OS kit](../../GLOSSARY/cosmos.md "An open-source C# operating-system kit")** as the framework,
and write your OS logic in familiar C#.

## The flow, in one picture

```mermaid
flowchart LR
    A[You write Kernel.cs<br/>subclass of Cosmos kernel] --> B["Cosmos/NativeAOT compiles<br/>your C# IL to native code"]
    B --> C["protected override BeforeRun()<br/>runs once"]
    C --> D["protected override Run()<br/>main loop, never returns"]
    D --> E[Console.WriteLine Hello World!]
    E --> F[command loop:<br/>help / hello / clear]
    F --> G[Kernel never returns from Run]
```
Where the C/C++/Rust/Go flow gave you `boot.s → your entry point → 0xB8000`,
here the *framework* is the bootloader and the runtime. You never touch
`0xB8000`; you write `Console.WriteLine` like any other C# app, and Cosmos does
the rest.

## Step 1 — Why C# is different from C/Rust/Go

|                        | C / C++            | Rust              | Go                     | C#                          |
|------------------------|--------------------|-------------------|------------------------|-----------------------------|
| Compiles to            | native machine code| native machine code | native (via gccgo) | **managed IL**          |
| Needs a runtime?       | no (`-ffreestanding`) | no (`no_std`)    | minimal (stubs)       | **yes — GC + BCL**      |
| Can poke 0xB8000 directly? | yes            | yes (`unsafe`)    | yes (`unsafe`)        | not as a beginner       |
| Realistic bare-metal path | full control    | full control      | stub + gccgo          | **needs [Cosmos](../../GLOSSARY/cosmos.md "An open-source C# operating-system kit")/[NativeAOT](../../GLOSSARY/nativeaot.md ".NET's ahead-of-time compiler that turns IL into native code")** |

The column that matters is *"Needs a runtime?"*. C++ you met: exceptions and
RTTI needed a runtime, so you compiled them out with `-fno-exceptions
-fno-rtti`. Go you met: its GC and scheduler needed a runtime, so you stubbed
it with empty symbols. **C# is the end of that road** — the runtime is not an
optional feature you can turn off; it's the entire execution model. The CLR
(Common Language Runtime) is a virtual machine with a JIT, a precise garbage
collector, and a huge base class library. Nothing useful survives if you
"just turn it off." So you don't turn it off — you *bring a runtime with you*,
and Cosmos *is* that runtime, compiled ahead-of-time to native code.

The beginner-friendly C# path, then, is: **let Cosmos do the bootloader and
the runtime; write your OS logic in familiar C#.** `ExampleOS.csproj` even
notes that Cosmos compiles via [NativeAOT](../../GLOSSARY/nativeaot.md ".NET's ahead-of-time compiler that turns IL into native code") / [IL2CPU](../../GLOSSARY/il2cpu.md "Cosmos's original IL-to-x86 compiler") — it turns your IL into a
bootable, native OS while you keep writing `Console.*`.

## Step 2 — `Kernel.cs`: a Cosmos kernel, not a hand-rolled one

```csharp
public class Kernel : Cosmos.System.Kernel
{
    // Runs once before the main Run() loop.
    protected override void BeforeRun()
    {
        Console.WriteLine("Cosmos booted successfully. Let's go!");
    }

    // The main loop. In Cosmos this is effectively your OS's "start".
    protected override void Run()
    {
        Console.WriteLine("Hello World!");
        Console.WriteLine("Welcome to your very own operating system (C# edition).");

        while (true)
        {
            Console.Write("> ");
            string input = Console.ReadLine();
            if (input == "help")
                Console.WriteLine("Commands: help, hello, clear");
            else if (input == "hello")
                Console.WriteLine("Hello from your Cosmos OS!");
            else if (input == "clear")
                Console.Clear();
            else
                Console.WriteLine($"Unknown command: {input}");
        }
    }
}
```

Compare its lifecycle to what you've seen everywhere else:

- **`Kernel : Cosmos.System.Kernel`** — you subclass a base class instead of
  defining a bare `_start`/`kernel_main` function. The "entry point" is a
  *framework-provided* object model.
- **`BeforeRun()`** — runs once, like the setup the other languages' entry
  points do by hand (clearing the screen, initializing). 
- **`Run()`** — the main loop, "effectively your OS's start". Like every
  kernel, **`Kernel` never returns from `Run()`**; it's your whole OS, so it
  loops forever handling input.
- **No `0xB8000`** — instead of raw framebuffer writes, it uses
  `Console.WriteLine`. Cosmos routes `Console` to the real video hardware for
  you. This is both the comfort and the trade-off: you lose the raw hardware
  lesson, but you get an OS you can actually extend quickly.

The project file (`ExampleOS.csproj`) shows the shape: `.NET` target, no `Main`
(so `StartupObject` is set to `Kernel` because Cosmos uses `Kernel.Run()`, not
`Main()`), and — in a real Cosmos install — `PackageReference` entries for
`Cosmos.System` and `Cosmos.Build` that resolve from the Cosmos DevKit's local
feeds.

## Step 3 — The memory-model comparison

Across five languages you've now touched the same `0xB8000` — and seen how
each one views raw memory:

- **C/C++** — `#define VGA_SCREEN ((unsigned short*)0xB8000)` and dereference
  it: a raw pointer is just an address. Full control, zero safety.
- **Rust** — `0xB8000 as *mut u16`, but every read/write must be inside
  `unsafe {}` with a safety comment: memory safety is enforced by the
  compiler, not convention.
- **Go** — Go has no safe pointer arithmetic; the `0xB8000` poke needs
  `unsafe.Pointer`, and the reference implementation even leaves it as a
  comment to keep the safe-mode code clean.
- **C#** — you don't poke memory at all. Managed references are handles, and
  memory is owned by the GC. Poking raw memory is possible (C# has an
  `unsafe` keyword) but is *not* how you work with this language — Cosmos
  gives you `Console` abstractions instead.

That progression *is* the lesson: as the language manages more for you ([GC](../../GLOSSARY/garbage-collection.md "Automatic memory reclamation used by managed runtimes"),
safety, runtime), direct hardware I/O moves further from your reach — until,
with C#, it moves behind a framework.

## Step 4 — Build & run (requires Visual Studio 2022 + Cosmos DevKit)

```bash
# 1. Install the Cosmos DevKit (registers templates + local NuGet feeds)
# 2. Create a Cosmos project:
dotnet new install Cosmos.Templates
dotnet new cosmos -n MyOS
#   -or- paste Kernel.cs / ExampleOS.csproj into a new project
# 3. Build a bootable ISO (Cosmos compiles your C# to native + ISO):
dotnet build
# 4. Run it in a VM. Cosmos normally launches VMware; for QEMU:
qemu-system-i386 -cdrom bin/Debug/MyOS.iso
```

Then QEMU shows the prompt shown at the top of this chapter.

## Realistic expectations (honest limits)

- The **Cosmos debugger** only fully works in Visual Studio + VMware, not
  QEMU.
- Smoothest experience needs **Visual Studio 2022**.
- This gives you a **kit-built OS**, not a hand-rolled one — but it's the only
  honest free path to "an OS written in C#" for a beginner. The raw
  hardware lessons you got in C/C++/Rust/Go are exactly the ones C# hands to
  the framework.

## Verification

What was actually verified for this chapter:

- `Kernel.cs` follows the **real Cosmos API**: it subclasses `Cosmos.System
  .Kernel` and overrides `BeforeRun()`/`Run()` as the framework expects — no
  invented methods.
- `ExampleOS.csproj` uses the **Cosmos project shape** (`StartupObject=Kernel`,
  no `Main`), with the `Cosmos.System` / `Cosmos.Build` packages documented as
  resolving from the DevKit's local feeds.
- **The C# kernel was not built/booted here** — it inherently requires Visual
  Studio 2022 + the Cosmos DevKit, which this environment does not have. This
  chapter is verified at the *source-review* level (API-correct, follows the
  documented Cosmos workflow), and the required toolchain is stated plainly
  rather than faked.

> **Bridge to OS concepts:** C# is the clearest object lesson in **what a
> runtime actually is and why it's hard** — the exact gap C++ avoided with
> `-fno-exceptions -fno-rtti`, Go papered over with stubs, and C never had
> (concepts/02 **[memory management](../../GLOSSARY/memory-management.md "How a kernel tracks used and free RAM and hands it out safely")**, concepts/01 **bootloaders and
> [Multiboot](../../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002")**). Where the other languages reached the **[VGA framebuffer](../../GLOSSARY/vga-framebuffer.md "The memory at 0xB8000 where screen text is written")**
> directly (concepts/04), C# delegates that hardware I/O to a framework —
> which is exactly why, when you *must* control hardware bit-by-bit, you reach
> for C, and when you just want a working OS quickly, C# + Cosmos wins.

---

## Watch and learn

- [The Operating System Construction Kit: Cosmos! [Cosmos Quest #1]](https://www.youtube.com/watch?v=Khff1xxyEHI) — A hands-on demo of writing C# with the Cosmos OS kit and booting it as a real operating system — the exact "build an OS with C#" workflow this chapter documents.
- [Exploring .NET's Memory Management — A Trip Down Memory Lane (JetBrains)](https://www.youtube.com/watch?v=9FEfy9y0fFQ) — How the .NET GC, CLR, and intermediate language manage memory and hidden allocations — the runtime reality behind the managed IL your C# kernel compiles to.
- [.NET GC - part 1 (Maoni Stephens)](https://www.youtube.com/watch?v=vqMky3uw4uI) — The .NET Garbage Collector's lead engineer explains generations, marking, and compaction — why a managed runtime like the one Cosmos brings along exists in the first place.
