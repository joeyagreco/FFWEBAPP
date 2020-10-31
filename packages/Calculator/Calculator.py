class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        sum = float(a) + float(b)
        if(sum.is_integer()):
            sum = int(sum)
        return sum        
