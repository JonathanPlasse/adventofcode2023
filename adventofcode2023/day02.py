from dataclasses import dataclass
from pathlib import Path


@dataclass
class GameSet:
    red: int
    green: int
    blue: int

    @classmethod
    def parse(cls, game_set: str) -> "GameSet":
        cubes = game_set.split(",")
        red = green = blue = 0
        for cube in cubes:
            count, color = cube.split()
            if color == "red":
                red = int(count)
            elif color == "green":
                green = int(count)
            elif color == "blue":
                blue = int(count)
        return GameSet(red, green, blue)


@dataclass
class Game:
    id_: int
    sets: list[GameSet]

    @classmethod
    def parse(cls, game: str) -> "Game":
        game_id_str, sets_str = game.split(":")
        game_id = int(game_id_str.split()[1])
        sets = [GameSet.parse(game_set) for game_set in sets_str.split(";")]
        return Game(game_id, sets)


@dataclass
class GameRecord:
    games: list[Game]

    @classmethod
    def parse(cls, game_record: str) -> "GameRecord":
        games = [Game.parse(game) for game in game_record.splitlines()]
        return GameRecord(games)


def part1(content: str) -> int:
    game_record = GameRecord.parse(content)
    nb_red_cubes = 12
    nb_green_cubes = 13
    nb_blue_cubes = 14
    possible_game_ids = (
        game.id_
        for game in game_record.games
        if all(
            game_set.red <= nb_red_cubes
            and game_set.green <= nb_green_cubes
            and game_set.blue <= nb_blue_cubes
            for game_set in game.sets
        )
    )
    return sum(possible_game_ids)


def part2(content: str) -> int:
    game_record = GameRecord.parse(content)
    min_game_sets = (
        GameSet(
            red=max(game_set.red for game_set in game.sets),
            green=max(game_set.green for game_set in game.sets),
            blue=max(game_set.blue for game_set in game.sets),
        )
        for game in game_record.games
    )
    min_game_set_powers = (
        game_set.red * game_set.green * game_set.blue for game_set in min_game_sets
    )
    return sum(min_game_set_powers)


if __name__ == "__main__":
    game_record = (Path("inputs") / "day02.txt").read_text()
    print(part1(game_record))
    print(part2(game_record))
