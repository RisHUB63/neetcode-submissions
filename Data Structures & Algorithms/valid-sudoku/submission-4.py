class Solution:

    def box_id(self, row, col):
        return (row // 3) * 3 + (col // 3)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memory = {"box":{}, "col":{}, "row": {}}

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                
                box_id = self.box_id(row, col)

                if box_id not in memory["box"]:
                    memory["box"][box_id] = set()
                if col not in memory["col"]:
                    memory["col"][col] = set()
                if row not in memory["row"]:
                    memory["row"][row] = set()

                if ((box_id in memory["box"] and board[row][col] in memory["box"][box_id]) 
                or (col in memory["col"] and board[row][col] in memory["col"][col]) 
                or (row in memory["row"] and board[row][col] in memory["row"][row])):
                    return False


                memory["box"][box_id].add(board[row][col])
                memory["col"][col].add(board[row][col])
                memory["row"][row].add(board[row][col])
        
        return True




        