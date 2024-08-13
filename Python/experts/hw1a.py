#write a class that will perform basic arithmatic

class Calculator:
    def __init__(self) -> float:
        pass

    def add(self, *args) -> float:
        return sum(args)
    
    def difference(self, *args) -> float:
        return args[0] - sum(args[1:])
    
    def product(self, *args) -> float:
        result = 1
        result = [i * result for i in args]
        return result

    
    def power(self, *args) -> float:
        result = args[0]
        start_args = args[1:]
        
        for i, x in enumerate(start_args):
            result **= args[i] 
            
        result = [result ** args[i] for i, x in enumerate(start_args)]
        
        return result
            
            
    # def quotient(self, *args) -> float:
#     result = args[0]
#     for i, x in enumerate(args):
            
        
        
        # result = [args[i] * result for i, x in enumerate(args)]
        return result