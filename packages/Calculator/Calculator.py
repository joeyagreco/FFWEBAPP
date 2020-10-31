class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        add_sum = float(a) + float(b)
        if(add_sum.is_integer()):
            add_sum = int(add_sum)
        return add_sum
