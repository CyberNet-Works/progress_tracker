def find_true_equations(equations):
    result = []

    for equation in equations:
        equation = equation.replace('=', '==')
        if eval(equation):
            equation = equation.replace('==', '=')
            result.append(equation)
    
    return result