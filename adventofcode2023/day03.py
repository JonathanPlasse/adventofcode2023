from dataclasses import dataclass
from pathlib import Path


@dataclass
class NumberPosition:
    value: int
    line_index: int
    start_index: int
    end_index: int


@dataclass
class OperatorPosition:
    operator: str
    line_index: int
    row_index: int


def parse(content: str) -> tuple[list[NumberPosition], list[OperatorPosition]]:
    lines = content.splitlines()
    numbers: list[NumberPosition] = []
    operators: list[OperatorPosition] = []
    for line_index, line in enumerate(lines):
        number = ""
        start_index = 0
        for char_index, char in enumerate(line):
            if char.isdigit():
                if number == "":
                    start_index = char_index
                number += char
            elif char != ".":
                operators.append(OperatorPosition(char, line_index, char_index))

            if number != "" and (not char.isdigit() or char_index == len(line) - 1):
                numbers.append(
                    NumberPosition(
                        int(number),
                        line_index,
                        start_index,
                        start_index + len(number),
                    ),
                )
                number = ""
    return numbers, operators


def is_number_near_operator(number: NumberPosition, operator: OperatorPosition) -> bool:
    return (
        operator.line_index == number.line_index
        and (operator.row_index in (number.start_index - 1, number.end_index))
    ) or (
        operator.line_index in (number.line_index - 1, number.line_index + 1)
        and (number.start_index - 1 <= operator.row_index <= number.end_index)
    )


def part1(content: str) -> int:
    numbers, operators = parse(content)

    total = 0
    for number in numbers:
        for operator in operators:
            if is_number_near_operator(number, operator):
                total += number.value
                break
    return total


def part2(content: str) -> int:
    numbers, operators = parse(content)

    total = 0
    for operator in operators:
        if operator.operator != "*":
            continue
        first_number = None
        for number in numbers:
            if is_number_near_operator(number, operator):
                if first_number is None:
                    first_number = number.value
                else:
                    total += first_number * number.value
                    break

    return total


if __name__ == "__main__":
    content = (Path("inputs") / "day03.txt").read_text()
    print(part1(content))
    print(part2(content))
