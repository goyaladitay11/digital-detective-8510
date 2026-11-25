# Mission 3 — Understand the operating system

## 1. Task / objective
Explore my operating system from the Terminal: system details, current account, storage and running activity. Learn
about processes and PIDs, absolute vs relative paths, file permissions, and the main jobs of an operating system.

## 2. Work completed
- Collected OS, account, storage and activity information (Task 3.1) and redacted personal details.
- Viewed the running process list and identified PIDs of real processes (Task 3.2).
- Moved between the assignment folder and a subfolder, compared absolute and relative paths, and read the permission
  letters of a practice file (Task 3.3).
- Explained six OS responsibilities with examples (Task 3.4).
- Saved the redacted output in [`../evidence/mission-03-os-output.txt`](../evidence/mission-03-os-output.txt).

### Task 3.1 — Explore my operating system

| Information explored | Command | What it tells me | My observation (privacy-safe) |
|----------------------|---------|------------------|-------------------------------|
| Operating system / system details | `sw_vers`, `uname -srm` | Name and version of the OS, the kernel and the CPU architecture. | macOS 27.2.1, Darwin kernel 27.2.0, `arm64` (Apple Silicon) processor. |
| Current account identity | `whoami` | Which user account is running the commands — this decides what files I am allowed to touch. | A normal (non-admin) user: `[redacted]`. |
| Available and used storage | `df -h /` | Total size, used space and free space of the main disk, in readable units. | 460 GiB disk, 13 GiB used by the system volume, 197 GiB available (7% capacity on `/`). |
| System activity snapshot | `top -l 1` | A one-time picture of processes, CPU load and memory use. | 579 processes (3 running, 576 sleeping), CPU about 75% idle, about 15 GB of memory in use. |

### Task 3.2 — Understand processes
I opened Safari and a text editor, then used `ps -ax -o pid,comm` (and `top`) to see the running processes.

| PID | Process | What it is |
|-----|---------|------------|
| 1 | `launchd` | The first process macOS starts; it launches and manages other services. |
| 610 | `WindowServer` | Draws all the windows on the screen. |
| 1302 | `Dock` | The Dock at the bottom of the screen. |
| 1304 | `Finder` | The file manager app. |

- **What is a process?** A process is a program that is currently running in memory. The same program can even run as
  several processes. When I quit the program, its process ends.
- **What does PID represent?** The Process ID — a unique number the OS gives each running process so it can track it,
  share CPU time and memory, or stop it if needed.
- **Two examples running on my computer:** `Finder` (PID 1304) and `Dock` (PID 1302). Background examples include
  `launchd` and `WindowServer`.

### Task 3.3 — Paths and permissions
I moved into a subfolder and back:

```
$ pwd
/Users/[redacted]/.../digital-detective-8510
$ cd mission-02-terminal/terminal-practice && pwd
/Users/[redacted]/.../digital-detective-8510/mission-02-terminal/terminal-practice
$ cd ../.. && pwd
/Users/[redacted]/.../digital-detective-8510
```

- **Absolute path:** the full address starting from the root `/`. It works from anywhere.
  Example: `/Users/[redacted]/.../digital-detective-8510/mission-05-numbers-data/number_converter.py`
- **Relative path:** an address starting from the folder I am in now. It is shorter but depends on my location.
  Example (from the repo folder): `mission-02-terminal/terminal-practice/clue.txt`, or `../..` to go up two levels.

**Permissions of `clue.txt`:** `ls -l` showed `-rw-r--r--`.

| Part | Letters | Meaning for this file |
|------|---------|-----------------------|
| File type | `-` | A normal file (a folder would show `d`). |
| Owner | `rw-` | The owner (me) **can read** and **can write**, but **cannot execute** it. |
| Group | `r--` | Group members can only read. |
| Others | `r--` | Everyone else can only read. |

| Permission | Meaning | Example |
|------------|---------|---------|
| r — Read | Allows a file's contents to be read. | Opening a text file. |
| w — Write | Allows a file to be changed. | Editing a text file. |
| x — Execute | Allows a file to be run; on a directory, allows access/traversal. | Running a script. |

I did not change any permissions.

### Task 3.4 — Operating-system responsibilities

| OS responsibility | My explanation | Example |
|-------------------|----------------|---------|
| Process management | The OS starts and stops programs and shares CPU time between them so many seem to run at once. | Music keeps playing while I type in the editor; each has its own PID. |
| Memory management | The OS gives each program its own part of RAM, keeps programs from touching each other's memory, and frees memory when a program closes. If RAM is full it compresses or swaps data. | `top` showed memory in use and "compressor" memory. |
| Device management | The OS talks to hardware through drivers so apps do not need to know how each device works. | Plugging in headphones and the sound switches automatically. |
| File management | The OS organises data into files and folders, tracks where they are stored on disk, and handles creating, copying and deleting them. | `mkdir`, `cp`, `mv` in Mission 2. |
| User interface / shell | The OS gives me a way to give it commands — a graphical desktop or a text shell. | The macOS desktop and Dock (GUI) and `zsh` in Terminal (shell). |
| Security and permissions | The OS checks who I am and what I am allowed to do, using accounts, passwords and file permissions. | `clue.txt` is `rw-r--r--`, so other users cannot edit it; system files need admin rights. |

## 3. Commands / tools used
| Command | Purpose |
|---------|---------|
| `sw_vers`, `uname -srm` | Show OS name/version, kernel and CPU architecture |
| `whoami` | Show the current account name |
| `df -h /` | Show disk size, used and free space |
| `top -l 1` | Take one snapshot of running activity |
| `ps -ax -o pid,comm` | List running processes with their PIDs |
| `pwd`, `cd`, `cd ../..` | Show and change location (absolute vs relative paths) |
| `ls -l` | Show permission letters of a file |

## 4. My understanding
The operating system is the manager between me, my programs and the hardware. Every program I open becomes a process
with its own PID, and the OS shares CPU and memory between hundreds of them — most are background processes I never see.
Files are found with paths: absolute paths are full addresses from `/`, relative paths depend on where I am. Permissions
(`r`, `w`, `x` for owner, group and others) are how the OS protects files from being read or changed by the wrong user,
which is why I should never use admin rights to change system files.

## 5. Difficulties faced
- The `top` command kept refreshing and did not stop on its own.
- The outputs of `whoami`, `pwd` and `ls -l` contained my username, and `uname -a` contained my computer's name.

## 6. How I resolved them
- Used `top -l 1` to take a single snapshot instead of a live view (pressing `q` also quits the live view).
- Replaced my username with `[redacted]`, shortened long paths with `...`, and used `uname -srm` which does not print the
  device name.

## 7. Evidence / files
- `../evidence/mission-03-os-output.txt` — redacted Terminal output for Tasks 3.1–3.3.
- `README.md` (this file) — tables and explanations.

## 8. Commit details
- Commit message: **`Document operating system and file management`**
- Pushed to GitHub and verified that the commit is visible.
