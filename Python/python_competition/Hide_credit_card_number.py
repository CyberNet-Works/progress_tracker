#hide all numbers except last 4 digits
def mask_credit_card(card_number): 
    card_number = [char for char in str(card_number)]

    stars = len(card_number) - 4


    return "*" * stars + "".join(card_number)[-4::]
