from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Board:
    board: list[list[int]]


if __name__ == "__main__":

    board: Board = Board.from_dict(
        {"board": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 3, 6, 9, 0, 0, 0], [6, 8, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 3, 5, 4, 0, 0, 0, 9], [4, 0, 0, 0, 9, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 3, 0, 6, 7, 0, 0, 9, 0], [0, 0, 2, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 5, 2]]
         })
    print(board.board[2][0])
