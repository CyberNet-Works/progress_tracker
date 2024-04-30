#return true if binary sequence represented by one bit
def is_last_character_one_bit(bits_list):
    if len(bits_list) > 1:
        return (bits_list[-1] == 0 and bits_list[-2] == 0)
    else:
        return bits_list[-1] == 0