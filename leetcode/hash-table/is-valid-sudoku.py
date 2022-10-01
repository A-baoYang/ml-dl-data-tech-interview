class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        len_row, len_col = len(board), len(board[0])
        row = [set() for _ in range(len_row)]
        col = [set() for _ in range(len_col)]
        loca = [set() for _ in range(len_row)]

        for i in range(len_row):
            for j in range(len_col):
                row_ind, col_ind = i // 3, j // 3
                loca_ind = row_ind * 3 + col_ind
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in loca[loca_ind]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    loca[loca_ind].add(board[i][j])
        return True
