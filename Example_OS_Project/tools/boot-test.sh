#!/usr/bin/env bash
# boot-test.sh — build & boot a kernel, then read the VGA text buffer back
# to PROVE it printed "Hello World!". No admin install needed: everything
# (make, gcc, qemu, python) runs inside a disposable Ubuntu container.
#
# Usage:  tools/boot-test.sh c | cpp
# Example:
#   tools/boot-test.sh c    # build + boot the C kernel, print the screen text
#
# The single QEMU monitor -> VGA readback is the honest proof the kernel
# actually booted and wrote text (not just "it compiled").
set -e
cd "$(dirname "$0")/.."
LANG_DIR="$1"
[ -z "$LANG_DIR" ] && { echo "usage: $0 c|cpp"; exit 1; }

HOST="$(pwd)"
echo "== Building & booting the $LANG_DIR kernel in a QEMU container =="
docker run --rm -v "$HOST:/hub" -w "/hub/$LANG_DIR" ubuntu:24.04 bash -c "
  set -e
  apt-get update -qq >/dev/null 2>&1
  apt-get install -y -qq make gcc g++ binutils qemu-system-x86 python3 >/dev/null 2>&1
  echo '--- build ---'
  make >/dev/null
  echo '--- boot + read VGA text back ---'
  qemu-system-i386 -kernel kernel.bin -display none -vga std \
    -monitor unix:/tmp/qemu-mon.sock,server,nowait &
  QPID=\$!
  sleep 3
  python3 /hub/tools/read_vga_text.py /tmp/qemu-mon.sock 240
  kill \$QPID 2>/dev/null || true
"
