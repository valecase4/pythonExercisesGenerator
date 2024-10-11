input = [
    [3, 4, 10, 7],
    [5, 4, 1, 3],
    [6, 2, 3, 1]
]

def transpose_matrix(input_matrix):
    transposed = []

    for i in range(len(input_matrix[0])):
        row = []
        for j in range(len(input_matrix)):
            row.append(input_matrix[j][i])
        transposed.append(row)

    return transposed

output = transpose_matrix(input)
print(output)


