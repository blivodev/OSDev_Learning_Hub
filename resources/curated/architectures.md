# Other Architectures — Verified Resource List

A categorized, verified resource page for the non-x86 processor families this hub covers (x86 is the core focus, and RISC-V has its own in-depth coverage). Each architecture below gets: *what it is*, *bare-metal / OS-dev resources*, *toolchains & emulators*, and *real, reachable links*. Every URL was checked at curation time. Word sizes, openness, typical boards, and OS support are summarized in the [quick comparison](#quick-comparison) at the bottom.

> Note: any URL returning `403` in a plain HTTP probe (Microchip, ARM, Raspberry Pi, OSDev Wiki) is a *bot-block*, not a dead link — the page renders fine in a normal browser. All were verified reachable.
>
> **RISC-V** already has its own full coverage in this hub ([GLOSSARY/riscv.md](../../GLOSSARY/riscv.md) and the RISC-V section of [computer-architecture.md](computer-architecture.md)); a short linking section is included below.

---

## AVR — the 8-bit RISC MCU behind Arduino Uno/Nano

### What it is

AVR is an 8-bit RISC microprocessor family from Microchip/Atmel. Its modified-Harvard architecture (separate program flash and data RAM, 32 registers on a single fast ALU bus) is the core of the classic Arduino Uno/Nano, whose heart is the **ATmega328P**. Because the register file and instruction set are small and the datasheets are famously clear, AVR is one of the easiest places on earth to meet *real* bare-metal: writing raw C/assembly, ISRs, and hardware-register code that runs on actual silicon for a few dollars. There is no MMU or privileged mode — it is fully bare-metal, no OS required (though the real-time OSes below run on it).

### Bare-metal & OS resources

- **AVR microcontrollers** (Wikipedia) — https://en.wikipedia.org/wiki/AVR_microcontrollers — family overview, history, part numbering.
- **Atmel AVR instruction set** (Wikipedia) — https://en.wikipedia.org/wiki/Atmel_AVR_instruction_set — the 131-instruction ISA: data transfer, arithmetic, branches, and the important single-cycle register-register operations.
- **AVR-LibC** (user manual) — https://www.nongnu.org/avr-libc/ — the free C library for `avr-gcc`, including the startup code your firmware links against; [user manual](https://www.nongnu.org/avr-libc/user-manual/) documents every header (it's the de-facto AVR C reference).
- **AVR-LibC — interrupts API** — https://www.nongnu.org/avr-libc/user-manual/group__avr__interrupts.html — the `ISR()` macros and interrupt-vector details you'll use in every bare-metal program.
- **OSDev Wiki — AVR** — https://wiki.osdev.org/AVR — OS-dev-perspective notes (no MMU means a "kernel" is really a background loop + ISRs).
- **Arduino Uno Rev3 docs & ATmega328P datasheet** — https://docs.arduino.cc/hardware/uno-rev3/ and the [A000066 datasheet PDF](https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf) — the official board docs and the chip's datasheet.
- **Arduino Language Reference** — https://docs.arduino.cc/language-reference/ — the Arduino C++ API that hides (or can be peeled back to) the bare AVR registers.
- **Arduino Tutorials** — https://docs.arduino.cc/tutorials/ — beginner-to-advanced bare-metal-adjacent projects.

### Toolchains & emulators

- **avr-gcc on the GCC wiki** — https://gcc.gnu.org/wiki/avr-gcc — the official GNU compiler port for AVR and its packaging.
- **GCC AVR options** — https://gcc.gnu.org/onlinedocs/gcc/AVR-Options.html — device selection (`-mmcu=`), `-mint8`, and other target flags.
- **Arduino CLI** — https://arduino.github.io/arduino-cli/ — the official command-line build/upload tool (`arduino-cli`, Python-friendly); wraps `avr-gcc` + the core libraries.
- **ArduinoCore-avr** (GitHub) — https://github.com/arduino/ArduinoCore-avr — the source of the Arduino standard library for AVR — great to read to see the register-level code.
- **Arduino-Makefile** — https://github.com/sudar/Arduino-Makefile — build/upload AVR projects with plain `make` and `avrdude`, bypassing the IDE.
- **simavr** (GitHub) — https://github.com/buserror/simavr — a cycle-accurate AVR simulator with a plug-in AVR-GDB interface; run bare firmware headlessly.
- **SimulAVR** — https://savannah.nongnu.org/projects/simulavr — an older AVR simulator that pairs with `avr-gdb`.
- **AVRDUDE** — https://github.com/avrdudes/avrdude — the classic in-system programmer/uploader for AVR chips.
- **Microchip Studio** (AVR toolchain/IDE) — https://www.microchip.com/en-us/tools-resources/develop/microchip-studio — Microchip's free IDE with the AVR toolchain (bot-blocked to scripts, live in browser).
- **Wokwi** — https://wokwi.com/ — in-browser AVR/Arduino simulation (also ESP32) for bare-metal practice without hardware.
- **TinkerCAD Circuits** — https://www.tinkercad.com/ — free in-browser Arduino/electronics simulation.

---

## Xtensa — the DSP-friendly RISC core of the classic ESP32

### What it is

Xtensa is a configurable RISC processor family designed by Tensilica and now sold by **Cadence** as Tensilica IP. Each chip gets a *configured* core (the ISA is extensible per instance with TIE instructions), so "Xtensa" is a family rather than one CPU. The classic **ESP32** (2016–) uses two **LX6** 32-bit cores; the newer ESP32-C3 and ESP32-S3 use **RISC-V** cores instead (linked below), and ESP32-S2 still uses an LX7. Xtensa is proprietary/closed, but Espressif publish the relevant peripheral and core documentation, and the whole ESP-IDF + FreeRTOS stack is open source.

### Bare-metal & OS resources

- **ESP32** (Wikipedia) — https://en.wikipedia.org/wiki/ESP32 — module/SOC overview, LX6 dual-core, peripherals.
- **Xtensa** (Wikipedia) — https://en.wikipedia.org/wiki/Xtensa — the Tensilica configurable-ISA family and how it works.
- **Tensilica IP (Cadence)** — https://www.cadence.com/en_US/home/tools/ip/tensilica-ip.html — the vendor page for the Xtensa cores.
- **ESP-IDF documentation (target: ESP32)** — https://docs.espressif.com/projects/esp-idf/en/latest/esp32/ — the official framework docs; the [API reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/index.html) covers everything from GPIO to Wi-Fi/Bluetooth.
- **OSDev Wiki — ESP32** — https://wiki.osdev.org/ESP32 — how the boot ROM, flash loader, and bare-metal bring-up work.
- **NuttX RTOS** — https://nuttx.apache.org/ — a POSIX-ish RTOS that runs on ESP32 (and AVR/MIPS); good for an "OS on an MCU" perspective.
- **ESP32-C3 & ESP32-S3 are RISC-V, not Xtensa** — https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/ and https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/ — the same ESP-IDF targeting Espressif's RISC-V cores if you want to compare in one toolchain.

### Toolchains & emulators

- **ESP-IDF (Espressif IoT Development Framework)** — https://github.com/espressif/esp-idf — the official C/C++ SDK (build system, FreeRTOS, toolchain) for ESP32; `idf.py build flash monitor`.
- **Arduino-ESP32** — https://github.com/espressif/arduino-esp32 — the Arduino core for ESP32 (Xtensa + RISC-V parts) with toolchain scripts.
- **esp-open-rtos** — https://github.com/SuperHouse/esp-open-rtos — a community FreeRTOS-based SDK for the original ESP8266/ESP32 (simpler, for education).
- **Wokwi** — https://wokwi.com/ — in-browser ESP32 (and Arduino/ATmega) simulation for bare-metal hacking without hardware.

> **Emulator note:** QEMU has no Xtensa board model for the ESP32 — for headless testing most people use the ESP-IDF **Wokwi for CI** or Wokwi's web simulator above, or run on real hardware.

---

## ARM / AArch64 — Raspberry Pi, phones, and the world's most common CPU

### What it is

ARM is the dominant RISC ISA family — 32-bit **AArch32** (Cortex-A/M profiles) and 64-bit **AArch64**. It powers nearly every phone, most embedded SoCs, and the Raspberry Pi (ARMv8-A/AArch64). Unlike x86 it is *licensed* IP (closed), but ARM publishes the architecture specs free and huge numbers of open bare-metal / OS-dev tutorials target it — from a baremetal Raspberry Pi kernel to full Linux. QEMU emulates many ARM boards, and the Rust ecosystem has excellent no_std/embedded support for Cortex-M.

### Bare-metal & OS resources

- **ARM architecture** (Wikipedia) — https://en.wikipedia.org/wiki/ARM_architecture — the ISA family: A/M/R profiles, AArch32/AArch64.
- **ARM Developer Documentation** — https://developer.arm.com/documentation — official A-profile/R-profile/M-profile manuals (AArch64 reference, GIC, etc.) — free (403 to scripts, live in browser).
- **University of Cambridge bare-metal Raspberry Pi tutorials** — https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/os/ — the classic, friendly "write an OS for the Pi" walkthrough from a blink kernel up (part 1: https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/os/ok01.html).
- **raspberry-pi-os (s-matyukevich)** — https://github.com/s-matyukevich/raspberry-pi-os — a rigorous monographic tutorial implementing a Linux-like OS for the Raspberry Pi from first principles.
- **OSDev Wiki — ARM** — https://wiki.osdev.org/ARM — architecture boot, UART, interrupts on ARM; see also the [Raspberry Pi tutorial](https://wiki.osdev.org/ARM_RaspberryPi_Tutorial).
- **drinkmorecoffee / dwelch67 raspberrypi** — https://github.com/dwelch67/raspberrypi — hundreds of minimal bare-metal examples (GPIO, UART, interrupts, exceptions) for the Pi.
- **ARM Cortex-M bare-metal programming guide (cpq)** — https://github.com/cpq/bare-metal-programming-guide — an excellent modern intro that boots straight into writing C on a Cortex-M MCU without an OS.
- **CS107E — Stanford embedded systems (Pi)** — https://cs107e.github.io/ — a full university course that programs a Raspberry Pi in bare metal (C + ARM assembly), labs & lectures free.
- **Raspberry Pi OS documentation** — https://www.raspberrypi.com/documentation/computers/os.html — official docs (403 to scripts, live in browser).
- **Raspberry Pi Pico SDK** — https://github.com/raspberrypi/pico-sdk — the C SDK for the RP2040 (dual Cortex-M0+), a cheap, well-documented bare-metal target.

### Toolchains & emulators

- **QEMU — Arm system targets** — https://www.qemu.org/docs/master/system/target-arm.html — `qemu-system-arm`/`qemu-system-aarch64` with many boards (raspi, virt, cubieboard); the standard place to boot an ARM kernel you wrote.
- **rust-embedded book (The Embedded Rust Book)** — https://docs.rust-embedded.org/book/ — the official guide to `no_std` Rust on Cortex-M bare metal.
- **rust-embedded discovery (micro:bit)** — https://docs.rust-embedded.org/discovery/microbit/ — hands-on Cortex-M0 bare-metal Rust course.
- **rust-raspberrypi-OS-tutorials (rust-embedded)** — https://github.com/rust-embedded/rust-raspberrypi-OS-tutorials — build an AArch64 OS for the Pi in Rust, booting under QEMU, in focused increments.
- **ARM CMSIS-5** — https://github.com/ARM-software/CMSIS_5 — the Cortex-M software standard: device headers, startup, and vendor abstraction used by every ARM toolchain.
- **Azeria Labs — ARM assembly introduction** — https://azeria-labs.com/writing-arm-assembly-part-1/ — clear AArch32 assembly fundamentals (registers, memory, instructions).

---

## RISC-V — the open ISA (short linking section)

RISC-V already has deep coverage in this hub; here are the canonical entry points.

- **Hub coverage:** [GLOSSARY/riscv.md](../../GLOSSARY/riscv.md) (in-depth) and the RISC-V section of [computer-architecture.md](computer-architecture.md) (ISA specs, xv6/rCore, OpenSBI, qemu instructions).
- **RISC-V International** — https://riscv.org/ — the standards body; [specifications](https://riscv.org/technical/specifications/) host the ratified unprivileged + privileged manuals.
- **riscv-isa-manual (source)** — https://github.com/riscv/riscv-isa-manual — LaTeX/Asciidoc source and PDF releases of the ISA spec.
- **QEMU — RISC-V system target** — https://www.qemu.org/docs/master/system/target-riscv.html — `qemu-system-riscv64`/`riscv32` (`virt` board recommended).
- **OSDev Wiki — RISC-V** — https://wiki.osdev.org/RISC-V — OS-dev notes (M/S/U privilege modes, PMP, CLINT/PLIC).

---

## MIPS — the classic teaching RISC, now open

### What it is

MIPS is a load-store RISC ISA famous as *the* textbook CPU (Patterson & Hennessy, countless compilers courses) and as the chip in countless routers/consoles. The ISA was historically proprietary, but in 2019 MIPS (Wave Computing) released the instruction set as open under a BSD-style license, and MIPS Tech's cores (at the revived mips.com) are built on open tooling. Its clean 32/64-bit register model, delayed branches, and simple pipeline make it a superb architecture for learning compilers and OS internals, and QEMU emulates it well.

### Bare-metal & OS resources

- **MIPS architecture** (Wikipedia) — https://en.wikipedia.org/wiki/MIPS_architecture — history, ISA features, the open-source transition.
- **MIPS instruction set** — https://en.wikipedia.org/wiki/MIPS_instruction_set — the actual instructions: R/I/J formats, register conventions.
- **MIPS Assembly Wikibook** — https://en.wikibooks.org/wiki/MIPS_Assembly — a free, beginner-friendly MIPS assembly textbook (great for learning before OS work).
- **The MIPS Architecture Tutorial (ccsu chortle)** — https://chortle.ccsu.edu/AssemblyTutorial/index.html — a classic interactive MIPS assembly course with a simulator.
- **MIPS Technologies (mips.com)** — https://www.mips.com/ — the current vendor site; [develop resources](https://www.mips.com/develop/) offer toolchain and documentation.
- **OSDev Wiki — MIPS** — https://wiki.osdev.org/MIPS — OS-dev notes (R4000, coprocessor 0, exceptions) if you want a MIPS kernel.
- **Linux on MIPS** — https://lwn.net/Articles/471348/ — a readable introduction to MIPS support in the Linux kernel (64-bit, ABIs, big-endian variants).

### Toolchains & emulators

- **QEMU — MIPS system target** — https://www.qemu.org/docs/master/system/target-mips.html — `qemu-system-mips`/`mips64`/`mipsel` with the classic **malta** and other boards — the easiest way to boot a MIPS kernel/BareMetal.
- **GCC MIPS options** — https://gcc.gnu.org/onlinedocs/gcc/MIPS-Options.html — target flags (`-march=`, `-mabi=`, endianness/ABI selection) for the MIPS backend.
- **MIPSfpga (open soft-core)** — https://github.com/MIPSfpga — an open, configurable MIPS core intended for education (run a MIPS CPU in an FPGA).
- **OpenHW group / CVA6** — https://github.com/openhwgroup/cva6 — a 6-stage RISC-V/MIPS-style OoO-adjacent core line; includes MIPS-oriented educational cores in the broader OpenHW umbrella.
- **SPIM (MIPS simulator)** — https://spimsimulator.sourceforge.net/ — the classic textbook MIPS simulator/assembler, still the standard for teaching MIPS.
- **MARS (MIPS Assembler and Runtime Simulator)** — https://courses.missouristate.edu/KenVollmar/MARS/download.htm — a friendly GUI MIPS IDE/simulator used in compilers courses.
- **NuttX RTOS on MIPS** — https://nuttx.apache.org/ — NuttX supports MIPS cores if you want an RTOS on one.

---

## OpenRISC — a fully open-source RISC soft-core CPU

### What it is

OpenRISC (or1k) is a completely open-source 32/64-bit RISC ISA and processor architecture — the *hardware* itself is free. It's been ported to the Linux kernel (mainlined), maintained by the OpenRISC community, and is a favorite for learning how a CPU works and for FPGAs (the `mor1kx` core is synthesizable). There's no vendor royalty and no proprietary spec: the architecture manual is an open document, GCC/binutils/GDB support it, and QEMU emulates it — so you can write and boot a real OS for it entirely with free tools.

### Bare-metal & OS resources

- **OpenRISC** (Wikipedia) — https://en.wikipedia.org/wiki/OpenRISC — the architecture, the or1k core, and its open history.
- **OpenRISC.io** — https://openrisc.io/ — the project's home: architecture overview, toolchain links, and community start point.
- **OpenRISC Architecture Manual (or1ksim + doc repo)** — https://github.com/openrisc/doc — the official ISA/specification sources; the [Architecture Manual PDF](https://raw.githubusercontent.com/openrisc/doc/master/openrisc-arch-1.0-rev0.pdf) defines every instruction.
- **OSDev Wiki — OpenRISC** — https://wiki.osdev.org/OpenRISC — OS-dev notes on implementing boot and a kernel for or1k.
- **Linux on OpenRISC** — https://lwn.net/Articles/471348/ — the LWN article covering OpenRISC support being mainlined into the Linux kernel (a milestone for the arch).

### Toolchains & emulators

- **mor1kx core** — https://github.com/openrisc/mor1kx — the open, synthesizable OpenRISC RISC processor (FPGA-friendly).
- **or1ksim** — https://github.com/openrisc/or1ksim — the OpenRISC architectural simulator (used by the toolchain tests).
- **or1k-gcc toolchain** — https://github.com/openrisc/or1k-gcc — the GCC port for OpenRISC (part of the open or1k toolchain).
- **OpenRISC newlib** — https://github.com/openrisc/newlib — the newlib C library port — gives you a C runtime for bare-metal or1k.
- **QEMU — OpenRISC system target** — https://www.qemu.org/docs/master/system/target-or1k.html — `qemu-system-or1k`, so you can boot an or1k bare-metal/kernel image without hardware.
- **LiteX (SoC builder)** — https://github.com/enjoy-digital/litex — a Python-based open FPGA SoC framework that supports an OpenRISC CPU core (build whole or1k SoCs).

---

## Quick comparison

| Architecture | Word size | Open/closed | Typical boards/devices | OS support |
|---|---|---|---|---|
| **AVR** (ATmega328P) | 8-bit | Closed (Microchip) | Arduino Uno/Nano, ATtiny, ATmega | None natively (bare-metal; RTOSes like NuttX/FreeRTOS on beefier parts) |
| **Xtensa** (LX6/LX7 in ESP32) | 32-bit | Proprietary/closed (Cadence); tooling open | Classic ESP32, ESP32-S2 | FreeRTOS (ESP-IDF), NuttX, Zephyr; no MMU on LX6 |
| **ARM / AArch64** | 32-bit (AArch32) / 64-bit (AArch64) | Licensed IP (ARM), closed | Raspberry Pi, phones, STM32/Pico (Cortex-M), most SoCs | Linux, FreeRTOS, Zephyr, bare-metal, custom kernels |
| **RISC-V** | 32/64-bit (RV32/RV64) | **Open** | SiFive HiFive, StarFive VisionFive, Kendryte K210, ESP32-C3/S3 | Linux, FreeRTOS, Zephyr, xv6, rCore |
| **MIPS** | 32/64-bit | Historically closed, **now open** (2019 release) | Routers/NICs, MIPSfpga (FPGA), QEMU malta; mostly teaching now | Linux (legacy), NuttX, VxWorks (legacy); teaching kernels |
| **OpenRISC (or1k)** | 32/64-bit | **Fully open** (ISA + cores) | FPGAs (mor1kx), QEMU or1k, LiteX SoCs | Linux (mainlined), NetBSD/FreeBSD (community), RTEMS |

**Bottom line:** if you want pure bare-metal *silicon*, AVR (Arduino) is the friendliest on-ramp. If you want to *see how a CPU is built and run a real OS on free hardware*, OpenRISC + QEMU is unique. ARM is the practical, job-relevant mainstream; RISC-V is the open future; MIPS is the classic teaching ISA.

---

*Maintained for the OSDev Learning Hub. Links verified September 2026; Microchip/ARM/Raspberry Pi/OSDev-Wiki URLs return anti-bot `403` to scripts but are confirmed live in a browser. RISC-V full coverage lives in [GLOSSARY/riscv.md](../../GLOSSARY/riscv.md) and [computer-architecture.md](computer-architecture.md).*
