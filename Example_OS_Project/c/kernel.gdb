# kernel.gdb — OSDev debugging helper for QEMU + gdb (Example_OS_Project)
#
# Usage:
#   make debug                     (terminal 1: boots QEMU paused on :1234)
#   gdb -x kernel.gdb kernel.dbg   (terminal 2: attach + useful setup)
#
# After attach:  continue  to run to kernel_main (breakpoint preset below).
# Control:       Ctrl-C in gdb interrupts the guest;  quit detaches.

set pagination off
set confirm off

# Connect to QEMU's built-in gdb stub.
target remote localhost:1234

# Preset breakpoints — the interesting entry points.
break kernel_main
break vga_write
break serial_write

# Load the Multiboot header info for orientation.
info files

# Print registers at attach so you can see the CPU start state.
info registers eip eax ebx

echo \n=== attached to QEMU. Type "continue" to run to kernel_main. ===\n

# Convenience: single-keystroke OSDev helpers
define hb
  break *0x8000
end
document hb
  Hardware breakpoint at 0x8000 (conventional low-memory area).
end

define bootregs
  printf "Multiboot magic: %#x  (0x2BADB002 = OK)\n", $eax
  printf "MB info ptr:     %#x\n", $ebx
  info registers eip esp ebp
end
document bootregs
  Show Multiboot boot state — magic in eax, info struct ptr in ebx.
end
