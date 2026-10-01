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

## More Beginner Tutorials
- **Golangbot: Learn Go Series** — https://golangbot.com/learn-golang-series/ — a well-structured, chapter-by-chapter Go tutorial covering syntax, structs, interfaces, concurrency and more.
- **W3Schools: Go Tutorial** — https://www.w3schools.com/go/ — a quick, example-first Go introduction with an online compiler.
- **freeCodeCamp: Learn the Go Programming Language (Handbook)** — https://www.freecodecamp.org/news/learn-golang-handbook/ — a free written handbook covering Go from zero, including concurrency.
- **The Little Go Book (Karl Seguin)** — https://github.com/karlseguin/the-little-go-book — a free, concise (~50 page) introduction to Go that's great as a fast second read.

## Go Reference, Internals & Low-Level
- **The Go Programming Language Specification** — https://go.dev/ref/spec — the authoritative grammar and semantics of Go — read the parts of the spec that define slice/string/map behavior when you go low-level.
- **Go Memory Model** — https://go.dev/ref/mem — the official document on ordering guarantees for reads, writes and atomic/sync operations — essential before writing concurrent systems code.
- **Go Slices: usage and internals** — https://go.dev/blog/slices-intro — the canonical blog post explaining how slices actually work in memory.
- **Go Assembly (Plan 9 asm)** — https://go.dev/doc/asm — the official guide to Go's Plan 9 assembly dialect — what you'll touch for the very lowest-level Go runtime/hardware work.
- **A Few Words on Interfaces (Griesemer)** — https://research.swtch.com/interfaces — a clear internals essay on how Go interfaces are represented at runtime.
- **Go Concurrency Patterns (Rob Pike)** — https://go.dev/talks/2012/concurrency.slide — the classic slide deck introducing goroutines, channels and pipelines as compositional tools.
- **Concurrency Is Not Parallelism (Rob Pike)** — https://go.dev/talks/2012/waza.slide — the well-known talk clarifying concurrency vs. parallelism — a must before designing a concurrent kernel.
- **Go Proverbs (Rob Pike)** — https://go-proverbs.github.io/ — the short set of aphorisms capturing Go's design philosophy, each with explanatory links.
- **Go Cheat Sheet (a8m)** — https://github.com/a8m/go-lang-cheat-sheet — a dense reference of Go syntax, semantics and gotchas.
- **syscall package** — https://pkg.go.dev/syscall — the low-level OS interface in the standard library — how Go reaches system calls, relevant when you map Go's syscall handling onto your own kernel.

## Go Tools & Ecosystem
- **The Go Playground** — https://go.dev/play/ — run and share Go snippets in the browser while you learn.
- **awesome-go** — https://github.com/avelino/awesome-go — the community's curated list of Go libraries and tools across every domain.
- **cgo (Go Wiki)** — https://go.dev/wiki/cgo — how Go interacts with C — key to mixing hand-written/C boot code with a Go kernel.

## Go Embedded & Unikernels
- **TinyGo** — https://tinygo.org/ — a Go compiler targeting microcontrollers and WebAssembly with a reduced runtime — the practical route to running Go on bare-metal/embedded hardware.
- **TinyGo docs** — https://tinygo.org/docs/ — official TinyGo documentation covering boards, targets and AVR/ARM/RISC-V support.
- **gVisor (Google)** — https://github.com/google/gvisor — a user-space kernel and sandbox written entirely in Go, implementing the Linux syscall ABI — an outstanding large-scale example of "an OS in Go".
- **go-boot (usbarmory)** — https://github.com/usbarmory/go-boot — a bare-metal Go UEFI boot manager and unikernel — a working demonstration of Go driving UEFI/OS loading directly.

## More Go Beginner & Practice
- **Go 101 (free ebook)** — https://go101.org/ — a deep, unusually thorough free book on Go, famous for explaining subtle semantics (slices, strings, channels, memory model) better than most sources.
- **Gophercises** — https://gophercises.com/ — a free set of ~20 small coding exercises from Jon Calhoun that build Go fluency by writing real mini-projects.
- **Exercism: Go track** — https://exercism.org/tracks/go — mentor-reviewed Go exercises spanning syntax, concurrency and testing.
- **Practical Go Lessons** — https://www.practical-go-lessons.com/ — a free, thorough Go course (in the spirit of "Practical C Programming") that moves methodically from syntax to systems topics.
- **Learn Go the Hard Way (Zed Shaw, free to read)** — https://learncodethehardway.com/courses/learn-go-the-hard-way — a beginner-friendly Go course that builds real command-line tools, from basics up to implementing coreutils.
- **ardanlabs/gotraining** — https://github.com/ardanlabs/gotraining — the training material behind Ardan Labs' acclaimed Go courses — covers internals, concurrency and idiomatic design in detail.
- **justforfunc (YouTube)** — https://www.youtube.com/@justforfunc — a popular Go programming video series with in-depth, live-coding episodes on internals and design.

## Go Official Getting-Started & Runtime
- **Go: Getting Started (official tutorials)** — https://go.dev/doc/tutorial/ — the official step-by-step getting-started tutorials (modules, packages, testing) — the canonical next step after A Tour of Go.
- **pkg.go.dev: runtime** — https://pkg.go.dev/runtime — documentation for the Go runtime package (scheduler, goroutines, GC hooks) — the part of Go you're effectively re-owning when you write Go without an OS.

## Go Unikernels & Bare-Metal
- **gokrazy** — https://gokrazy.org/ — a system that runs a pure-Go "appliance" on a Raspberry Pi with no general-purpose OS — the easiest way to get bare-metal-ish Go running on real hardware.
- **TamaGo** — https://github.com/inversepath/tamago — the bare-metal Go framework that powers go-boot and USB Armory unikernels — lets you run Go directly on ARM/AMD64 with no OS underneath.
