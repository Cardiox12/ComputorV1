from core.expression import Expression

class Equation:
    def __init__(self, expression):
        self.expression = Expression(expression)
        self.left, self.right = self.expression.split()
        self.left.decompose()

    def sqrt(self, x):
        return x

    def simplify(self):
        pass

    def show(self):
        pass