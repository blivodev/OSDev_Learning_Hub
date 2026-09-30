# Phoenix Code — project setup for Example_OS_Project

**Phoenix Code** (https://phcode.io) is the free, open-source successor to
Adobe Brackets. It's pre-configured for this project via the
[`.brackets.json`](.brackets.json) file in this folder — open this folder
with Phoenix Code and the editor picks up C/C++/Rust/Go/Makefile/etc.
highlighting and the file-exclude rules automatically.

## 1. Open the project
1. Launch **Phoenix Code** (installed as `Phoenix Code.exe`).
2. **File → Open Folder** → choose this `Example_OS_Project/` folder
   (or the whole `OSDev_Learning_Hub/` for the full learning resource).

## 2. Install recommended extensions
Press `Ctrl+Shift+Z` (or **View → Extension Manager**) and search for:
- **C/C++ language support** (clang-based highlighting for `.c`, `.c++`, `.h`)
- **Rust language** support (or use `rust-analyzer` via the built-in terminal)
- **Makefile / NASM / QEMU** syntax highlighting
- **Markdown Preview** (already built-in — great for these tutorials)

Phoenix Code ships with Git, a built-in Terminal, and Markdown preview out
of the box, so you can build and run straight from the editor:
1. Open the **Terminal** panel (View → Terminal).
2. Run `make run-c` to boot the C [kernel](../../GLOSSARY/kernel.md "The core program that owns the machine and manages hardware") in [QEMU](../../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing") — you don't need to leave
   the editor.

## 3. Editor config already in place
`.brackets.json` pre-sets:
- 4-space indentation (matches the kernel code)
- Line numbers + linting enabled
- Excludes `target/`, `build/`, `*.o`, `*.bin`, `*.iso` from the file tree
- Treats `.c++` as C++ for highlighting

## 4. Toolchain from inside the editor
The built-in Terminal inherits your shell. On Windows, run the C/C++ builds
from **WSL** (gcc/g++/ld live there):
```bash
# in the Phoenix Code terminal (WSL tab or `wsl` prefix):
make run-c      # boots the C kernel in QEMU
make run-cpp
```
> QEMU must be on the PATH of whatever shell the terminal uses. On the
> easiest setup, run Phoenix Code's terminal as WSL and `sudo apt install
> qemu-system-x86` once.
