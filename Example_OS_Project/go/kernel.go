// kernel.go — A minimal "Hello World!" OS kernel in Go.
//
// This follows the OSDev Wiki "Go Bare Bones" tutorial:
//   - Go's runtime is a problem on bare metal, so we implement just the
//     stub symbols the toolchain expects (in boot.s) and write the kernel
//     logic in Go.
//   - terminal.go provides the VGA text-mode painting.
//   - main() is called by boot.s.
//
// Compile (requires a Go-enabled cross-compiler, e.g. i686-elf-gccgo):
//   i686-elf-gccgo -static -Werror -nostdlib -nostartfiles \
//       -nodefaultlibs -c kernel.go -o kernel.go.o
//   (then link with terminal.go.o, boot.o and linker.ld)

package kernel

import "example_os_go/terminal"

// main is the Go kernel entry point, called from boot.s.
// It paints "Hello World!" to the VGA text buffer and then idles.
func Main() {
	terminal.Init() // clear the screen

	terminal.WriteString("Hello World!\n")
	terminal.WriteString("Welcome to your very own operating system (Go edition).\n")

	// A Go kernel has no OS to return to. Spin forever.
	// (A real kernel would use the hlt instruction to idle; on bare
	// metal Go we keep a simple busy loop for this first version.)
	for {
		// idle
	}
}
