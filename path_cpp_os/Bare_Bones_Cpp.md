# OSDev Wiki — Bare Bones (C++ variant)

> Source: https://wiki.osdev.org/Bare_Bones (C++ section) — community-reviewed.
> This is a **converted/summarized** reference copy for offline reading.

---

## Writing a kernel in C++

Writing a kernel in C++ is easy, but **not all language features are available**:
- **Exceptions** require special runtime support → usually disabled (`-fno-exceptions`).
- **Memory allocation / RTTI** need runtime support → disabled (`-fno-rtti`).

The one essential trick: **give `kernel_main` [C linkage](../GLOSSARY/extern-c.md "C++ keyword giving a function C linkage so its name isn't mangled")** with `extern "C"`. Without it, the compiler mangles the symbol name (adds type info), which breaks the call from the assembly stub.

```cpp
#include <stdint.h>
#include <stddef.h>

// VGA text-mode driver (same as C).
static const size_t VGA_WIDTH  = 80;
static const size_t VGA_HEIGHT = 25;
static uint16_t* const VGA_MEMORY = (uint16_t*) 0xB8000;

// MUST use C linkage so the bootloader stub can call this exact symbol.
extern "C" void kernel_main() {
    // clear screen
    for (size_t y = 0; y < VGA_HEIGHT; y++)
        for (size_t x = 0; x < VGA_WIDTH; x++) {
            const size_t index = y * VGA_WIDTH + x;
            VGA_MEMORY[index] = (uint16_t) 0x0F00 | ' ';
        }
    // print "Hello World!"
    const char* msg = "Hello World!";
    size_t i = 0;
    while (msg[i] != '\0') {
        VGA_MEMORY[i] = (uint16_t) 0x0F00 | (uint8_t) msg[i];
        i++;
    }
}
```

Save as `kernel.c++`.

## Compile

```bash
i686-elf-g++ -c kernel.c++ -o kernel.o -ffreestanding -O2 -Wall -Wextra -fno-exceptions -fno-rtti
```

(`g++` instead of `gcc`, plus `-fno-exceptions -fno-rtti` for a [freestanding](../GLOSSARY/freestanding.md "Code compiled assuming no OS or standard library exists") C++ kernel.)

The bootstrap assembly (`boot.s`), [linker](../GLOSSARY/linker.md "Merges object files into one image at a chosen address") script, and [QEMU](../GLOSSARY/qemu.md "A free emulator you can boot your kernel in for testing") test are identical to the C Bare Bones tutorial — see `path_c_os/Bare_Bones_C.md`.

---

## Key takeaways (beginner)
1. **`extern "C"`** on the entry point — avoids C++ name mangling.
2. **`-ffreestanding -fno-exceptions -fno-rtti`** — you can't use the parts of C++ that need a runtime.
3. Everything else ([Multiboot](../GLOSSARY/multiboot.md "The protocol that lets a bootloader load any kernel; magic 0x1BADB002"), `0xB8000`, 1 MiB link origin) is the same as C.
