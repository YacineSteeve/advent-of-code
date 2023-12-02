import re
from typing import Dict, Tuple


def get_color_num(color: str, text: str) -> int:
    color_pattern = r"(\d+) " + color
    color_num = re.search(color_pattern, text)

    if color_num is not None:
        return int(color_num.group(1))

    return 0


def format_games(game_string) -> Tuple:
    game, subsets = game_string.split(":")
    subsets = list(map(lambda s: s.strip(), subsets.split(";")))

    cubes_min_nums: Dict = {"red": 0, "green": 0, "blue": 0}

    for subset in subsets:
        cubes_min_nums["red"] = max(cubes_min_nums.get("red"), get_color_num("red", subset))
        cubes_min_nums["green"] = max(cubes_min_nums.get("green"), get_color_num("green", subset))
        cubes_min_nums["blue"] = max(cubes_min_nums.get("blue"), get_color_num("blue", subset))

    return int(game.strip().split()[1]), cubes_min_nums


def is_valid_game(game_colors) -> bool:
    return game_colors["red"] <= 12 and game_colors["blue"] <= 14 and game_colors["green"] <= 13


def game_power(game_colors) -> int:
    return game_colors["red"] * game_colors["blue"] * game_colors["green"]


with open("input.txt", "r") as file:
    valid_games_ids = []
    games_powers = []

    for line in file.readlines():
        game_id, game_colors_min = format_games(line)
        if is_valid_game(game_colors_min):
            valid_games_ids.append(game_id)
        games_powers.append(game_power(game_colors_min))

    print(sum(valid_games_ids))
    print(sum(games_powers))
