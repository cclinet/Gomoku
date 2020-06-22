from typing import Tuple, List

import numpy as np


class Game:
    def __init__(self):
        self.board = np.zeros(shape=(15, 15), dtype=np.int8)

    def game_result(self) -> Tuple[int, List[Tuple[int, int]]]:
        # 横向
        for x in range(11):
            for y in range(15):
                if (
                    self.board[x, y] == 1
                    and self.board[x + 1, y] == 1
                    and self.board[x + 2, y] == 1
                    and self.board[x + 3, y] == 1
                    and self.board[x + 4, y] == 1
                ):
                    return 1, [(x0, y) for x0 in range(x, x + 5)]
                elif (
                    self.board[x, y] == 2
                    and self.board[x + 1, y] == 2
                    and self.board[x + 2, y] == 2
                    and self.board[x + 3, y] == 2
                    and self.board[x + 4, y] == 2
                ):
                    return 2, [(x0, y) for x0 in range(x, x + 5)]
        # 纵向
        for x in range(15):
            for y in range(11):
                if (
                    self.board[x, y] == 1
                    and self.board[x, y + 1] == 1
                    and self.board[x, y + 2] == 1
                    and self.board[x, y + 3] == 1
                    and self.board[x, y + 4] == 1
                ):
                    return 1, [(x, y0) for y0 in range(y, y + 5)]
                elif (
                    self.board[x, y] == 2
                    and self.board[x, y + 1] == 2
                    and self.board[x, y + 2] == 2
                    and self.board[x, y + 3] == 2
                    and self.board[x, y + 4] == 2
                ):
                    return 2, [(x, y0) for y0 in range(y, y + 5)]
        # 左上到右下
        for x in range(1):
            for y in range(11):
                if (
                    self.board[x, y] == 1
                    and self.board[x + 1, y + 1] == 1
                    and self.board[x + 2, y + 2] == 1
                    and self.board[x + 3, y + 3] == 1
                    and self.board[x + 4, y + 4] == 1
                ):
                    return 1, [(x, y0) for y0 in range(y, y + 5)]
                elif (
                    self.board[x, y] == 2
                    and self.board[x + 1, y + 1] == 2
                    and self.board[x + 2, y + 2] == 2
                    and self.board[x + 3, y + 3] == 2
                    and self.board[x + 4, y + 4] == 2
                ):
                    return 2, [(x + t, y + t) for t in range(5)]
        # 右上到左下
        for x in range(4, 15):
            for y in range(11):
                if (
                    self.board[x, y] == 1
                    and self.board[x - 1, y + 1] == 1
                    and self.board[x - 2, y + 2] == 1
                    and self.board[x - 3, y + 3] == 1
                    and self.board[x - 4, y + 4] == 1
                ):
                    return 1, [(x, y0) for y0 in range(y, y + 5)]
                elif (
                    self.board[x, y] == 2
                    and self.board[x - 1, y + 1] == 2
                    and self.board[x - 2, y + 2] == 2
                    and self.board[x - 3, y + 3] == 2
                    and self.board[x - 4, y + 4] == 2
                ):
                    return 2, [(x - t, y + t) for t in range(5)]
        # 平局
        for x in range(15):
            for y in range(15):
                if self.board[x, y] == 0:
                    return 0, [(-1, -1)]
        return 3, [(-1, -1)]
