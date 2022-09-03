def update_board(board):
    WRAPPING = False

    new_board = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    neighbours = ((-1, -1),
                  (-1, 0),
                  (-1, 1),
                  (0, -1),
                  (0, 1),
                  (1, -1),
                  (1, 0),
                  (1, 1))

    for x, column in enumerate(board):
        for y, cell in enumerate(column):
            n_count = 0
            for n in neighbours:
                pos = [x + n[0], y + n[1]]
                if pos[0] < 0 or pos[1] < 0 or pos[1] >= len(board[0]) or pos[0] >= len(board):
                    if not WRAPPING:
                        continue
                    else:
                        if pos[0] >= len(board): pos[0] -= len(board)
                        if pos[1] >= len(board[0]): pos[1] -= len(board[0])
                if board[pos[0]][pos[1]]:
                    n_count += 1

            # Rules
            if not cell:
                if n_count == 3:
                    new_board[x][y] = True
            else:
                if n_count == 2 or n_count == 3:
                    new_board[x][y] = True

    return new_board
