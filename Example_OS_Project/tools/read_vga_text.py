#!/usr/bin/env python3
"""read_vga_text.py — read & decode the VGA text buffer from a running QEMU.

Usage: python3 read_vga_text.py <qemu-monitor-socket> [cells]
Reads `xp` output from QEMU's monitor at 0xB8000 and decodes the 80x25
VGA text cells into readable characters (proving the kernel printed text).

Requires: qemu-system-i386 running with -monitor unix:<sock>,server,nowait
"""
import socket, time, re, sys

sock_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/qemu-mon.sock"
cells     = int(sys.argv[2]) if len(sys.argv) > 2 else 80

# QEMU monitor `xp` prints in host words (4 bytes = 2 VGA cells).
# We ask for cells/2 words and decode.
s = socket.socket(socket.AF_UNIX); s.connect(sock_path)
time.sleep(0.3)
word_request = cells // 2
s.sendall(b"xp /%dhw 0xb8000\n" % word_request)
time.sleep(0.6)
buf = b""
s.settimeout(1.0)
try:
    while True:
        d = s.recv(65536)
        if not d: break
        buf += d
except socket.timeout:
    pass
s.close()

# Grab everything after the address, all hex tokens, decode little-endian.
# Each token is a 32-bit LE word like 0x0f650f48. VGA cells are 16-bit:
#   cell = [char_low][color_high]  (char byte at the LOWER address).
# In the LE word [48,0f,65,0f] (addr 0,1,2,3), the chars live at even
# addresses -> bytes 0x48 and 0x65, which in fromhex display are b[3] and b[1].
tokens = re.findall(rb"0x[0-9a-f]{8}", buf)
chars = []
for tok in tokens:
    b = bytes.fromhex(tok[2:].decode())   # 4 bytes: [0f,65,0f,48] -> chars 0x48,0x65
    c0, c1 = b[3], b[1]                    # low byte of each little-endian u16 cell
    chars.append(chr(c0) if 32 <= c0 < 127 else ".")
    chars.append(chr(c1) if 32 <= c1 < 127 else ".")

# Print as an 80-wide row grid.
line = "".join(chars)
for r in range(0, len(line), 80):
    print("row%2d: %s" % (r // 80, line[r:r+80]))
