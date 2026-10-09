#!/bin/bash
# run_kernel.sh — runs INSIDE the sandbox container (as user 'runner').
# Receives the mounted /work dir containing kernel.c (+ boot.s, linker.ld, Makefile
# from the template), compiles it, boots it headless, and prints the serial output.
#
# Usage (inside container):  bash run_kernel.sh
# The API mounts a fresh temp dir at /work per request.
set -u
cd /work || exit 2

echo "=== COMPILE ==="
# Build only the C kernel (kernel.bin is a 32-bit Multiboot ELF).
make -s 2>&1
rc=$?
if [ $rc -ne 0 ]; then
    echo ""
    echo "=== COMPILE FAILED (exit $rc) ==="
    exit 10
fi

if [ ! -f kernel.bin ]; then
    echo "=== NO kernel.bin PRODUCED ==="
    exit 11
fi

echo ""
echo "=== BOOT (QEMU, headless) ==="
# Boot headless; the kernel prints to COM1 serial -> captured here.
# -no-reboot + timeout so a hanging kernel can't run forever.
timeout 4 qemu-system-i386 -kernel kernel.bin -nographic -monitor none -no-reboot 2>&1
brc=$?
echo ""
if [ $brc -eq 124 ]; then
    echo "=== BOOT TIMEOUT (kernel ran 4s; likely halted as expected) ==="
fi
echo "=== DONE ==="
exit 0
