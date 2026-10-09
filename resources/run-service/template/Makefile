# Makefile — sandbox build for a single C kernel (kernel.c -> kernel.bin)
# Runs inside the runner container. No host assumptions, freestanding -m32.
AS      ?= as
CC      ?= gcc
LD      ?= ld

CFLAGS   = -ffreestanding -fno-pie -m32 -nostdlib -O2 -Wall -Wextra
ASFLAGS  = --32
LDFLAGS  = -m elf_i386 -T linker.ld -nostdlib

BIN      = kernel.bin

.PHONY: all clean
all: $(BIN)

boot.o: boot.s
	$(AS) $(ASFLAGS) boot.s -o $@

kernel.o: kernel.c
	$(CC) -c kernel.c -o $@ $(CFLAGS)

$(BIN): boot.o kernel.o linker.ld
	$(LD) $(LDFLAGS) -o $@ boot.o kernel.o

clean:
	rm -f *.o $(BIN)
