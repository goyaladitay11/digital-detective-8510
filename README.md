# The Digital Detective 🔍

**Diwali Independent Learning Assignment — Explore Your Computer • Build a Mini System Report**

This repository is my "mini system report". In it I investigate how my computer works: how it takes input and produces
output, how the Terminal and operating system manage files and programs, how numbers and text are stored as bits, how
Git and GitHub keep track of work, and how computers talk to each other over a network.

The work is split into **missions**. Each mission lives in its own folder with its own `README.md`. Every mission was
completed, documented, committed and pushed **separately** before the next one was started, so the commit history shows
the progress mission by mission.

## Mission index

| # | Mission | Folder |
|---|---------|--------|
| 0 | Repository and workspace setup | [mission-00-setup](mission-00-setup/README.md) |
| 1 | Computer fundamentals and IPOS | [mission-01-computer-basics](mission-01-computer-basics/README.md) |
| 2 | Terminal and file management | [mission-02-terminal](mission-02-terminal/README.md) |
| 3 | Operating system, processes and permissions | [mission-03-operating-system](mission-03-operating-system/README.md) |
| 4 | How programs run | [mission-04-programs](mission-04-programs/README.md) |
| 5 | Number systems, Python and text encoding | [mission-05-numbers-data](mission-05-numbers-data/README.md) |
| 6 | Git, GitHub, branches and Pull Requests | [mission-06-git-github](mission-06-git-github/README.md) |
| 7 | Computer networks | [mission-07-networking](mission-07-networking/README.md) |
| 8 | Final review and submission | [mission-08-final-report](mission-08-final-report/README.md) |

Privacy-safe evidence (selected Terminal outputs) is kept in [`evidence/`](evidence/).

## Topics explored
- IPOS (Input → Processing → Output → Storage), hardware vs software, OS / application / utility software
- Terminal basics: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, redirection `>` / `>>`, flags and pipes
- Package managers (Homebrew)
- Operating system: system info, storage, processes and PIDs, absolute vs relative paths, file permissions, OS duties
- Compilers vs interpreters, running a Python program
- Binary, decimal and hexadecimal conversion; ASCII and UTF-8 text encoding
- Git and GitHub: status, add, commit, log, branches, push, pull, Pull Requests
- Networks: LAN, MAN, WAN, DNS, routers, protocols, packet switching, client-server, `ping`, `nslookup`

## How to run the number converter
Requires Python 3.

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

Type a whole number such as `25` when asked. The program prints it in binary (`0b11001`) and hexadecimal (`0x19`).

## My Learning
- The Terminal can do everything the file manager does, and `pwd` + `ls` help me check where I am before changing anything.
- Every program I open becomes a process with a PID, and the operating system shares the CPU and memory between hundreds of them.
- Numbers and text are all stored as bits — binary, hex and encodings like UTF-8 are just different ways of writing them.

## Summary of what I learned
A computer is a system of hardware controlled by software, with the operating system in the middle managing processes,
memory, files, devices and security. The Terminal gives direct, precise control over that system. Programs must be
translated (compiled or interpreted) into machine code, and all data — numbers and text — ends up as bits. Git lets me
save my work in safe checkpoints and collaborate with branches and Pull Requests, and networks use protocols, DNS and
routers to move packets between clients and servers.

> No passwords, tokens, usernames, device names or private network details are stored in this repository.
