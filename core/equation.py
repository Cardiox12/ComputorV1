from core.expression import Expression
from pprint import pprint

class Equation:
	def __init__(self, expression):
		self.expression = Expression(expression)
		self.left, self.right = self.expression.split()

		print(self.expression)
		self.left.decompose()
		if self.right is not None:
			self.right.decompose()
			self.right.invert()
			self.left.pass_to_left(self.right)

		self.degree = max(self.left.decomposition.keys())
		self.solve()
		print("=" * 50)

	@staticmethod
	def has_solutions(self, decomposition):
		pass

	def solve(self):
		if any([not float(n).is_integer() for n in self.left.decomposition.keys()]):
			print("Cannot solve, degree float")
		if self.degree > 2:
			print(f"Cannot solve this equation with degree {self.degree}, degree too high")
		if any([degree < 0 for degree in self.left.decomposition.keys()]):
			print(f"Cannot solve this equation, degree too low")
		elif self.degree == 1:
			a = self.left.decomposition.get(1, 0)
			b = self.left.decomposition.get(0, 0)

			x = -b / a
			print(f"{self.expression} a pour solution x = {x}")
			print(self.format())
		elif self.degree == 2 and len(self.left.decomposition.keys()) == 1:
			factor = float(self.left.expression.split("X")[0])
			x = Equation.sqrt(factor)
			print(f"{self.expression} admet une solution x = {x}")
			print(self.format())
		elif self.degree == 2:
			# Calculer discriminant
			a = self.left.decomposition.get(2, 0)
			b = self.left.decomposition.get(1, 0)
			c = self.left.decomposition.get(0, 0)

			delta = (b ** 2) - (4 * a * c)

			if delta > 0:
				# Two real solutions
				x1 = (-b - Equation.sqrt(delta)) / (2 * a)
				x2 = (-b + Equation.sqrt(delta)) / (2 * a)
				print(f"{self.expression} admet deux solutions\n\tx1 : {x1}\n\tx2 : {x2}")
				print(self.format())
			elif delta < 0:
				print("WIP Equation complexe")
				# Two imaginary solutions
				# x1 = complex(-b / (2 * a), Equation.sqrt(delta) / (2 * a))
				# x2 = complex(-b, - Equation.sqrt(delta))
				# print(f"{self.expression} admet deux solutions imaginaires\n\tx1 : {x1}\n\tx2 : {x2}")
				# print(self.format())
				pass
			else:
				# One solution
				x = (-b) / (2 * a)
				print(f"{self.expression} admet une solution\n\tx : {x}")
				print(self.format())
	
	def format(self):
		equation = ""
		for index, key in enumerate(self.left.decomposition):
			value = self.left.decomposition[key]
			value = value if not value.is_integer() else int(value)

			if index == 0:
				if key == 0:
					equation += f"{value}"
				elif key == 1:
					equation += f"{value} * X"
				else:
					equation += f"{value} * X^{key}"
			elif value < 0:
				equation += f" - {str(value).replace('-', '')} * X^{key}"
			elif value >= 0:
				if key == 0:
					equation += f" + {value}"
				elif key == 1:
					equation += f" + {value} * X"
				else:
					equation += f" + {value} * X^{key}"
		return equation

	@staticmethod
	def sqrt(x):
		def _sqrt(x):
			i = 0
			while (i * i < x and i <= 46340):
				i+=1
			if (i * i == x):
				return (i)
			else:
				return (0)

		def _splitTooPerTooInt(x):
			decompo = []
			while x > 0:
				decompo.append(x%100)
				x //= 100
			decompo.reverse()
			return decompo

		def _splitTooPerTooFloat(x):
			decompo = []
			i = 0
			while i < 10:
				decompo.append(int(x*100))
				x *= 100
				x -= int(x)
				i += 1
			return decompo

		div = 0
		result = 0
		partie = 0
		decimal = 10
		if _sqrt(x):
			return _sqrt(x)
		gauche = _splitTooPerTooInt(int(x))
		x -= int(x)
		droite = _splitTooPerTooFloat(x)
		
		while(len(gauche)):
			partie = partie*100+gauche[0]
			i = 0
			while partie > ((div*10)+i+1)*(i+1):  
				i += 1
			partie -= ((div*10)+i)*i
			div = (div*10)+(i*2)
			result = result*10 + i
			del gauche[0]

		while(len(droite)):
			partie = partie*100+droite[0]
			i = 0
			while partie > ((div*10)+i+1)*(i+1):  
				i += 1
			partie -= ((div*10)+i)*i
			div = (div*10)+(i*2)
			result = result + i/(decimal)
			del droite[0]
			decimal *= 10
		return result

	def simplify(self):
		pass

	def show(self):
		pass