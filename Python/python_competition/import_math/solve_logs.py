import math
def solve_exponential(base, result):
	
    
    for x in range(result // 2): 
        if result == base ** float(x):
            return float(x)
        else:
            None