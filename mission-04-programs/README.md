# Mission 4 — How programs run

## 1. Task / objective
Write and run a simple Python program, then compare how a compiler and an interpreter turn source code into something
the computer can run.

## 2. Work completed
- Created [`hello.py`](hello.py) containing one line: `print("Hello from Python")`.
- Ran it from the Terminal with `python3 hello.py` and confirmed that **`Hello from Python`** was printed.
- Completed the compiler vs interpreter comparison table and explanation.

### Task 4.1 — Create and run a Python program
```
$ python3 hello.py
Hello from Python
```

### Task 4.2 — Compiler vs interpreter

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| When translation / execution happens | The whole program is translated **before** it runs, in a separate build step. | Instructions are read and carried out **while** the program runs, one statement at a time. |
| Typical output | A separate executable file (machine code), e.g. `a.out` or `app.exe`, that can run without the source code. | No separate executable — the result of the program appears directly (like the printed message). |
| One example | C compiled with `gcc` / `clang` (also C++, Rust, Go). | Python with `python3` (also JavaScript in a browser, Ruby). |
| One advantage | The finished program usually runs faster, and many errors are found before running. | Quick to test and change — I can edit and re-run immediately, and use it interactively. |

**Explanation:** A compiler works like translating a whole book before anyone reads it: it converts all of the source
code into machine code first, producing a separate executable file that then runs quickly. An interpreter works like a
live translator: it reads my program and carries out each instruction as it goes, so I see results straight away
without a build step, but it is usually slower. When I ran `python3 hello.py`, there was no executable created — the
Python interpreter read the file and printed the message. In reality, Python also mixes both ideas, because it first
compiles code to *bytecode* (`.pyc`) and then interprets that bytecode.

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| `echo 'print("Hello from Python")' > hello.py` (or a text editor) | Create the Python file |
| `python3 hello.py` | Run the file with the Python 3 interpreter |
| `print()` (Python function) | Display text on the screen |

## 4. My understanding
Computers only understand machine code, so the code I write in a language like Python or C must be translated.
A **compiler** translates everything first and gives an executable; an **interpreter** translates and runs as it goes.
Python is called an interpreted language, which is why I can run `hello.py` immediately with no extra build step.
Choosing one or the other is a trade-off between speed of running (compiled) and speed of developing and testing
(interpreted).

## 5. Difficulties faced
I first typed `python hello.py`, which did not work on my Mac because the command is `python3`.

## 6. How I resolved them
I used `python3 --version` to confirm the correct command name and then ran `python3 hello.py`, which worked.

## 7. Evidence / files
- `hello.py` — the one-line Python program.
- `../evidence/mission-04-hello-output.txt` — the Terminal output of running it.

## 8. Commit details
- Commit message: **`Compare compilers and interpreters`**
- Pushed to GitHub and verified that the commit is visible.
