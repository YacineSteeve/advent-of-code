from typing import Dict, Tuple


def get_first_digit(
        text_line: str,
        literals: Dict[str, int],
        stop_index: int
) -> Tuple[int, int]:
    i: int = 0
    t_first_digit = (None, len(text_line))
    while i <= stop_index:
        if text_line[i].isdigit():
            t_first_digit = (int(text_line[i]), i)
            break
        i += 1

    t_first_literal = sorted(
        list(
            map(
                lambda literal: (
                    literal,
                    text_line.index(literal, 0, stop_index) if literal in text_line[:stop_index] else len(text_line)
                ),
                literals.keys()
            )
        ),
        key=lambda l: l[1]
    )[0]

    if t_first_literal[1] < t_first_digit[1]:
        return literals[t_first_literal[0]], t_first_literal[1] + len(t_first_literal[0])
    else:
        return t_first_digit[0], t_first_digit[1] + 1


def get_calibration_values(text_line: str) -> int:
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

    reversed_digits_literals: Dict[str, int] = {
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9
    }

    n = len(text_line)
    first_digit, first_digit_index = get_first_digit(text_line, digits_literals, n - 1)
    last_digit, _ = get_first_digit(text_line[::-1], reversed_digits_literals,n - first_digit_index - 1)

    return int(f"{first_digit}{last_digit if last_digit is not None else ''}")


with open("input.txt", "r") as file:
    print(sum(get_calibration_values(line) for line in file.readlines()))
