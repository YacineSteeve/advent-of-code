import re
from typing import Dict, Tuple, Union


def replace_digit_literals(text_line: str) -> str:
    new_text_line: str = text_line
    digits_literals: Dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    pattern = r"one|two|three|four|five|six|seven|eight|nine"
    cleaned = False

    while not cleaned:
        literal_match = re.search(pattern, new_text_line)

        if literal_match is not None:
            new_text_line = \
                new_text_line[:literal_match.start()] \
                + digits_literals[literal_match.group()] \
                + new_text_line[literal_match.end():]

        cleaned = literal_match is None

    return new_text_line


def get_first_digit(
        text_line: str,
        start_index: int = 0,
        stop_index: int = None
) -> Tuple[Union[int, None], Union[int, None]]:
    i: int = start_index
    stop_index = [len(text_line) - 1, stop_index][stop_index is not None]

    while i <= stop_index:
        if text_line[i].isdigit():
            return int(text_line[i]), i
        i += 1

    return None, None


def get_last_digit(
        text_line: str,
        start_index: int = None,
        stop_index: int = 0
) -> Tuple[Union[int, None], Union[int, None]]:
    i: int = [len(text_line) - 1, start_index][start_index is not None]

    while i >= stop_index:
        if text_line[i].isdigit():
            return int(text_line[i]), i
        i -= 1

    return None, None


def get_calibration_values(text_line: str) -> int:
    text_line_nums_only = replace_digit_literals(text_line)

    first_digit, first_digit_index = get_first_digit(text_line_nums_only)
    last_digit, _ = get_last_digit(text_line_nums_only, stop_index=first_digit_index+1)

    return int(f"{first_digit}{last_digit if last_digit is not None else ''}")


with open("input.txt", "r") as file:
    print(sum(get_calibration_values(line) for line in file.readlines()))
