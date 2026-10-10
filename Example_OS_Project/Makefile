# Example_OS_Project — top-level build & run
#
# Wraps the per-language builds and boots kernels in QEMU.
#
# Targets:
#   make            - build everything buildable on this host
#   make run-c      - build + boot the C    kernel in QEMU
#   make run-cpp    - build + boot the C++  kernel in QEMU
#   make run-rust   - build + boot the Rust kernel in QEMU
#   make run-go     - build + boot the Go   kernel in QEMU (needs gccgo cross)
#   make iso-c      - build a bootable ISO of the C kernel (needs grub-mkrescue)
#   make clean      - remove all build artifacts
#
# Notes:
#   - C/C++/Go boot a 32-bit Multiboot ELF, so they use qemu-system-i386 -kernel.
#   - Rust uses the bootloader crate / bootimage, so it boots as a disk image
#     with qemu-system-x86_64 -drive.

.PHONY: all run-c run-cpp run-rust run-go debug-c debug-c-gui iso-c clean

all:
	$(MAKE) -C c
	$(MAKE) -C cpp
	$(MAKE) -C rust
	@echo "Go kernel requires a gccgo cross-compiler — see go/README.md"
	@echo "C# kernel requires Cosmos + VS2022 — see csharp/README.md"

run-c:
	$(MAKE) -C c run

run-c-headless:
	$(MAKE) -C c run-headless

run-cpp:
	$(MAKE) -C cpp run

run-rust:
	$(MAKE) -C rust run

run-go:
	$(MAKE) -C go run

iso-c:
	$(MAKE) -C c iso

# Debug the C kernel with QEMU's gdb stub (see c/Makefile for the workflow).
debug-c:
	$(MAKE) -C c debug

debug-c-gui:
	$(MAKE) -C c debug-gui

debug-c-script:
	$(MAKE) -C c debug-script

clean:
	$(MAKE) -C c clean
	$(MAKE) -C cpp clean
	$(MAKE) -C rust clean
	rm -rf build
