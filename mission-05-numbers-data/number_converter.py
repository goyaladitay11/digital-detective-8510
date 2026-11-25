"""Digital Detective — Mission 5 number converter.

Asks the user for a decimal (base 10) number and shows it in
binary (base 2) and hexadecimal (base 16).
"""


def convert(number):
    """Return the binary and hexadecimal text for a whole number."""
    binary_text = bin(number)  # e.g. 13 -> '0b1101'
    hex_text = hex(number)     # e.g. 31 -> '0x1f'
    return binary_text, hex_text


def main():
    user_text = input("Enter a decimal number: ")
    try:
        number = int(user_text)
    except ValueError:
        print("That is not a whole number. Please enter digits like 13 or 255.")
        return

    binary_text, hex_text = convert(number)
    print(f"Decimal:     {number}")
    print(f"Binary:      {binary_text}  (without prefix: {binary_text.replace('0b', '')})")
    print(f"Hexadecimal: {hex_text}  (without prefix: {hex_text.replace('0x', '').upper()})")


if __name__ == "__main__":
    main()
