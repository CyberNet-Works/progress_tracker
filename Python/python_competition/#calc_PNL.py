#calc_PNL.py
def calculate_profit_loss(cost_price, selling_price):
    pnl = selling_price - cost_price

    if pnl > 0:
        return f"Profit: {pnl}"
    else:
        return f"Loss: {pnl * -1}"