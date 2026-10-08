# Makefile for the C kernel of Example_OS_Project
#
# Builds kernel.bin (a Multiboot bootable ELF) and, optionally, a bootable ISO.
#
# Targets:
#   make          - build kernel.bin only
#   make run      - build + boot kernel.bin in QEMU
#   make iso      - build a bootable CD ISO (needs grub-mkrescue + xorriso)
#   make clean    - remove build artifacts
#
# NOTE on the cross-compiler: the OSDev community recommends building an
# i686-elf cross-compiler. For learning on a normal machine you can build
# with your system gcc using -m32 (as below) and boot the 32-bit ELF
# directly with QEMU -kernel. For real bare-metal or GRUB-on-disk you
# should use i686-elf-gcc. See docs/setup.md.

AS      ?= as              # GNU assembler (or: nasm -f elf32)
CC      ?= gcc
LD      ?= ld

# Freestanding: no libc, no host assumptions. -m32 targets 32-bit x86
# (Multiboot v1 runs in 32-bit protected mode).
CFLAGS   = -ffreestanding -fno-pie -m32 -nostdlib -O2 -Wall -Wextra
ASFLAGS  = --32
LDFLAGS  = -m elf_i386 -T linker.ld -nostdlib

BIN      = kernel.bin

.PHONY: all run iso clean

all: $(BIN)

# Assemble the Multiboot bootstrap.
boot.o: boot.s
	$(AS) $(ASFLAGS) boot.s -o $@

# Compile the kernel freestanding.
kernel.o: kernel.c
	$(CC) -c kernel.c -o $@ $(CFLAGS)

# Link everything into one kernel image at 1 MiB.
$(BIN): boot.o kernel.o linker.ld
	$(LD) $(LDFLAGS) -o $@ boot.o kernel.o

run: $(BIN)
	@echo "Booting $(BIN) in QEMU..."
	qemu-system-i386 -kernel $(BIN)

# Headless run: kernel prints "Hello World!" to the terminal via COM1 serial.
# Works inside code-server (no GUI display needed).
run-headless: $(BIN)
	@echo "Booting $(BIN) headless - kernel output goes to this terminal (serial)..."
	qemu-system-i386 -kernel $(BIN) -nographic -monitor none

# Same, but capture serial to a file instead of the terminal.
run-serial: $(BIN)
	@echo "Capturing kernel serial output to kernel_serial.txt (3s boot)..."
	timeout 3 qemu-system-i386 -kernel $(BIN) -display none -serial file:kernel_serial.txt -monitor none || true
	@echo "--- kernel_serial.txt ---"
	@cat kernel_serial.txt

# Optional: build a bootable ISO (requires grub-mkrescue, xorriso, mtools).
iso: $(BIN)
	@echo "Building bootable ISO (needs grub-mkrescue + xorriso)..."
	mkdir -p iso/boot/grub
	cp $(BIN) iso/boot/kernel.bin
	printf 'set timeout=0\nmenuentry "Example OS (C)" {\n  multiboot /boot/kernel.bin\n  boot\n}\n' > iso/boot/grub/grub.cfg
	grub-mkrescue -o Example_OS_C.iso iso

clean:
	rm -f *.o $(BIN) *.iso
	rm -rf iso
