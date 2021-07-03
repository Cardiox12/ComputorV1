from core.expression import Expression

class Equation:
	def __init__(self, expression):
		self.expression = Expression(expression)
		self.left, self.right = self.expression.split()
		decompo = self.left.decompose()
		invert = self.left.invert()

		print("=" * 50)
		print(self.left)
		print(decompo)
		print(invert)

	def sqrt(self, x):
		return x

	def simplify(self):
		pass

	def show(self):
		pass
