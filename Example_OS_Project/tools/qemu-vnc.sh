#!/bin/bash
# qemu-vnc.sh — boot a kernel in QEMU with VNC display, served to the
# browser via noVNC (websockify). See the real VGA screen in a browser tab.
#
# Usage:
#   ./qemu-vnc.sh [kernel.bin] [vnc_display] [novnc_port]
#   ./qemu-vnc.sh /workspace/Example_OS_Project/c/kernel.bin 1 6080
#
# Defaults:
#   KERNEL  = Example_OS_Project/c/kernel.bin
#   VNC     = display :1  (port 5901)
#   NOVNC   = port 6080
#
# After launching, open http://localhost:6080/vnc.html (or the proxied
# vnc.sektor9.dev) and click Connect — the kernel's VGA screen appears.
set -e

KERNEL="${1:-/workspace/Example_OS_Project/c/kernel.bin}"
VNC_DISP="${2:-1}"
NOVNC_PORT="${3:-6080}"
VNC_PORT=$((5900 + VNC_DISP))

# Kill any stale instances
pkill -f "qemu-system-i386 -kernel $KERNEL" 2>/dev/null || true
pkill -f "websockify $NOVNC_PORT" 2>/dev/null || true
sleep 1

echo "== Starting QEMU (VNC display :$VNC_DISP) =="
qemu-system-i386 -kernel "$KERNEL" -vnc "127.0.0.1:$VNC_DISP" -monitor none \
    >/tmp/qemu-vnc.log 2>&1 &
QPID=$!
sleep 2

echo "== Starting websockify (port $NOVNC_PORT -> VNC $VNC_PORT) =="
websockify --web /usr/share/novnc "$NOVNC_PORT" "127.0.0.1:$VNC_PORT" \
    >/tmp/websockify.log 2>&1 &
WPID=$!
sleep 2

echo "QEMU pid=$QPID  websockify pid=$WPID"
echo "Kernel: $KERNEL"
echo "VNC display: :$VNC_DISP (port $VNC_PORT)"
echo "noVNC: http://localhost:$NOVNC_PORT/vnc.html"
echo "Logs: /tmp/qemu-vnc.log  /tmp/websockify.log"
echo "Stop: pkill -f qemu-system-i386; pkill -f websockify"
