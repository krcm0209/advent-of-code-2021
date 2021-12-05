import numpy as np
import re
from typing import List, Union


class Board:
    def __init__(self, rows: List[List[int]]):
        self.elements = np.array(rows)
        self.win_mask = np.full_like(self.elements, False, bool)

    def check_num(self, num: int) -> Union[None, int]:
        self.win_mask += self.elements == num
        for element in np.all(self.win_mask, axis=0):
            if not element:
                continue
            # found column win
            return self.score(num)
        for element in np.all(self.win_mask, axis=1):
            if not element:
                continue
            # found row win
            return self.score(num)

    def score(self, num: int) -> int:
        else_arr = np.ma.masked_array(self.elements, self.win_mask)
        else_sum = np.sum(else_arr)
        return else_sum * num


def chronological_winning_board_scores(numbers: List[int], boards: List[Board]) -> List[Board]:
    winning_board_scores = []

    for number in numbers:
        boards_to_remove = []
        for board in boards:
            result = board.check_num(number)
            if result:
                winning_board_scores.append(result)
                boards_to_remove.append(board)
        for board in boards_to_remove:
            boards.remove(board)

    return winning_board_scores


def main():
    boards = []

    # load input
    with open("input", "r") as file:
        numbers = [int(num) for num in file.readline()[:-1].split(",")]
        file.readline() # throw away empty line

        rows = []
        for line in [line[:-1] for line in file]:
            if line == "":
                boards.append(Board(rows))
                rows = []
            else:
                rows.append([int(e) for e in re.split(r"\s+", line.strip())])
        boards.append(Board(rows))
    
    winning_board_scores = chronological_winning_board_scores(numbers, boards)

    # part 1
    print(f"First winning board score: {winning_board_scores[0]}")
    # part 2
    print(f"Last winning board score: {winning_board_scores[-1]}")


if __name__ == "__main__":
    main()
