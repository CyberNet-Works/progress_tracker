#simple_interest.py
def simple_interest(principal, rate, time):
    interest = principal * rate * time / 100

    return interest, principal + interest