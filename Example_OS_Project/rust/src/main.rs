#![no_std]          // do NOT link the standard library
#![no_main]         // do NOT use the normal Rust main() runtime

// main.rs — A minimal "Hello World!" OS kernel in Rust (no_std).
//
// The Rust reference implementation, following the approach of the
// "Writing an OS in Rust" series (os.phil-opp.com):
//   - #![no_std]      : our kernel uses zero OS/library-provided features.
//   - #![no_main]     : we define our own entry point (_start).
//   - panic handler   : bare metal has no panic runtime, so we provide one.
//   - _start          : the CPU/bootloader jumps here to start the kernel.
//
// Build (kernel only — compiles to a freestanding ELF):
//   rustup target add x86_64-unknown-none
//   cargo build --target x86_64-unknown-none
//
// To actually BOOT it you bundle this ELF with the `bootloader` crate
// (which needs a nightly toolchain) into a disk image — see Makefile.

use core::panic::PanicInfo;

// ---- VGA text-mode driver -------------------------------------------
// Simple 80x25 text buffer at 0xB8000. Each cell is 2 bytes: [char][color].
const VGA_WIDTH: usize = 80;
const VGA_HEIGHT: usize = 25;
const VGA_BUFFER: *mut u16 = 0xB8000 as *mut u16;   // the framebuffer
const COLOR_WHITE_ON_BLACK: u16 = 0x0F;              // fg=white, bg=black

// Simple "terminal" cursor (row/column) — the minimal bookkeeping the
// Phil Opp series grows into a full Writer type in later chapters.
static mut CURSOR_ROW: usize = 0;
static mut CURSOR_COL: usize = 0;

/// Write a single character to the VGA buffer at the current cursor.
fn vga_putchar(c: u8) {
    if c == b'\n' {
        // newline: go to start of the next row, wrap at the bottom
        unsafe {
            CURSOR_COL = 0;
            CURSOR_ROW += 1;
            if CURSOR_ROW >= VGA_HEIGHT {
                CURSOR_ROW = 0;
            }
        }
        return;
    }

    let row = unsafe { CURSOR_ROW };
    let col = unsafe { CURSOR_COL };
    let index = row * VGA_WIDTH + col;
    // Safety: 0xB8000 is the valid, always-mapped VGA text framebuffer.
    unsafe {
        *VGA_BUFFER.add(index) = (COLOR_WHITE_ON_BLACK << 8) | c as u16;
    }

    // advance the cursor, wrapping at the end of the row
    unsafe {
        CURSOR_COL += 1;
        if CURSOR_COL >= VGA_WIDTH {
            CURSOR_COL = 0;
            CURSOR_ROW += 1;
            if CURSOR_ROW >= VGA_HEIGHT {
                CURSOR_ROW = 0;
            }
        }
    }
}

/// Write a string to the VGA buffer. Kernel text is ASCII for now.
fn vga_write(s: &str) {
    for byte in s.bytes() {
        vga_putchar(byte);
    }
}

/// The kernel entry point, called by the CPU payload / bootloader.
/// It gets a proper stack from the bootloader — we just print and loop
/// forever (a kernel never returns).
#[no_mangle]
pub extern "C" fn _start() -> ! {
    vga_write("Hello World!\n");
    vga_write("Welcome to your very own operating system (Rust edition).\n");
    loop {
        // A kernel never returns. `hlt` parks the CPU to save power;
        // interrupts (added in later chapters) wake it up again.
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}

/// Panic handler — what runs if our kernel ever panics. There is no OS to
/// unwind through, so the minimal implementation just halts forever.
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {
        unsafe { core::arch::asm!("hlt", options(nomem, nostack)) }
    }
}
