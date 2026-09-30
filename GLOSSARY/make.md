<!-- Glossary page — Make. Grounded in OSDev_Learning_Hub docs. -->

# Make

> **[Back to glossary index](README.md)** · Category: Toolchain & build

Make is a build automation tool that reads a `Makefile` and runs the right compile/link commands whenever files change.

## The short version
Kernel builds involve several steps — assemble, compile freestanding, link with a linker script, boot in QEMU — and you don't want to type them every time. A `Makefile` encodes those steps as named *targets* (`all`, `run`, `iso`, `clean`) with their dependencies, so `make run` builds the kernel *and* boots it in QEMU in one command. This hub has a Makefile per language plus a top-level orchestrator.

## Detailed explanation
Make captures the core loop from `02-your-toolchain.md` as reproducible rules. In `Example_OS_Project/c/Makefile` (C++ is identical), the rules chain together:

```make
CFLAGS   = -ffreestanding -fno-pie -m32 -nostdlib -O2 -Wall -Wextra
ASFLAGS  = --32
LDFLAGS  = -m elf_i386 -T linker.ld -nostdlib

boot.o: boot.s
	$(AS) $(ASFLAGS) boot.s -o $@
kernel.o: kernel.c
	$(CC) -c kernel.c -o $@ $(CFLAGS)
$(BIN): boot.o kernel.o linker.ld
	$(LD) $(LDFLAGS) -o $@ boot.o kernel.o
run: $(BIN)
	@echo "Booting $(BIN) in QEMU..."
	qemu-system-i386 -kernel $(BIN)
iso: $(BIN)
	... # grub-mkrescue + xorriso → Example_OS_C.iso
clean:
	rm -f *.o $(BIN) *.iso
```

Because `kernel.bin` *depends on* `boot.o`, `kernel.o`, and `linker.ld`, `make` rebuilds only what changed and re-runs the link whenever any input changes — so editing `kernel.c` automatically recompiles and relinks on the next `make run`.

The top-level `Example_OS_Project/Makefile` wraps all the language builds with targets like `make run-c`, `make run-cpp`, `make run-rust`, `make run-go`, and `make iso-c`, plus a `make clean` that removes every build artifact.

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/Makefile` — top-level orchestrator with `run-*` and `iso-c` targets.
- `Example_OS_Project/c/Makefile` and `cpp/Makefile` — the C/C++ build & boot rules.
- `Example_OS_Project/rust/Makefile` — wraps `cargo build --target x86_64-unknown-none` and `cargo bootimage`.
- `Example_OS_Project/Cargo.toml` and the Rust `Makefile` more closely mirror `cargo`'s role as the build driver for Rust.

## Watch / listen
- [GNU Make manual — Official docs](https://www.gnu.org/software/make/manual/make.html) — free, authoritative
- [Wikipedia — Make (software)](https://en.wikipedia.org/wiki/Make_(software)) — free overview

## Related terms
- [Cross-Compiler](cross-compiler.md)
- [Linker](linker.md)
- [QEMU](qemu.md)
- [cargo](cargo.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
