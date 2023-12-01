from pathlib import Path


def part1(calibration_document: str) -> int:
    lines = calibration_document.splitlines()
    calibration_value_sum = 0
    for line in lines:
        digits = list(filter(str.isdigit, line))
        calibration_value = int(digits[0] + digits[-1])
        calibration_value_sum += calibration_value
    return calibration_value_sum


def replace_spelled_out_digits(line: str) -> str:
    digit_replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    while any(digit in line for digit in digit_replacements):
        digit = min(
            (digit for digit in digit_replacements if digit in line),
            key=lambda digit: line.index(digit),
        )
        line = line.replace(digit, digit_replacements[digit], 1)
    return line


def part2(calibration_document: str) -> int:
    lines = calibration_document.splitlines()
    calibration_value_sum = 0
    for line in lines:
        new_line = replace_spelled_out_digits(line)
        digits = list(filter(str.isdigit, new_line))
        calibration_value = int(digits[0] + digits[-1])
        calibration_value_sum += calibration_value
    return calibration_value_sum


if __name__ == "__main__":
    calibration_document = (Path("inputs") / "day01.txt").read_text()
    print(part1(calibration_document))
    print(part2(calibration_document))
