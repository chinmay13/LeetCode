from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(arr):
            check_set = set()
            for num in arr:
                if num != "." and num in check_set:
                    return False
                else:
                    check_set.add(num)
            return True

        for row in board:
            if not check_row(row):
                return False
        for col in zip(*board):
            if not check_row(col):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                arr = [x for row in board[row:row + 3] for x in
                       row[col:col + 3]]
                if not check_row(arr):
                    return False
        return True

