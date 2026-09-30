#!/usr/bin/env bash
# build-all.sh — build every kernel that this machine can build.
# Skips Go (needs gccgo cross) and C# (needs Cosmos) with a friendly note.
set -e
cd "$(dirname "$0")/.."

echo "== Building C kernel ==" && make -C c
echo "== Building C++ kernel ==" && make -C cpp

# Rust: only if cargo is available (it lives on the Windows host in this
# setup, not in WSL). Skip gracefully otherwise.
if command -v cargo >/dev/null 2>&1; then
  echo "== Building Rust kernel ==" && make -C rust
else
  echo "== Rust kernel =="
  echo "  [skip] cargo not on PATH here (build with the Windows-host Rust,"
  echo "         or add cargo to PATH)"
fi

echo
echo "Done. To boot a kernel, run:  make run-c   |   make run-cpp   |   make run-rust"
echo "Go (make run-go) needs i686-elf-gccgo; C# needs Cosmos + VS2022 (see their READMEs)."
