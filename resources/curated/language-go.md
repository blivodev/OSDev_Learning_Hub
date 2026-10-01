# Go — Curated Learning & OS-Dev Resources

Go is an unusual but growing systems language: with its AOT-compiled runtime, goroutines and GC it can technically do bare-metal work, and projects like eggos, go-dav-os and the OSDev Go Bare Bones tutorial prove a whole OS can be started in Go. These resources cover learning Go, Go systems programming, and Go OS-dev/hardware work. All links verified reachable.

## Go Language Tutorials (beginner onward)
- **A Tour of Go** — https://go.dev/tour — the official interactive introduction; start here.
- **Effective Go** — https://go.dev/doc/effective_go — the official idioms-and-style guide — essential once you know the syntax.
- **Go by Example** — https://gobyexample.com/ — bite-sized annotated examples of every major Go feature.
- **Learn Go with Tests** — https://quii.gitbook.io/learn-go-with-tests — a free, test-driven book that teaches Go through writing tests — great structured path.
- **The Go Programming Language docs** — https://go.dev/doc/ — official documentation hub (getting started, FAQ, articles). Install page: https://go.dev/doc/install.

## Go Reference & Advanced
- **The Go standard documentation / pkg.go.dev** — https://pkg.go.dev/ — the official package documentation for the standard library and all modules.
- **The Go Blog** — https://go.dev/blog/ — official deep-dive articles on internals: GC, scheduler, interfaces, `strings`, etc. Same content on https://blog.golang.org/.
- **Go Wiki: Learn** — https://go.dev/wiki/Learn — the community-curated list of the best Go learning resources.
- **golang/go (source)** — https://github.com/golang/go — read the actual compiler/runtime source to understand how Go behaves at the lowest level.

## Go Systems Programming
- **iximiuz Labs: Using Go for Systems Programming** — https://labs.iximiuz.com/tutorials/go-as-systems-programming-language-a667d22b — a practical intro to writing system-level code (processes, syscalls, Linux) in Go.
- **Packt: Go Systems Programming (repo)** — https://github.com/packtpublishing/go-systems-programming — the companion code for the book on Linux/Unix system-level programming with Go (processes, files, networking).
- **Packt: Hands-On System Programming with Go (repo)** — https://github.com/PacktPublishing/Hands-On-System-Programming-with-Go — companion code teaching syscalls, concurrency and OS interaction in Go.
- **Go Wiki: Books** — https://go.dev/wiki/Books — curated list of Go books, several of which cover systems/advanced topics.

## Go OS-Dev & Unikernels
- **OSDev Wiki: Go Bare Bones** — https://wiki.osdev.org/Go_Bare_Bones — the canonical tutorial for booting a Go kernel (multiboot + a `noos` freestanding harness); start here for OS-dev in Go.
- **eggos (icexin)** — https://github.com/icexin/eggos — a Go unikernel running directly on x86 bare metal; demonstrates threading, networking and Go runtime without an OS. (Original at https://github.com/alexflint/eggos.)
- **go-dav-os** — https://github.com/dmarro89/go-dav-os — a practical demonstration of writing an OS/boot flow in Go (a variant of the OSDev Go bare bones).
- **project-layout** — https://github.com/golang-standards/project-layout — standard Go project structure conventions, useful for organizing a Go systems/hardware project.

## Talks & Community
- **GopherCon: An Operating System in Go** — https://www.youtube.com/watch?v=SvsdVe1kgSU — a talk walking through building an OS in Go (linked from the hub's video section too).
- **Go Wiki** — https://go.dev/wiki/ — community index of Go projects and resources relevant to systems work.
