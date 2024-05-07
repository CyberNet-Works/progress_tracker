#check_subset_for_math_expression

def is_math_expression(s):
    valid_chars = set("+-=*/()1234567890")

    s = set(s)
    return s.issubset(valid_chars)