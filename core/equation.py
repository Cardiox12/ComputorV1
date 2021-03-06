from core.expression import Expression
from pprint import pprint

class Equation:
	def __init__(self, expression):
		self.expression = Expression(expression)
		self.left, self.right = self.expression.split()
		
		self.left.decompose()
		self.solvable = True
		if self.right is not None:
			self.right.decompose()
			self.solvable = Equation.has_solutions(self.left, self.right)
			self.right.invert()
			self.left.pass_to_left(self.right)

		self.degree = max(self.left.decomposition.keys())
		self.solve()
		print("=" * 50)

	@staticmethod
	def has_solutions(a: Expression, b: Expression):
		# Verify the equation has one or more solutions
		# by checking if the two sides are differents constants
		if len(a.decomposition.items()) == 1 and len(b.decomposition.items()):
			a_key, a_val = list(a.decomposition.items())[0]
			b_key, b_val = list(b.decomposition.items())[0]

			if a_key == 0 and b_key == 0:
				return a_val == b_val
		return True


	def solve(self):
		if not self.solvable:
			print("Equation not solvable")
		elif any([not float(n).is_integer() for n in self.left.decomposition.keys()]):
			print("Cannot solve, degree float")
		elif self.degree > 2:
			print(f"Cannot solve this equation with degree {self.degree}, degree too high")
		elif any([degree < 0 for degree in self.left.decomposition.keys()]):
			print(f"Cannot solve this equation, degree too low")
		elif self.degree == 1:
			a = self.left.decomposition.get(1, 0)
			b = self.left.decomposition.get(0, 0)

			x = -b / a

			equation, solution = self.format(x, None, None, True)
			print(equation)
			print(solution)
		elif self.degree == 2 and len(self.left.decomposition.keys()) == 1:
			factor = float(self.left.expression.split("X")[0])
			x = Equation.sqrt(factor)

			equation, solution = self.format(x, None, None, True)
			print(equation)
			print(solution)
		elif self.degree == 2:
			# Compute delta
			a = self.left.decomposition.get(2, 0)
			b = self.left.decomposition.get(1, 0)
			c = self.left.decomposition.get(0, 0)

			delta = (b ** 2) - (4 * a * c)

			if delta > 0:
				# Two real solutions

				x1 = (-b - Equation.sqrt(delta)) / (2 * a)
				x2 = (-b + Equation.sqrt(delta)) / (2 * a)
				
				equation, solution = self.format(x1, x2, None, True)
				print(equation)
				print(solution)
			elif delta < 0:
				# Two imaginary solutions
				div = (-b) / (2 * a)
				x1 = (-Equation.sqrt(delta)) / (2 * a)
				x2 = (Equation.sqrt(delta) / (2 * a))
				
				print("IMAG")
				equation, solution = self.format(x1, x2, div, False)
				print(equation)
				print(solution)
				pass
			else:
				# One solution
				x = (-b) / (2 * a)
				equation, solution = self.format(x, None, None, True)
				print(equation)
				print(solution)
	
	def format(self, x1: int, x2: int, div: int, reel: bool):
		equation = ""
		solution = ""

		for index, key in enumerate(self.left.decomposition):
			value = self.left.decomposition[key]
			value = value if not value.is_integer() else int(value)
			key = key if not key.is_integer() else int(key)

			if value < 0:
				value = str(value).replace("-", "")
				sign = "-"
			else:
				sign = "+" if index != 0 else ""

			space = " " if index != 0 else ""
			if key == 0:
				equation += f"{space}{sign} {value}"
			elif key == 1:
				equation += f"{space}{sign} {value} * X"
			else:
				equation += f"{space}{sign} {value} * X^{key}"

		equation += " = 0"
		if all(x is not None for x in [x1, x2]):
			if reel:
				solution = f"{equation} admet deux solutions reelles \n\tx1 : {x1}\n\tx2 : {x2}"
			else:
<<<<<<< HEAD
				solution = f"{equation} admet deux solutions complexes \n\tx1 : {div} + {x1}\n\tx2 : {div} - {x2}"
=======
				print("IMAG")
				solution = f"{equation} admet deux solutions complexes \n\tx1 {div} + i {x1}\n\t {div} - i {x2}"
>>>>>>> 83da5640c9fbcc210da5720de859de8605e368ca
		else:
			solution = f"{equation} admet une solution x = {x1}"

		equation = f"Equation simplifiee : {equation}"
		return equation, solution

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