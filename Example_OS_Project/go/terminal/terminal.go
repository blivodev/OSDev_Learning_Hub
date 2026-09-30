// terminal.go — A minimal VGA text-mode terminal driver for the Go kernel.
//
// Same idea as the C/C++/Rust drivers: the VGA text framebuffer lives at
// 0xB8000, an 80x25 grid where each cell is 2 bytes: [char][color].
//
// This is the "package terminal" that kernel.go imports.

package terminal

// VGA text-mode geometry and addresses.
const (
	width  = 80 // columns
	height = 25 // rows
	// The framebuffer is at physical address 0xB8000.
	// In Go we treat it as a raw memory address (see write method).
	bufferAddr = uintptr(0xB8000)
)

// Color constants (low nibble = foreground, high nibble = background).
const (
	colorWhiteOnBlack = 0x0F // white text on black background
)

var (
	row int
	col int
)

// Init clears the screen and moves the cursor to (0,0).
func Init() {
	clear()
	row = 0
	col = 0
}

// writeCell writes one (char,color) cell at (r,c).
// Go has no direct pointer-arithmetic-to-memory in safe mode, so on a
// real freestanding gccgo target you'd use the `unsafe` package to poke
// byte 0xB8000 + 2*(r*width+c). This comment marks exactly where.
func writeCell(r, c int, char byte, color byte) {
	// Example (unsafe) implementation:
	//   offset := uintptr(r*width + c) * 2
	//   *(*byte)(unsafe.Pointer(bufferAddr + offset))     = char
	//   *(*byte)(unsafe.Pointer(bufferAddr + offset + 1)) = color
	_ = r
	_ = c
	_ = char
	_ = color
}

// clear fills the whole screen with blank spaces.
func clear() {
	for r := 0; r < height; r++ {
		for c := 0; c < width; c++ {
			writeCell(r, c, ' ', colorWhiteOnBlack)
		}
	}
}

// putChar writes a single character at the cursor, handling newline/wrap.
func putChar(ch byte) {
	if ch == '\n' {
		row++
		col = 0
		if row >= height {
			row = 0
		}
		return
	}
	writeCell(row, col, ch, colorWhiteOnBlack)
	col++
	if col >= width {
		col = 0
		row++
		if row >= height {
			row = 0
		}
	}
}

// WriteString prints a string to the screen.
func WriteString(s string) {
	for i := 0; i < len(s); i++ {
		putChar(s[i])
	}
}
