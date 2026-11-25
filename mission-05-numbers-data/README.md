# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers between decimal, binary and hexadecimal by hand, check the answers with Python, build a small number
converter program, and explain how text is stored using encodings.

## 2. Work completed
- Did all seven conversions by hand with full working (Task 5.1).
- Checked every answer in the Python interactive environment (Task 5.2) — all matched.
- Wrote [`number_converter.py`](number_converter.py) and tested it with four numbers plus one invalid input (Task 5.3).
- Found ASCII codes and explained text encoding (Task 5.4).

### Task 5.1 — Convert numbers by hand

| Question | My working and answer |
|----------|-----------------------|
| Decimal 13 → binary | 13 ÷ 2 = 6 r **1**; 6 ÷ 2 = 3 r **0**; 3 ÷ 2 = 1 r **1**; 1 ÷ 2 = 0 r **1**. Read remainders bottom → top: **1101** |
| Decimal 25 → binary | 25 ÷ 2 = 12 r **1**; 12 ÷ 2 = 6 r **0**; 6 ÷ 2 = 3 r **0**; 3 ÷ 2 = 1 r **1**; 1 ÷ 2 = 0 r **1**. Bottom → top: **11001** |
| Binary 1010 → decimal | Place values 8 4 2 1 → (1×8) + (0×4) + (1×2) + (0×1) = 8 + 2 = **10** |
| Binary 1101 → decimal | (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 1 = **13** |
| Hex A → decimal | In hex, A stands for ten, so A = 10 × 16⁰ = **10** |
| Hex 1F → decimal | (1 × 16¹) + (F × 16⁰) = (1 × 16) + (15 × 1) = 16 + 15 = **31** |
| Binary 1111 → hex | 1111 = 8 + 4 + 2 + 1 = 15 in decimal, and 15 is **F** in hex. (One group of 4 bits = one hex digit.) |

**Check:** decimal 13 → binary 1101, and binary 1101 → decimal 13, so the conversions agree in both directions.

### Task 5.2 — Verify using Python
I opened the interactive environment with `python3` and typed each expression:

| Expression tested | Result | Matches my working? |
|-------------------|--------|---------------------|
| `bin(13)` | `'0b1101'` | ✅ Yes |
| `bin(25)` | `'0b11001'` | ✅ Yes |
| `int("1010", 2)` | `10` | ✅ Yes |
| `int("1101", 2)` | `13` | ✅ Yes |
| `int("A", 16)` | `10` | ✅ Yes |
| `int("1F", 16)` | `31` | ✅ Yes |
| `hex(int("1111", 2))` | `'0xf'` | ✅ Yes |
| `hex(31)` (decimal → hex) | `'0x1f'` | ✅ Yes (reverse of the 1F question) |

`0b` at the start means "this is binary" and `0x` means "this is hexadecimal".

### Task 5.3 — Number converter
**How it works:**
1. `input()` asks the user to type a number. Whatever is typed comes back as text (a string).
2. `int()` turns that text into a whole number. If the text is not a number (e.g. `abc`), `int()` raises a
   `ValueError`, which my program catches and prints a friendly message instead of crashing.
3. `bin(number)` returns the number written in **binary** as text starting with `0b`.
4. `hex(number)` returns the number written in **hexadecimal** as text starting with `0x`.
5. `print()` shows both results, with and without the prefix.

**Run it:**
```bash
cd mission-05-numbers-data
python3 number_converter.py
```

**Test results:**

| Test number | Binary output | Hexadecimal output |
|-------------|---------------|--------------------|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 255 | `0b11111111` | `0xff` |
| 2026 | `0b11111101010` | `0x7ea` |
| `abc` (invalid) | — | Program printed: "That is not a whole number…" |

255 is a useful test because it is the biggest number that fits in one byte (eight 1s in binary, `FF` in hex).

### Task 5.4 — How is text stored?
- **ASCII codes:** uppercase **A = 65**, lowercase **a = 97** (checked with `ord("A")` and `ord("a")`). The difference
  is 32, which is the same for every letter.
- **Why an encoding is needed:** a computer can only store numbers (bits), not letters. An encoding standard is an
  agreed table that says which number stands for which character, so a file saved on one computer shows the same
  text when opened on another.
- **A character not in basic ASCII:** the Indian Rupee sign **₹**. ASCII only has 128 characters (codes 0–127). In
  UTF-8, `"₹".encode("utf-8")` gives 3 bytes: `e2 82 b9`. Another example is `é`, which takes 2 bytes (`c3 a9`).

## 3. Commands / tools used
| Command / function | Purpose |
|--------------------|---------|
| `python3` | Open the Python interactive environment |
| `bin()` | Decimal → binary text |
| `hex()` | Decimal → hexadecimal text |
| `int(text, base)` | Binary/hex text → decimal (`base` 2 or 16) |
| `input()`, `int()`, `print()` | Read user input, convert it to a number, show results |
| `ord()` | Get the character code of a letter |
| `str.encode("utf-8")` | See the bytes UTF-8 uses for a character |
| `python3 number_converter.py` | Run the converter program |

## 4. My understanding
Everything inside a computer is stored as bits (0 or 1), and 8 bits make a byte. Binary is base 2 (place values 1, 2,
4, 8 …), decimal is base 10, and hexadecimal is base 16 (place values 1, 16, 256 …, digits 0–9 and A–F). Hex is popular
because one hex digit is exactly 4 bits, so it is a short way to write binary. Text is also stored as numbers: an
encoding like ASCII or UTF-8 maps every character to a number. ASCII covers basic English, while UTF-8 can store
characters from every language (and emojis) by using 1 to 4 bytes per character.

## 5. Difficulties faced
- Python's `hex()` gave lowercase letters (`0x1f`) while my hand working used uppercase (`1F`), and I wondered if one was wrong.
- The first version of the converter crashed with a `ValueError` when I typed letters instead of a number.

## 6. How I resolved them
- Learned that hex letters are not case-sensitive (`1f` = `1F`). My program also prints the uppercase version.
- Wrapped `int()` in `try` / `except ValueError` so the program shows a friendly message instead of crashing.

## 7. Evidence / files
- `number_converter.py` — the working converter.
- `../evidence/mission-05-converter-output.txt` — output of the converter for every test.
- `../evidence/mission-05-python-verification.txt` — the Python verification expressions and results.

## 8. Commit details
- Commit message: **`Build number converter and practise data representation`**
- Pushed to GitHub and verified that the commit is visible.
