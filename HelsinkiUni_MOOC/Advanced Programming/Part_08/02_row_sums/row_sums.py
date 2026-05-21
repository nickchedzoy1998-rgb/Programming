def row_sums(my_matrix: list):
    for i, row in enumerate(my_matrix):
        total = sum(row)

        my_matrix[i].append(total)