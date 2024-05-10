#check_tictactoe_game_valid
def is_valid_tictactoe(state):
    Xs = 0
    Os = 0

    for matrix in state:
        for x in matrix:
            if x == "X":
                Xs += 1
            if x == "O":
                Os += 1

    return Xs >= Os and (Xs - Os == 1 or Xs - Os == 0)