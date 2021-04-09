import numpy as np
""" 
&& - должны выполняться обо услови (*)
|| - должно выполняться любое условие (+)
"""
matrix = np.zeros((5, 5))
S = 0.5
Cf = 9.3


def update_matrix(matrix: np.ndarray, S: float, Cf: float, unit: str) -> np.ndarray:
    row = col = len(matrix)
    if unit == '1X&&yes':
        """(1X&&yes) - элементы, для которых (номер строки>=номер столбца)&&(номер строки > 0)&&
            (номер столбца > 0) уменьшаются на S*Cf. Остальные увеличиваются на S."""
        for row in range(row):
            for col in range(col):
                if (row and col > 0) and row >= col:
                    matrix[row][col] -= S * Cf
                else:
                    matrix[row][col] += S
    elif unit == '1X&&no':
        """(1X&&no) - элементы, для которых (номер строки<номер столбца)||(номер строки==0)||
            (номер столбца == 0) уменьшаются на S*Cf. Остальные увеличиваются на S."""
        for row in range(row):
            for col in range(col):
                if row or col == 0 or row < col:
                    matrix[row][col] -= S * Cf
                else:
                    matrix[row][col] += S
    elif unit == '12&&yes':
        """(12&&yes) - элементы, для которых (номер строки!=номер столбца)&&(номер строки > 0)&&
            (номер столбца > 0) уменьшаются на S*Cf. Остальные увеличиваются на S."""
        for row in range(row):
            for col in range(col):
                if row and col > 0 and row != col:
                    matrix[row][col] -= S * Cf
                else:
                    matrix[row][col] += S
    elif unit == '12&&no':
        """(12&&no) - элементы, для которых (номер строки==номер столбца)||(номер строки ==0) ||
            (номер столбца == 0) уменьшаются на S*Cf. Остальные увеличиваются на S."""
        for row in range(row):
            for col in range(col):
                if row or col == 0 or row == col:
                    matrix[row][col] -= S * Cf
                else:
                    matrix[row][col] += S
    elif unit == '2X&&yes':
        """(2X&&yes) - элементы, для которых (номер строки<=номер столбца)&&(номер строки > 0)&&
            (номер столбца > 0) уменьшаются на S*Cf. Остальные увеличиваются на S."""
        for row in range(row):
            for col in range(col):
                if row and col > 0 and row <= col:
                    matrix[row][col] -= S * Cf
                else:
                    matrix[row][col] += S
    elif unit == '2X&&no':
        """(2X&&no) - элементы, для которых (номер строки>номер столбца)||(номер строки == 0) ||
            (номер столбца == 0) уменьшаются на S*Cf. Остальные увеличиваются на S."""
        for row in range(row):
            for col in range(col):
                if row or col == 0 or row > col:
                    matrix[row][col] -= S * Cf
                else:
                    matrix[row][col] += S
    return matrix


print(update_matrix(matrix, S, Cf, '1X&&yes'))
print(update_matrix(matrix, S, Cf, '1X&&no'))
print(update_matrix(matrix, S, Cf, '12&&yes'))
print(update_matrix(matrix, S, Cf, '12&&no'))
print(update_matrix(matrix, S, Cf, '2X&&yes'))
print(update_matrix(matrix, S, Cf, '2X&&no'))
