# Makefile for the C++ kernel of Example_OS_Project
#
# Same layout as the C kernel, using g++ and the C++-specific flags:
#   -fno-exceptions -fno-rtti  (no runtime support for these on bare metal)
#
# Targets: make | make run | make iso | make clean
#
# See the C Makefile header for notes about the cross-compiler.

AS      ?= as
CXX     ?= g++
LD      ?= ld

# Freestanding C++: no libc/libstdc++, no exceptions, no RTTI, 32-bit.
CXXFLAGS = -ffreestanding -fno-pie -m32 -nostdlib \
           -fno-exceptions -fno-rtti -O2 -Wall -Wextra
ASFLAGS  = --32
LDFLAGS  = -m elf_i386 -T linker.ld -nostdlib

BIN      = kernel.bin

.PHONY: all run iso clean

all: $(BIN)

boot.o: boot.s
	$(AS) $(ASFLAGS) boot.s -o $@

kernel.o: kernel.c++
	$(CXX) -c kernel.c++ -o $@ $(CXXFLAGS)

$(BIN): boot.o kernel.o linker.ld
	$(LD) $(LDFLAGS) -o $@ boot.o kernel.o

run: $(BIN)
	@echo "Booting $(BIN) in QEMU..."
	qemu-system-i386 -kernel $(BIN)

iso: $(BIN)
	@echo "Building bootable ISO (needs grub-mkrescue + xorriso)..."
	mkdir -p iso/boot/grub
	cp $(BIN) iso/boot/kernel.bin
	printf 'set timeout=0\nmenuentry "Example OS (C++)" {\n  multiboot /boot/kernel.bin\n  boot\n}\n' > iso/boot/grub/grub.cfg
	grub-mkrescue -o Example_OS_CPP.iso iso

clean:
	rm -f *.o $(BIN) *.iso
	rm -rf iso
