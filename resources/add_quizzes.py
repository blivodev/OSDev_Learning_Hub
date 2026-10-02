#!/usr/bin/env python3
"""Insert interactive quiz blocks before each chapter's Exercises & Projects section."""
import re, sys

OSDEV = r"D:/Projects/OSDev-Tutorial-Site/docs/"
ELEC = r"D:/Projects/Electronics-Learning-Hub/docs/"

# quiz HTML per target file
QUIZZES = {
 OSDEV+"synthesized_tutorials/00-introduction/02-your-toolchain.md": """<div class="quiz" data-title="Quick check: your toolchain">

<div class="q" data-type="choice">
  <p class="question">Which toolchain component turns assembly into machine code?</p>
  <ul class="options">
    <li data-correct>The assembler (e.g. NASM)</li>
    <li>The linker</li>
    <li>The compiler</li>
    <li>The loader</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What does the linker do that the compiler does not?</p>
  <ul class="options">
    <li data-correct>Resolves symbol references and produces the final binary layout</li>
    <li>Optimizes the source code</li>
    <li>Checks the syntax of the code</li>
    <li>Runs the program</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: an object file (.o) is fully linked and ready to run on its own.</p>
  <ul class="options">
    <li>True</li>
    <li data-correct>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The tool that runs and tests your kernel in a virtual machine on your host is called ____ (the popular one ships as qemu-system-x86_64).</p>
  <input class="answer" data-answers="qemu, qemu system x86 64, qemu-system-x86_64, emulator">
</div>

</div>

""",
 OSDEV+"synthesized_tutorials/01-c/README.md": """<div class="quiz" data-title="Quick check: C for OS dev">

<div class="q" data-type="choice">
  <p class="question">Why is C so widely used for kernel development?</p>
  <ul class="options">
    <li data-correct>It gives direct memory control with predictable machine-code output</li>
    <li>It has automatic garbage collection</li>
    <li>It is the fastest language to write</li>
    <li>It hides all hardware details</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What does the volatile keyword tell the compiler?</p>
  <ul class="options">
    <li data-correct>That a value may change outside the program flow, so it must be re-read each time</li>
    <li>That a variable is stored in a register</li>
    <li>That a function never returns</li>
    <li>That a pointer is constant</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: writing to a fixed memory address such as the VGA buffer requires dereferencing a pointer cast to that address.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">In a freestanding kernel you avoid the standard library; the entry point must be marked ____ so the linker does not rename it (the attribute is used on the main function).</p>
  <input class="answer" data-answers="naked, no mangle, noreturn, freestanding">
</div>

</div>

""",
 OSDEV+"synthesized_tutorials/02-rust/README.md": """<div class="quiz" data-title="Quick check: Rust for OS dev">

<div class="q" data-type="choice">
  <p class="question">Which two crate attributes disable the standard library in a kernel?</p>
  <ul class="options">
    <li data-correct>no_std and no_main</li>
    <li>no_std and no_alloc</li>
    <li>bare_metal and no_std</li>
    <li>no_main and no_alloc</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What target is used to compile Rust to a bare-metal x86_64 kernel?</p>
  <ul class="options">
    <li data-correct>x86_64-unknown-none</li>
    <li>x86_64-pc-windows-msvc</li>
    <li>wasm32-unknown-unknown</li>
    <li>aarch64-unknown-linux-gnu</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: Rust's ownership rules still apply in a no_std kernel and help prevent memory bugs.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">To halt the CPU in a Rust kernel you usually write an inline ____ instruction using core::arch::asm (the mnemonic that pauses the CPU).</p>
  <input class="answer" data-answers="hlt, hlt instruction, asm hlt">
</div>

</div>

""",
 OSDEV+"synthesized_tutorials/03-cpp/README.md": """<div class="quiz" data-title="Quick check: C++ for OS dev">

<div class="q" data-type="choice">
  <p class="question">What does the extern "C" linkage specifier do?</p>
  <ul class="options">
    <li data-correct>Prevents C++ name mangling so symbols match C/assembly names</li>
    <li>Makes a function inline</li>
    <li>Links against the C standard library</li>
    <li>Declares a function static</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">Why must global constructors be handled manually in a freestanding C++ kernel?</p>
  <ul class="options">
    <li data-correct>There is no runtime (libstdc++) to call them before main</li>
    <li>Because the compiler forbids globals in kernels</li>
    <li>Because constructors are not part of C++</li>
    <li>Because the linker removes them automatically</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: in a kernel you must avoid or provide your own versions of new and delete because they normally come from the runtime.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The C++ standard function for a global constructor list that the kernel calls during startup is ____ (it takes no arguments).</p>
  <input class="answer" data-answers="init array, __cxa_atexit, __libc_csu_init, static initialization">
</div>

</div>

""",
 ELEC+"concepts/01-electricity.md": """<div class="quiz" data-title="Quick check: electricity basics">

<div class="q" data-type="choice">
  <p class="question">Voltage is best described as:</p>
  <ul class="options">
    <li data-correct>The electrical pressure (potential difference) pushing charge</li>
    <li>The amount of charge flowing per second</li>
    <li>The opposition to current</li>
    <li>The energy stored in a battery</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">Current is measured in:</p>
  <ul class="options">
    <li data-correct>Amperes (amps)</li>
    <li>Volts</li>
    <li>Ohms</li>
    <li>Watts</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: alternating current (AC) reverses direction periodically, unlike direct current (DC).</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">A 9 V battery pushing 0.5 A through a circuit delivers ____ watts of power.</p>
  <input class="answer" data-answers="4.5, 4.5 w, 4.5 watts, 4 5">
</div>

</div>

""",
 ELEC+"concepts/03-circuits.md": """<div class="quiz" data-title="Quick check: circuits & schematics">

<div class="q" data-type="choice">
  <p class="question">In a series circuit, current is:</p>
  <ul class="options">
    <li data-correct>The same through every component</li>
    <li>Divided among the components</li>
    <li>Zero in the middle components</li>
    <li>Different at each point</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What does a schematic symbol with a triangle and a line represent?</p>
  <ul class="options">
    <li data-correct>An operational amplifier (op-amp)</li>
    <li>A resistor</li>
    <li>A capacitor</li>
    <li>A ground connection</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: a short circuit is a low-resistance path that can allow dangerously large current.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">Kirchhoff's current law states that the sum of currents entering a node ____ the sum of currents leaving it (one word: equals, exceeds, or... ).</p>
  <input class="answer" data-answers="equals, is equal to, balances">
</div>

</div>

""",
 ELEC+"concepts/04-microcontrollers.md": """<div class="quiz" data-title="Quick check: microcontroller basics">

<div class="q" data-type="choice">
  <p class="question">What is the key difference between a microcontroller and a microprocessor?</p>
  <ul class="options">
    <li data-correct>A microcontroller integrates CPU, memory, and peripherals on one chip</li>
    <li>A microcontroller is faster than a microprocessor</li>
    <li>A microprocessor has built-in flash storage</li>
    <li>There is no difference</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What do GPIO pins do?</p>
  <ul class="options">
    <li data-correct>Read or write digital signals to connect to the outside world</li>
    <li>Provide the main clock signal</li>
    <li>Supply power to the board</li>
    <li>Store the firmware</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: an ADC (analog-to-digital converter) converts a continuous voltage into a discrete numeric value.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The program that runs on the microcontroller is often called ____ (the word for the low-level code stored in flash).</p>
  <input class="answer" data-answers="firmware, sketch, program">
</div>

</div>

""",
 ELEC+"synthesized/arduino-c.md": """<div class="quiz" data-title="Quick check: Arduino in C">

<div class="q" data-type="choice">
  <p class="question">In an Arduino sketch, which function runs once at startup?</p>
  <ul class="options">
    <li data-correct>setup()</li>
    <li>loop()</li>
    <li>main()</li>
    <li>init()</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What does pinMode(pin, OUTPUT) do?</p>
  <ul class="options">
    <li data-correct>Configures a pin as a digital output driver</li>
    <li>Reads the pin's voltage</li>
    <li>Turns on the built-in LED</li>
    <li>Starts the serial port</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: digitalWrite(HIGH) sets the pin to the supply voltage (usually 5 V or 3.3 V).</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The Arduino function that pauses the program for a given number of milliseconds is ____.</p>
  <input class="answer" data-answers="delay, delay()">
</div>

</div>

""",
 ELEC+"synthesized/esp32-cpp.md": """<div class="quiz" data-title="Quick check: ESP32 in C/C++">

<div class="q" data-type="choice">
  <p class="question">Which wireless interfaces does the ESP32 natively support?</p>
  <ul class="options">
    <li data-correct>Wi-Fi and Bluetooth</li>
    <li>Only Zigbee</li>
    <li>Only LoRa</li>
    <li>None - it is wired only</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What is ESP-IDF?</p>
  <ul class="options">
    <li data-correct>The official Espressif IoT Development Framework</li>
    <li>A hardware debugger</li>
    <li>A WiFi router firmware</li>
    <li>A pin layout diagram</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: the ESP32 has multiple cores (usually 2), so you can run tasks on different CPUs.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The low-power sleep mode that keeps RAM alive but pauses the CPU is called ____ sleep.</p>
  <input class="answer" data-answers="deep, deep sleep, light">
</div>

</div>

""",
 ELEC+"synthesized/embedded-rust.md": """<div class="quiz" data-title="Quick check: embedded Rust">

<div class="q" data-type="choice">
  <p class="question">What does the embedded Rust HAL (hardware abstraction layer) provide?</p>
  <ul class="options">
    <li data-correct>Safe typed access to peripheral registers</li>
    <li>A full operating system</li>
    <li>The C standard library</li>
    <li>Prebuilt device drivers for every sensor</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">Which crate generates code from a device's SVD (system view description) file?</p>
  <ul class="options">
    <li data-correct>svd2rust</li>
    <li>embedded-hal</li>
    <li>cortex-m-rt</li>
    <li>panic-halt</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: Rust's type system can encode that a GPIO pin is in input mode vs output mode at compile time.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The embedded Rust trait set that standardizes peripheral APIs across chips is called ____-hal.</p>
  <input class="answer" data-answers="embedded, embedded hal, ehal">
</div>

</div>

""",
 ELEC+"synthesized/micropython.md": """<div class="quiz" data-title="Quick check: MicroPython">

<div class="q" data-type="choice">
  <p class="question">What is MicroPython?</p>
  <ul class="options">
    <li data-correct>A compact Python interpreter for microcontrollers</li>
    <li>A Python-to-C compiler</li>
    <li>A hardware simulator</li>
    <li>A version of CPython for desktops</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">How do you blink the built-in LED on a board like the Raspberry Pi Pico in MicroPython?</p>
  <ul class="options">
    <li data-correct>Create a Pin object and toggle its value with machine.Pin</li>
    <li>Use the Arduino digitalWrite function</li>
    <li>Call os.system to run C code</li>
    <li>Edit the boot ROM</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: MicroPython code runs slower than native C but is much faster to write and iterate.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The MicroPython module that provides hardware access (pins, ADC, PWM) is called ____.</p>
  <input class="answer" data-answers="machine, machine module">
</div>

</div>

""",
 ELEC+"synthesized/rtos-on-mcu.md": """<div class="quiz" data-title="Quick check: FreeRTOS on MCU">

<div class="q" data-type="choice">
  <p class="question">What is the basic unit of work in FreeRTOS?</p>
  <ul class="options">
    <li data-correct>A task</li>
    <li>A process</li>
    <li>A thread pool</li>
    <li>A coroutine</li>
  </ul>
</div>

<div class="q" data-type="choice">
  <p class="question">What does a mutex do?</p>
  <ul class="options">
    <li data-correct>Guarantees exclusive access to a shared resource</li>
    <li>Schedules tasks in round-robin order</li>
    <li>Counts clock ticks</li>
    <li>Stops all interrupts</li>
  </ul>
</div>

<div class="q" data-type="tf">
  <p class="question">True or false: a queue in FreeRTOS is the standard way to pass data between tasks safely.</p>
  <ul class="options">
    <li data-correct>True</li>
    <li>False</li>
  </ul>
</div>

<div class="q" data-type="fill">
  <p class="question">The FreeRTOS function that creates a new task is called xTask____ (one word).</p>
  <input class="answer" data-answers="create, create, xTaskCreate">
</div>

</div>

""",
}

import os
done = 0
for path, quiz in QUIZZES.items():
    if not os.path.exists(path):
        print(f"MISSING: {path}")
        continue
    text = open(path, encoding='utf-8').read()
    marker = "## \U0001f9ea Exercises & Projects"
    if marker not in text:
        # try without emoji
        import re as _re
        m = _re.search(r'##\s+Exercises & Projects', text)
        if not m:
            print(f"NO EXERCISES MARKER: {path}")
            continue
        # insert before that heading
        idx = m.start()
    else:
        idx = text.index(marker)
    if "class=\"quiz\"" in text or "class='quiz'" in text or 'class="quiz"' in text:
        print(f"ALREADY HAS QUIZ: {path}")
        continue
    new = text[:idx] + quiz + text[idx:]
    open(path, 'w', encoding='utf-8').write(new)
    print(f"QUIZ ADDED: {path}")
    done += 1
print(f"\nTotal quizzes added: {done}/{len(QUIZZES)}")
