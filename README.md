# OSDev_Learning_Hub

A **comprehensive, beginner-friendly Operating System development learning resource and workspace.**

This repository brings together the best **legally free** OS-development resources, converts them into an organized documentation tree, synthesizes a brand-new consolidated beginner's guide, and ships a complete `Example_OS_Project` — a minimal bootable OS that prints **"Hello World!"** — implemented in **C, C++, Rust, Go, and C#**.

---

## 📚 Repository Layout

```
OSDev_Learning_Hub/
├── path_c_os/            # Path A:  C  → OS development resources
├── path_cpp_os/          # Path C:  C++ → OS development resources
├── path_rust_os/         # Path B:  Rust → OS development resources
├── path_go_os/           # Path Go: Go  → OS development resources
├── path_csharp_os/       # Path C#: C#  → OS development resources (Cosmos)
├── resources/            # Misc. reference material & links
├── synthesized_tutorials/# NEW consolidated beginner's guide (original)
└── Example_OS_Project/   # Minimal bootable "Hello World!" OS in 5 languages
    ├── c/                #   C kernel  (VGA text mode + multiboot stub)
    ├── cpp/              #   C++ kernel (extern "C" entry)
    ├── rust/             #   Rust kernel (no_std, bootimage)
    ├── go/               #   Go kernel  (gccgo multiboot)
    ├── csharp/           #   C# kernel  (Cosmos-like template)
    ├── build/            # Build artifacts
    ├── docs/             # Build & run guide (setup.md, etc.)
    └── Makefile / build.sh
```

---

## 📖 Phase 1 — Selected Resources

| Path | Language | Primary Free Resource | License / Cost | Notes |
|------|----------|----------------------|----------------|-------|
| **A** | C | [Operating Systems: From 0 to 1](https://github.com/tuhdo/os01) (Doh Tu) | Free (GitHub PDF) | Book: x86 asm, ELF, linking, bare-metal C |
| **A** | C | [OSDev Wiki - Bare Bones](https://wiki.osdev.org/Bare_Bones) | Open wiki | The canonical minimal-kernel tutorial |
| **B** | Rust | [Writing an OS in Rust](https://os.phil-opp.com/) (Phil Opp) | Free (CC-BY-NC) | The most famous free Rust OS blog series |
| **C** | C++ | [OSDev Wiki - Bare Bones (C++)](https://wiki.osdev.org/Bare_Bones) | Open wiki | `extern "C"` kernel entry point |
| **Go** | Go | [OSDev Wiki - Go Bare Bones](https://wiki.osdev.org/Go_Bare_Bones) | Open wiki | gccgo freestanding kernel |
| **C#** | C# | [Cosmos OS](https://www.gocosmos.org/) | Open source (BSD) | C# operating-system **kit** (not bare metal by hand) |

> **Edge case applied:** For **C#**, no single complete "from-scratch bare-metal" free book exists that a beginner could realistically follow (C# compiles to managed IL, so a real bare-metal kernel needs a massive framework like Cosmos/NativeAOT). Per the plan, we **do not synthesize** a full C# OS-dev book; we keep Cosmos as the primary reference and provide a well-commented boilerplate + explanation of *why* (see `path_csharp_os/` and `synthesized_tutorials/03-csharp/`).

---

## 🚀 Phase 6 — Hello World OS

The `Example_OS_Project` contains a minimal bootable OS for each language.

**✅ Verified:** the **C** and **C++** kernels build to valid Multiboot v1
kernels (`grub-file` confirms) and **boot in QEMU, printing "Hello World!"** —
the VGA text buffer was read back from the running emulator to prove it.
A reusable harness does this in one command:

```bash
Example_OS_Project/tools/boot-test.sh c      # build + boot C  kernel, show screen text
Example_OS_Project/tools/boot-test.sh cpp    # build + boot C++ kernel, show screen text
```

- **C / C++ / Go** kernels boot via a **Multiboot** GRUB-style stub (GNU `as`).
- **Rust** kernel is a verified `no_std` kernel; the bootable-image step needs
  a nightly toolchain + `cargo bootimage`.
- **C#** uses a **Cosmos-style** kernel template (source + explanation).

Build & run with QEMU from inside `Example_OS_Project`:

```bash
make            # builds all kernels
make run-c      # boots the C kernel in QEMU
make run-cpp
make run-rust
make run-go
make iso-c      # builds a bootable ISO for the C kernel
```

---

## ⚙️ Toolchain

See [`Example_OS_Project/docs/setup.md`](Example_OS_Project/docs/setup.md) for a full environment setup guide (GCC, NASM, Rust nightly + `bootimage`, Go/gccgo cross-compiler, QEMU, Make).

---

## 🔒 Remotes

Private mirrors of this repository:

- **GitHub:** https://github.com/YOUR_USERNAME/OSDev_Learning_Hub (private)
- **Gitea:**  https://git.example.com/YOUR_USERNAME/OSDev_Learning_Hub (private)

---

*Created by Hermes Agent. All external resources remain the property of their respective authors and are included under their open licenses.*
