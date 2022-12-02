from pathlib import Path

turns = Path("./d2_input.txt").read_text()

LOSS = 0
DRAW = 3
WIN = 6

DRAW_MAP = {"A": "X", "B": "Y", "C": "Z"}


def p1() -> int:
    LOSS_MAP = {"A": "Z", "B": "X", "C": "Y"}

    POINTS = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    def play(a, b):
        if DRAW_MAP[a] == b:
            return DRAW
        if LOSS_MAP[a] == b:
            return LOSS
        return WIN

    r = 0
    for turn in turns.split("\n"):
        enemy, me = turn.split(" ")
        r += play(enemy, me) + POINTS[me]

    return r


def p2() -> int:
    LOSS_MAP = {"A": "Z", "B": "X", "C": "Y"}

    WIN_MAP = {"A": "Y", "B": "Z", "C": "X"}

    POINTS = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    WIN_POINTS = {
        "X": LOSS,
        "Y": DRAW,
        "Z": WIN,
    }

    def pick(enemy: str, outcome: str) -> str:
        if outcome == "X":
            return LOSS_MAP[enemy]
        if outcome == "Y":
            return DRAW_MAP[enemy]
        return WIN_MAP[enemy]

    r = 0
    for turn in turns.split("\n"):
        enemy, outcome = turn.split(" ")
        picked = pick(enemy, outcome)
        r += POINTS[picked] + WIN_POINTS[outcome]

    return r


if __name__ == "__main__":
    print("part 1", p1())
    print("part 2", p2())
