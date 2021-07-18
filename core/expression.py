import re

class Expression:
	LEFT_REGEX = re.compile(r"(((^[+-]?)|([\+-]))((([0-9]+([\.,][0-9]+)?\*?)?(X((\^[0-9]+([\.,][0-9]+)?)|(\^\(-?[0-9]+([\.,][0-9]+)?\)))?)?)))")
	RIGHT_REGEX = re.compile(r"([\+-]?((([0-9]+([\.,][0-9]+)?\*?)?(X((\^[0-9]+([\.,][0-9]+)?)|(\^\(-?[0-9]+([\.,][0-9]+)?\)))?)?)))")
	# Works with parenthesis
	# MONOME_REGEX = re.compile(r"((\+|\-)?(\s*)(\d*((,|\.)?\d*))(\s*)((\s*)(\*?)(\s*))(X?)(\s*)(\^?)(\s*)(\(?)(-|\+)?(\d*((,|\.)?\d*))(\)?))")

	# Original regex
	# MONOME_REGEX = re.compile(r"((\+|\-)?(\s*)(\d*((,|\.)?\d*))(\s*)((\s*)(\*?)(\s*))(X?)(\s*)(\^?)(\s*)(\d*((,|\.)?\d*)))")

	# Original regex
	# MONOME_REGEX = re.compile(r"((\+|-)?\d*((\.|,)?\d*)X?\^?\(?(\+|-)?(\d*(\.|,)?\d*)\)?)")
	MONOME_REGEX = re.compile(r"((([+-]?)|([\+-]?))((([0-9]+([\.,][0-9]+)?\*?)?(X((\^[0-9]+([\.,][0-9]+)?)|(\^\(-?[0-9]+([\.,][0-9]+)?\)))?)?)))")
	def __init__(self, expression: str):
		self.expression = expression
		self.degree = None
		self.degrees = None
		self.decomposition = {}

	def simplify(self):
		pass

	def is_valid(self):
		pass

	def split(self):
		if self.expression is not None:
			splitted = self.expression.split("=")
			if len(splitted) == 1:
				if len(splitted[0]) == 0:
					return None, None
				return Expression(splitted[0]), None
			elif len(splitted) == 2:
				return Expression(splitted[0]), Expression(splitted[1])
			else:
				return None, None

	def pass_to_left(self, right):
		for key in right.decomposition:
			try:
				right_value = right.decomposition[key]
				if key != 0 and right_value != 0:
					self.decomposition[key] += right_value
			except KeyError:
				self.decomposition[key] = right.decomposition[key]
		self.expression += right.expression
		return dict(self.decomposition)

	def invert(self):
		if not self.decomposition:
			self.decompose()
		
		for key in self.decomposition:
			self.decomposition[key] *= -1

		return dict(self.decomposition)

	def decompose(self):
		monomes = Expression.MONOME_REGEX.findall(self.expression.replace(" ", ""))
		monomes = [monome[0].replace("(", "").replace(")", "") for monome in monomes if monome[0].replace(" ", "")]

		for monome in monomes:
			terms = monome.split("^")
			term = terms[0]

			if len(terms) == 2:
				degree = float(terms[-1])
			else:
				if "X" in term:
					degree = 1.0
				else:
					degree = 0.0

			if "*" in term:
				term = float(term.split("*")[0].replace(",", "."))
			else:
				if term == "X" or term == "+X":
					term = 1.0
				elif term == "-X":
					term = -1.0
				else:
					term = float(term.split("X")[0].replace(",", "."))

			self.decomposition[degree] = term
		
		return dict(self.decomposition)

	def __repr__(self):
		return self.expression
