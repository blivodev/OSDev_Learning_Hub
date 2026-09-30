# Makefile for the Rust kernel of Example_OS_Project
#
# The KERNEL builds with the stable built-in bare-metal target
# x86_64-unknown-none (no nightly needed). Producing a BOOTABLE disk image
# additionally needs the `bootloader` crate + a nightly toolchain — see
# the `bootimage` target below.
#
# Targets:
#   make          - build the freestanding kernel (no bootable image)
#   make run      - build + boot in QEMU (needs nightly + bootimage)
#   make clean    - remove build artifacts

CARGO   ?= cargo
QEMU    ?= qemu-system-x86_64

TARGET   = x86_64-unknown-none

.PHONY: all run clean

# Build the freestanding kernel ELF (verified on stable).
all:
	$(CARGO) build --target $(TARGET)

# Build a bootable disk image and boot it in QEMU.
# NOTE: needs nightly + `cargo install bootimage` (see docs/setup.md). The
# bootloader crate bundles this kernel into a BIOS-bootable image that QEMU
# boots as a raw disk.
run:
	$(CARGO) bootimage --target $(TARGET)
	$(QEMU) -drive format=raw,file=target/$(TARGET)/debug/bootimage-example_os_rust.bin

clean:
	$(CARGO) clean
