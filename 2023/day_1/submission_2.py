from typing import Dict, Tuple, Union

digits_literals: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

max_digit_literal_length: int = max(len(literal) for literal in digits_literals.keys())


def get_first_digit(
        text_line: str,
        start_index: int = 0,
        stop_index: int = None
) -> Tuple[Union[int, None], Union[int, None]]:
    global digits_literals, max_digit_literal_length

    i: int = start_index
    stop_index = [len(text_line) - 1, stop_index][stop_index is not None]

    literal: str = ""
    while i <= stop_index:
        if text_line[i].isdigit():
            return int(text_line[i]), i
        elif text_line[i].isalpha():
            literal += text_line[i]
            if len(literal) > max_digit_literal_length or not any(map(lambda digit_literal: digit_literal.startswith(literal), digits_literals.keys())):
                literal = literal[1:]
            elif literal in digits_literals.keys():
                return digits_literals[literal], i

        i += 1

    return None, None


def get_last_digit(
        text_line: str,
        start_index: int = None,
        stop_index: int = 0
) -> Tuple[Union[int, None], Union[int, None]]:
    global digits_literals, max_digit_literal_length

    i: int = [len(text_line) - 1, start_index][start_index is not None]

    literal: str = ""
    while i >= stop_index:
        if text_line[i].isdigit():
            return int(text_line[i]), i
        elif text_line[i].isalpha():
            literal = text_line[i] + literal
            if len(literal) > max_digit_literal_length or not any(map(lambda digit_literal: digit_literal.endswith(literal), digits_literals.keys())):
                literal = literal[:-1]
            elif literal in digits_literals.keys():
                return digits_literals[literal], i

        i -= 1

    return None, None


def get_calibration_values(text_line: str) -> int:
    first_digit, first_digit_index = get_first_digit(text_line)
    last_digit, _ = get_last_digit(text_line, stop_index=first_digit_index + 1)
    return int(f"{first_digit}{last_digit if last_digit is not None else ''}")


with open("input.txt", "r") as file:
    print(sum(get_calibration_values(line) for line in file.readlines()))
