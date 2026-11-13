from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    rows = row_end - row_start + 1
    columns = column_end - column_start + 1
    arr = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            arr[i][j] = (row_start + i) * (column_start + j)
    return arr

