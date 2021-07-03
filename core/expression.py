import re
from pprint import pprint

class Expression:
    LEFT_REGEX = r"(((^[+-]?)|([\+-]))((([0-9]+([\.,][0-9]+)?\*?)?(X((\^[0-9]+([\.,][0-9]+)?)|(\^\(-?[0-9]+([\.,][0-9]+)?\)))?)?)))"
    RIGHT_REGEX = r"([\+-]?((([0-9]+([\.,][0-9]+)?\*?)?(X((\^[0-9]+([\.,][0-9]+)?)|(\^\(-?[0-9]+([\.,][0-9]+)?\)))?)?)))"
    MONOME_REGEX = re.compile(r"((\+|\-)?(\d+((,|\.)\d+)?)(x(\^(\d+((,|\.)\d+)?)?)?)?)")
    def __init__(self, expression: str):
        self.expression = expression
        self.degree = None
        self.degrees = None

    def simplify(self):
        pass

    def is_valid(self):
        pass

    def get_data(self):
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

    def decompose(self):
        decomposition = {}

        monomes = Expression.MONOME_REGEX.findall(self.expression)
        monomes = [monome[0] for monome in monomes]

        for monome in monomes:
            terms = monome.split("^")
            term = terms[0]
            if len(terms) == 2:
                degree = int(terms[-1])
            else:
                if "x" in term:
                    degree = 1
                else:
                    degree = 0
            
            term = float(term.split("x")[0].replace(",", "."))
            decomposition[degree] = term
        print("=" * 40)
        print(self.expression)
        pprint(decomposition)

        


    def __repr__(self):
        return self.expression