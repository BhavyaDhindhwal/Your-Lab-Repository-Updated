import sys
import re
from pathlib import Path

PREDEFINED = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}

for i in range(16):
    PREDEFINED[f"R{i}"] = i

DEST = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111"
}

JUMP = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001", "!M": "1110001",
    "-D": "0001111", "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
    "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101"
}


def clean_lines(source):
    result = []
    for line_number, line in enumerate(source.splitlines(), 1):
        line = line.split("//")[0].strip()
        if line:
            result.append((line_number, line))
    return result


def assemble(source):
    lines = clean_lines(source)
    symbols = PREDEFINED.copy()
    instructions = []

    # PASS 1: Find labels
    rom_address = 0

    for line_number, line in lines:
        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1].strip()

            if not label or not re.fullmatch(r"[A-Za-z_.$:][\w.$:]*", label):
                raise ValueError(f"Line {line_number}: Invalid label")

            if label in symbols:
                print(f"Warning: Line {line_number}: Duplicate label '{label}'")
            else:
                symbols[label] = rom_address
        else:
            instructions.append((line_number, line))
            rom_address += 1

    # PASS 2: Translate instructions
    output = []
    next_variable = 16

    for line_number, line in instructions:
        if line.startswith("@"):
            symbol = line[1:].strip()

            if not symbol:
                raise ValueError(f"Line {line_number}: Empty A-instruction")

            if symbol.isdigit():
                address = int(symbol)
            else:
                if not re.fullmatch(r"[A-Za-z_.$:][\w.$:]*", symbol):
                    raise ValueError(f"Line {line_number}: Invalid symbol '{symbol}'")

                if symbol not in symbols:
                    symbols[symbol] = next_variable
                    next_variable += 1

                address = symbols[symbol]

            if not 0 <= address <= 32767:
                raise ValueError(f"Line {line_number}: Address out of range")

            output.append(format(address, "016b"))

        else:
            if line.count("=") > 1 or line.count(";") > 1:
                raise ValueError(f"Line {line_number}: Invalid C-instruction")

            if ";" in line:
                instruction, jump = line.split(";")
            else:
                instruction, jump = line, ""

            if "=" in instruction:
                dest, comp = instruction.split("=")
            else:
                dest, comp = "", instruction

            dest, comp, jump = dest.strip(), comp.strip(), jump.strip()
            if all(ch in "ADM" for ch in dest):
                dest = "".join(ch for ch in "AMD" if ch in dest)

            if comp not in COMP:
                raise ValueError(f"Line {line_number}: Invalid comp '{comp}'")
            if dest not in DEST:
                raise ValueError(f"Line {line_number}: Invalid dest '{dest}'")
            if jump not in JUMP:
                raise ValueError(f"Line {line_number}: Invalid jump '{jump}'")

            output.append("111" + COMP[comp] + DEST[dest] + JUMP[jump])

    return output, symbols


def main():
    if len(sys.argv) != 2:
        print("Usage: python assembler.py filename.asm")
        return

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        return

    try:
        source = input_path.read_text(encoding="utf-8-sig")
        machine_code, symbols = assemble(source)

        output_path = input_path.with_suffix(".hack")
        output_path.write_text("\n".join(machine_code) + "\n", encoding="utf-8")

        print(f"Assembly successful!")
        print(f"Input: {input_path}")
        print(f"Output: {output_path}")
        print(f"Instructions: {len(machine_code)}")

    except (ValueError, OSError) as error:
        print(f"Assembly Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
