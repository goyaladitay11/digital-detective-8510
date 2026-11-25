# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface (CLI) to inspect folders, create and manage practice files safely, understand flags
(options) and pipes, and explain what a package manager does.

## 2. Work completed
- Practised nine basic Terminal operations and recorded what each one did (Task 2.1, folder `practice-folder/`).
- Created `terminal-practice/`, wrote a file with `>`, appended a second line with `>>`, made a backup and renamed it
  (Task 2.2).
- Compared `ls` with `ls -lah` and used a pipe `ls -lah | head -5` (Task 2.3).
- Checked my Homebrew version and listed the packages it manages without installing anything (Task 2.4).
- Saved the full privacy-safe Terminal output in [`../evidence/mission-02-terminal-output.txt`](../evidence/mission-02-terminal-output.txt).

### Task 2.1 — Basic Terminal operations

| Operation / command name | What it does | What I observed |
|--------------------------|--------------|-----------------|
| Current-directory display — `pwd` | Prints the full path of the folder I am working in. | It printed `/Users/[redacted]/.../digital-detective-8510/mission-02-terminal`. |
| Directory listing — `ls` | Lists the names of files and folders in the current folder. | Only `README.md` was there at the start. |
| Detailed listing — `ls -l` | Lists files with permissions, owner, size and date modified. | Each line began with letters like `-rw-r--r--` and showed the size in bytes. |
| Change directory — `cd ..` | Moves me to the parent folder (one level up). | `pwd` afterwards ended in `digital-detective-8510` instead of `mission-02-terminal`. |
| Create directory — `mkdir practice-folder` | Makes a new empty folder. | `practice-folder` appeared in the next `ls`. |
| Create empty file — `touch practice-folder/notes.txt` | Creates an empty file (or updates the time of an existing one). | `notes.txt` was created with size 0. |
| Copy file — `cp notes.txt notes-copy.txt` | Makes a second, separate copy of a file. | Both files existed after the command. |
| Move / rename file — `mv notes-copy.txt renamed-copy.txt` | Moves a file, or renames it if it stays in the same folder. | `notes-copy.txt` disappeared and `renamed-copy.txt` appeared. |
| Display file contents — `cat practice-folder/notes.txt` | Prints the text inside a file. | Nothing was printed because the file was empty. |

### Task 2.2 — Practise file changes safely
Commands used inside `terminal-practice/`:

```bash
echo "Line 1: The Digital Detective starts here." > clue.txt
echo "Line 2: Appended without deleting line 1." >> clue.txt
cat clue.txt
cp clue.txt clue-backup.txt
mv clue-backup.txt clue-backup-renamed.txt
```

`cat clue.txt` showed both lines, so the second line was added without removing the first.

**Answers**
- **Replace vs add to the end:** `>` *replaces* everything in the file with the new text (old contents are lost).
  `>>` *appends*, adding the new text after what is already there.
- **Copy vs move:** copying (`cp`) leaves the original and creates a second file, so there are two. Moving (`mv`) takes
  the same file to a new name or place, so there is still only one.
- **Current-directory display:** `pwd` tells me exactly where I am in the folder tree, as a full path from the root `/`.
  This helps me avoid creating or deleting files in the wrong place.
- **Why directory listing is useful:** `ls` lets me check what files exist before and after a command, so I can confirm
  that a command worked and I do not overwrite something by mistake.

### Task 2.3 — Flags and pipes
- `ls` only showed names: `README.md  practice-folder  terminal-practice`.
- `ls -lah` showed much more:
  - `-l` → long format: permissions, owner, group, size and date.
  - `-a` → all files, including hidden ones that start with a dot. I could now see `.` (current folder) and `..`
    (parent folder).
  - `-h` → human-readable sizes like `92B` and `160B` instead of plain byte counts.
- `ls -lah | head -5` printed only the first 5 lines of the long listing.

**What the pipe does:** the `|` symbol sends the *output* of the command on its left into the *input* of the command on
its right. Here, `ls -lah` produces the full listing, and `head -5` receives it and keeps only the first five lines. This
lets me combine small commands to get exactly the result I need.

### Task 2.4 — Package managers
Homebrew is installed on my Mac. `brew --version` showed **Homebrew 7.0.16**, and `brew list` showed it manages
**109 packages** (for example `brotli`, `ca-certificates`, `coreutils`). I did not install or uninstall anything for this task.

A package manager installs, updates and removes software with one command, instead of me downloading installers from
different websites. It also automatically installs the other packages (dependencies) that a program needs, and it can
update everything at once, which keeps my tools consistent and up to date.

## 3. Commands / tools used
| Command | Purpose |
|---------|---------|
| `pwd` | Show current folder path |
| `ls`, `ls -l`, `ls -lah` | List folder contents (normal, detailed, all + human-readable) |
| `cd` | Change folder |
| `mkdir` | Create a folder |
| `touch` | Create an empty file |
| `cp` | Copy a file |
| `mv` | Move or rename a file |
| `cat` | Display file contents |
| `echo ... >` / `echo ... >>` | Write (replace) / append text to a file |
| `head -5` | Show only the first 5 lines |
| `|` (pipe) | Send one command's output into another command |
| `brew --version`, `brew list` | Check Homebrew version and installed packages |

## 4. My understanding
The Terminal lets me control the computer by typing commands instead of clicking. Commands follow the pattern
`command -flags arguments`. Flags change *how* a command behaves (e.g. `-l`, `-a`, `-h`), and arguments tell it *what*
to work on (e.g. a file name). Redirection (`>` and `>>`) sends output into a file, and pipes (`|`) connect commands
together. I learned to always check where I am with `pwd` and what is there with `ls` before changing files, and to
work only inside my practice folder.

## 5. Difficulties faced
- `cat notes.txt` printed nothing and at first I thought the command had failed.
- The `ls -l` output showed my computer username in the owner column, which is private information.

## 6. How I resolved them
- I realised the file was created with `touch`, so it was empty — `cat` had nothing to print. In Task 2.2 I wrote text
  into a file first and `cat` then displayed it.
- I replaced the username with `[redacted]` in the saved evidence and shortened the full path.

## 7. Evidence / files
- `practice-folder/notes.txt`, `practice-folder/renamed-copy.txt` — Task 2.1 practice files.
- `terminal-practice/clue.txt`, `terminal-practice/clue-backup-renamed.txt` — Task 2.2 files.
- `../evidence/mission-02-terminal-output.txt` — redacted Terminal output for all tasks.

## 8. Commit details
- Commit message: **`Complete Terminal and file management mission`**
- Pushed to GitHub and verified that the commit is visible.
