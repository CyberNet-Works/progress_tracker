#check_if_n_is_both_square_root_and_cube_root
def is_cubic_square(n):
    if n < 0:
        return False
    
    square_root = False

    for x in range(n + 1):
        if x * x == n:
            square_root = True
    
    cube_root = False

    for y in range(n + 1):
        if y * y * y == n:
            cube_root = True

    return cube_root == square_root == True