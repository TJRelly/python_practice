def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    TL_to_BR = []
    BL_to_TR = []
    
    for i, lst in enumerate(matrix):
        TL_to_BR.append(lst[i])
        BL_to_TR.append(lst[::-1][i])

    return sum(TL_to_BR + BL_to_TR)