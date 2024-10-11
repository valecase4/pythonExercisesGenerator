matrix = [
    [10, 3, 5],
    [3, 4, 1],
    [4, 4, 2]
]

max_column_sum = 0
index_best_column = None

for r in range(len(matrix[0])):
    column_sum = 0
    for c in range(len(matrix)):
        column_sum += matrix[c][r]

    if column_sum > max_column_sum:
        max_column_sum = column_sum
        index_best_column = r
    
print(f"The column with the greatest sum of its elements  is the column {index_best_column} ({max_column_sum})")
