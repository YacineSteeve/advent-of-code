def get_first_digit(text_line: str) -> int:
    i: int = 0
    while i < len(text_line):
        if text_line[i].isdigit():
            return int(text_line[i])
        i += 1


def get_last_digit(text_line: str) -> int:
    i: int = len(text_line) - 1
    while i >= 0:
        if text_line[i].isdigit():
            return int(text_line[i])
        i -= 1


def get_calibration_values(text_line: str) -> int:
    return int(f"{get_first_digit(text_line)}{get_last_digit(text_line)}")


with open("input.txt", "r") as file:
    print(sum(get_calibration_values(line) for line in file.readlines()))
