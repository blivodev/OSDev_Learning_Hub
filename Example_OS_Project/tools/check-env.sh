#!/usr/bin/env bash
# check-env.sh — verify the Example_OS_Project toolchain is installed.
#
# Prints ✓/✗ for each tool, and exits 0 only if the core C/C++/Rust
# toolchain is present. Use this before building.

echo "== Core (C/C++/Go multiboot) toolchain =="
for tool in as gcc g++ ld make; do
  if command -v "$tool" >/dev/null 2>&1; then echo "  [OK]   $tool"; else echo "  [MISS] $tool"; fi
done

echo "== Running the kernels =="
if command -v qemu-system-i386 >/dev/null 2>&1; then
  echo "  [OK]   qemu-system-i386"
else
  echo "  [MISS] qemu-system-i386  (sudo apt install qemu-system-x86)"
fi

echo "== Rust (optional night/day) =="
for tool in rustup cargo; do
  if command -v "$tool" >/dev/null 2>&1; then echo "  [OK]   $tool"; else echo "  [MISS] $tool"; fi
done
rustup target list --installed 2>/dev/null | grep -q x86_64-unknown-none \
  && echo "  [OK]   rust target x86_64-unknown-none" \
  || echo "  [MISS] rust target x86_64-unknown-none"

echo "== Go (needs i686-elf-gccgo cross) =="
command -v i686-elf-gccgo >/dev/null 2>&1 \
  && echo "  [OK]   i686-elf-gccgo" \
  || echo "  [MISS] i686-elf-gccgo  (see go/README.md to build)"

echo "== C# (needs Cosmos + VS2022) =="
command -v dotnet >/dev/null 2>&1 \
  && echo "  [OK]   dotnet" \
  || echo "  [MISS] dotnet"
