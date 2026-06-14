class Solution:
    def box_id(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                box = self.box_id(row, col)

                if value in rows[row] or value in cols[col] or value in boxes[box]:
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)

        return True
