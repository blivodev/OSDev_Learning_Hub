// Kernel.cs — A minimal "Hello World!" C# kernel (Cosmos-style).
//
// EDGE CASE EXPLANATION (read first):
//   C# compiles to managed IL and depends on a runtime (GC, JIT, BCL).
//   There is NO practical way for a beginner to hand-write a bare-metal
//   C# kernel from scratch the way you can in C/C++/Rust/Go. So per the
//   OSDev_Learning_Hub plan, we use **Cosmos OS** (an open source C#
//   operating-system kit) as the framework. You write normal-looking C#
//   and Cosmos (via NativeAOT / IL2CPU) compiles it down to a bootable OS.
//
// This file is a complete, commented Cosmos kernel. It is NOT the raw
// "write to 0xB8000 yourself" version — that's what the C/C++/Rust/Go
// kernels show. This shows the realistic C# path: a framework-provided
// Kernel base class with lifecycle methods.

using System;

// A Cosmos kernel subclasses Kernel and overrides lifecycle methods.
// BeforeRun() sets things up; Run() is the main loop that never returns.
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

        // A trivial command loop so you have something interactive.
        // `Kernel` never returns from Run() — it's your whole OS.
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
