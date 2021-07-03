from core.expression import Expression
from pprint import pprint

class Equation:
    def __init__(self, expression):
        self.expression = Expression(expression)
        self.left, self.right = self.expression.split()

        self.left.decompose()
        if self.right is not None:
            self.right.decompose()
            self.right.invert()
            self.left.pass_to_left(self.right)

        print("=" * 50)
        pprint(self.expression)
        pprint(self.left.decomposition)

    def sqrt(self, x):
        return x

    def simplify(self):
        pass

    def show(self):
        pass
