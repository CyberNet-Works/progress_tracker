def largest_swap(num):
    flipped_number = int("".join([char for char in str(num)][::-1]))

    return flipped_number if flipped_number > num else num
