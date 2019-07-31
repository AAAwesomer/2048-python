import copy


def pos_score(board):
    mat = copy.deepcopy(board)
    for i in range(len(mat)):
        if i % 2 == 1:
            mat[i].reverse()
    mat = [item for sublist in mat for item in sublist]
    mat = [mat[i] / 2 ** i for i in range(len(mat))]
    return sum(mat)


def free_tiles(board):
    mat = copy.deepcopy(board)
    flat = [item for sublist in mat for item in sublist]
    free_indices = [i for i, x in enumerate(flat) if x == 0]
    free_coords = [(i // 4, i % 4) for i in free_indices]
    return free_coords
