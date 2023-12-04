from dataclasses import dataclass
from pathlib import Path


@dataclass
class ScratchCard:
    winning_numbers: set[int]
    numbers: set[int]
    nb_instances: int = 1

    @classmethod
    def parse(cls, content: str) -> "ScratchCard":
        _, card_numbers = content.split(":")
        winning_numbers_str, numbers_str = card_numbers.split("|")
        return cls(
            winning_numbers={int(n) for n in winning_numbers_str.split()},
            numbers={int(n) for n in numbers_str.split()},
        )

    @property
    def nb_matching_numbers(self) -> int:
        return len(self.winning_numbers & self.numbers)


def parse_scratchcards(content: str) -> list[ScratchCard]:
    return [ScratchCard.parse(card_content) for card_content in content.splitlines()]


def part1(content: str) -> int:
    scratchcards = parse_scratchcards(content)
    return sum(
        2 ** (nb_winning_numbers - 1) if (nb_winning_numbers := card.nb_matching_numbers) > 0 else 0
        for card in scratchcards
    )


def part2(content: str) -> int:
    scratchcards = parse_scratchcards(content)
    for card_index, card in enumerate(scratchcards):
        for other_card in scratchcards[card_index + 1 : card_index + 1 + card.nb_matching_numbers]:
            other_card.nb_instances += card.nb_instances
    return sum(card.nb_instances for card in scratchcards)


if __name__ == "__main__":
    content = (Path("inputs") / "day04.txt").read_text()
    print(part1(content))
    print(part2(content))
