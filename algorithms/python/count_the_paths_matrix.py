from typing import List


def _is_at_end(matrix: List[List], row: int, col: int) -> bool:
    if row == len(matrix) - 1 and col == len(matrix[row]) - 1:
        return True
    return False


def count_the_paths(matrix: List[List], row: int, col: int, total: int) -> int:
    if row > len(matrix) - 1 or col > len(matrix[row]) - 1:
        return 0
    elif _is_at_end(matrix, row, col):
        return 1
    else:
        total += (count_the_paths(matrix, row + 1, col, total) +
                  count_the_paths(matrix, row, col + 1, total))
    return total


def count_the_paths_with_memoization(matrix: List[List], row: int,
                                     col: int, paths: List[List]) -> int:
    if row > len(matrix) - 1 or col > len(matrix[row]) - 1:
        return 0
    elif _is_at_end(matrix, row, col):
        return 1
    elif not paths[row][col]:
        paths[row][col] = count_the_paths_with_memoization(matrix, row + 1,
                                                           col, paths) + \
                           count_the_paths_with_memoization(matrix, row,
                                                            col + 1, paths)
    return paths[row][col]
