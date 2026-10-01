# OS Development Communities

Categorized list of real online communities for operating-system and low-level development: forums, Discords, subreddits, mailing lists, IRC, GitHub organizations, Q&A sites, and newsletters. Every link was verified reachable at curation time. Discord invites in particular can expire — if one is dead, check the linked project's README or website for the current invite.

## Forums

- **OSDev Forum (forum.osdev.org)** – The canonical OS-dev forum and the home of the OSDev Wiki community; huge archives, an explicit *OS Development* board plus *OS Design & Theory*. https://forum.osdev.org
- **OSDev Wiki (wiki.osdev.org)** – Not a forum, but the community's shared reference wiki: bare-bones tutorials, hardware specs, and beginner guides. https://wiki.osdev.org
- **OSDev.wiki** – Community-maintained mirror/companion with extra articles (incl. the *Chat* page that documents current Discord/IRC/Matrix rooms). https://osdev.wiki
- **Raspberry Pi Forums – "Bare metal, Assembly language"** – Active bare-metal and OS-dev board for writing programs/OSes on ARM Raspberry Pi. https://forums.raspberrypi.com

## Discord & Real-Time Chat

- **Operating System Development (Discord)** – The largest OS-dev Discord server (2,000+ online, 15K+ members); invite channelled via `discord.gg/osdev` and also `discord.gg/RnCtsqD`. Verified live. https://discord.gg/osdev
- **OSDev.wiki *Chat* page** – Maintained list of the OS-dev Discord invite plus FOSS alternatives (Matrix, Revolt). https://osdev.wiki/wiki/Chat
- **#osdev on Matrix** – The OS-dev space on the Matrix protocol: `#osdev:matrix.org`. https://matrix.to/#/#osdev:matrix.org
- **Project Discords** – SerenityOS, Redox, and other hobby-OS projects run their own Discords; find the current invite in each project's GitHub README (e.g. `github.com/SerenityOS/serenity`, `github.com/redox-os`).
- **Redox OS Discord / community** – The Rust OS community (Redox is a from-scratch Rust OS); find the current invite in the project's GitHub README. https://github.com/redox-os/redox
- **r/embedded Discord (official)** – Large, active embedded/bare-metal Discord; find the invite via the subreddit sidebar. https://www.reddit.com/r/embedded/

## Subreddits

- **r/osdev** – The main OS-development subreddit; share projects, ask beginner questions, and find series recommendations. https://www.reddit.com/r/osdev/
- **r/OperatingSystems** – General OS theory, design, and news. https://www.reddit.com/r/OperatingSystems/
- **r/LowLevel** – Low-level programming, kernels, embedded, and minimal OSes. https://www.reddit.com/r/LowLevel/
- **r/kerneldevelopment** – Kernel development (Linux-focused but welcome to systems dev generally). https://www.reddit.com/r/kerneldevelopment/
- **r/Compilers** – Compiler and language-implementation discussion; highly relevant to the bootstrapping/ELF side of OSdev. https://www.reddit.com/r/Compilers/
- **r/embedded** – Embedded systems and bare-metal programming; an active community for OS-adjacent hardware work. https://www.reddit.com/r/embedded/
- **r/ReverseEngineering** – Reverse engineering of binaries and systems; useful for understanding ELF/PE, loaders, and debuggers. https://www.reddit.com/r/ReverseEngineering/
- **r/programming** – General programming subreddit; OS-dev and low-level posts regularly surface under it. https://www.reddit.com/r/programming/
- **r/AskComputerScience** – Ask-me-style forum for comp-sci fundamentals (OS, architecture theory). https://www.reddit.com/r/AskComputerScience/

## Mailing Lists

- **LKML – Linux Kernel Mailing List** – The de-facto kernel development mailing list (not friendly to spam, but essential for learning how kernel dev by email works). https://lkml.org
- **LKML via Lore** – The modern web/NNTP archive and interface to the Linux Kernel Mailing List (see also lkml.org). https://lore.kernel.org/lkml/
- **vger.kernel.org list index** – Hosts the Linux kernel and related subsystem mailing lists. https://vger.kernel.org/vger-lists.html#linux-kernel
- **Kernelnewbies Mailing List** – Beginner-friendly kernel-development list (paired with the wiki/IRC). https://kernelnewbies.org/MailingList
- **FreeBSD — Developer & System lists (freebsd-hackers, freebsd-drivers, freebsd-arch)** – the technical lists behind a real production OS. https://www.freebsd.org/community/mailinglists.html
- **lists.freebsd.org** – Web archives of all FreeBSD mailing lists, searchable for OS-design threads. https://lists.freebsd.org/
- **rust-osdev** – The Rust OS-dev community runs its discussions around GitHub; see below.

## IRC

- **#osdev on Libera.Chat** – The long-running (20+ year) OS-dev IRC channel; many OSDev.org regulars idle there. Connect to `irc.libera.chat` and `/join #osdev`. https://web.libera.chat/?channel=#osdev
- **Channel logs** – Searchable public IRC history for #osdev. https://libera.irclog.whitequark.org/osdev
- **#kernelnewbies on IRC (irc.oftc.net)** – The beginner kernel-development IRC channel (pair with the MailingList above). https://kernelnewbies.org/IRC

## GitHub Organizations & Reading Lists

- **rust-osdev** – The umbrella org for Rust OS-dev crates (bootloader, x86_64, vga, etc.). https://github.com/rust-osdev
- **phil-opp / blog_os & os.phil-opp.com** – The *Writing an OS in Rust* blog + source. https://os.phil-opp.com
- **SerenityOS/serenity** – Reference hobby OS worth reading/browsing as a full example. https://github.com/SerenityOS/serenity
- **mit-pdos/xv6-riscv** – MIT's xv6 used to teach OS design. https://github.com/mit-pdos/xv6-riscv
- **nanobyte-dev/nanobyte_os** – Source for the *Building an OS* series. https://github.com/nanobyte-dev/nanobyte_os
- **davidcallanan/os-series** – Source for the OS Dev video series. https://github.com/davidcallanan/os-series
- **cfenollosa/os-tutorial** – Text tutorial for bootloaders + a kernel. https://github.com/cfenollosa/os-tutorial
- **rezgui/AwesomeOS** – Curated list of OS-dev resources (orgs, papers, tutorials). https://github.com/rezgui/AwesomeOS
- **codecrafters-io/build-your-own-x** – The famous "build your own OS" and related challenge list. https://github.com/codecrafters-io/build-your-own-x

### Language-specific projects on GitHub
- **Go** – **gopher-os/gopher-os** (proof-of-concept Go kernel), **dmarro89/go-dav-os**, **icexin/eggos** (Go unikernel). https://github.com/gopher-os/gopher-os
- **C#** – **CosmosOS/Cosmos** (C# OS construction kit). https://github.com/CosmosOS/Cosmos
- **Rust (bare metal)** – **rust-osdev/bootloader**, plus the `blog_os` resources above.

## Q&A Sites

- **Stack Overflow – `operating-system` tag** – Practical kernel/OS implementation questions and answers. https://stackoverflow.com/questions/tagged/operating-system
- **Stack Overflow – `kernel` and `osdev` tags** – Follow alongside the above. https://stackoverflow.com/questions/tagged/kernel

## Newsletters & Aggregators

- **os.phil-opp.com** – The Rust "Writing an OS" blog; updated with new posts and a mailing-list/blog-style feed. https://os.phil-opp.com
- **OSNews** – Long-running magazine/blog aggregating OS, kernel, UI, and hardware news. https://osnews.com/
- **LWN.net** – Reader-supported Linux/OS news with the best kernel coverage (a key "OSdev current events" source). https://lwn.net/
- **Kernelnewbies LinuxChanges** – A per-release plain-language summary of what's new in the kernel. https://kernelnewbies.org/LinuxChanges
- **Hacker News** – Frequent high-quality OS-dev projects and discussions under `show hn`/`operating system`. https://news.ycombinator.com
- **Lobsters** – Tech community where deep OS and systems posts regularly surface (invite-gated, public read of /newest). https://lobste.rs
