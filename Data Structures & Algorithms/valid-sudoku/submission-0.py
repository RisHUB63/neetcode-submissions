class Solution:

    def box_id(self, row, col):
        return (row // 3) * 3 + (col // 3)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memory = {"box":{}, "col":{}, "row": {}}

        for row in range(9):
            for col in range(9):
                box_id = self.box_id(row, col)
                check = f"{row},{col}"

                if ((box_id in memory["box"] and board[row][col] in memory["box"][box_id]) 
                or (col in memory["col"] and board[row][col] in memory["col"][col]) 
                or (row in memory["row"] and board[row][col] in memory["row"][row])):
                    return False
                
                if board[row][col] == '.':
                    continue
                
                if box_id not in memory["box"]:
                    memory["box"][box_id] = []
                if col not in memory["col"]:
                    memory["col"][col] = []
                if row not in memory["row"]:
                    memory["row"][row] = []
                

                memory["box"][box_id].append(board[row][col])
                memory["col"][col].append(board[row][col])
                memory["row"][row].append(board[row][col])
        
        return True




        