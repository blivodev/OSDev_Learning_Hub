<!-- Glossary page — Text Mode Cursor. Grounded in OSDev_Learning_Hub docs. -->

# Text Mode Cursor

> **[Back to glossary index](README.md)** · Category: Hardware

The text-mode cursor is the blinking position indicator in the VGA text buffer that marks where the next character will be written.

## The short version
When a kernel writes text to the VGA buffer at `0xB8000`, it needs to track *where* the next character goes. That current position — a row and column, or an offset into the 2000-cell (80×25) buffer — is the cursor. A minimal kernel manages it in software, writing characters to the buffer and advancing the position, exactly like `Console.Write` on a managed OS.

## Detailed explanation
The VGA text mode is a 25-row × 80-column grid of 2-byte cells starting at `0xB8000`, for a total of 80 × 25 = 2000 cells. A character cell stores the ASCII code in the low byte and its color attribute (foreground/background nibble) in the high byte. The cursor is simply the index into this buffer where the next write lands.

A text-mode cursor in a hand-rolled kernel is typically processed in two parts:

1. **Software position tracking** — the kernel keeps a `row`/`column` (or a buffer offset) and, when the next character arrives, writes `character | (attribute << 8)` at `0xB8000 + 2 * (row * 80 + column)`, then advances the column, wrapping to the next row at column 80.

2. **Hardware cursor shape/position** — the VGA text controller also exposes a *hardware* cursor, positioned by writing its 16-bit offset to two I/O ports: select the "cursor location high" register on port `0x3D4`, write the high byte to `0x3D5`, then repeat for the low byte. The kernel doesn't strictly have to move the hardware cursor to print text, but doing so keeps the blinking block in sync.

The Cosmos C# kernel's `Console.Write`/`Console.Clear` use a cursor under the hood too — `Kernel.cs` calls `Console.Write("> ")` inside its `Run()` loop, and the framework manages cursor position for you.

## Why it matters here (OSDev_Learning_Hub)
- `Example_OS_Project/c/kernel.c` and `Example_OS_Project/rust/src/main.rs` — a minimal VGA driver that tracks a cursor position while writing to `0xB8000`.
- `Example_OS_Project/csharp/Kernel.cs` — the Cosmos `Console.Write("> ")` prompt whose cursor is managed by the framework.
- `Example_OS_Project/tools/read_vga_text.py` — reads the text buffer, whose 2000-cell layout depends on cursor convention.

## Watch / listen
[- Writing an OS in Rust - Part 3 - VGA Text Mode - Uncle Scientist](https://www.youtube.com/watch?v=DA2zIAkE26Q) — driving the text-mode cursor
- [OSDev Wiki — Text UI](https://wiki.osdev.org/Text_UI) — free, covers the buffer + cursor
- [OSDev Wiki — Text Mode Cursor](https://wiki.osdev.org/Text_Mode_Cursor) — free, the port-based hardware cursor

## Related terms
- [VGA Text Mode](vga-text-mode.md)
- [Memory-Mapped I/O](memory-mapped-io.md)
- [x86](x86.md)
- [Kernel](kernel.md)

---
*Grounded in the OSDev_Learning_Hub tutorials, the OSDev Wiki (free), and standard OS-dev references.*
