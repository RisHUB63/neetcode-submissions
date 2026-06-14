class Solution:
    def box_id(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                digit = int(value)
                mask = 1 << digit
                box = self.box_id(row, col)

                if (
                    rows[row] & mask
                    or cols[col] & mask
                    or boxes[box] & mask
                ):
                    return False

                rows[row] |= mask
                cols[col] |= mask
                boxes[box] |= mask

        return True