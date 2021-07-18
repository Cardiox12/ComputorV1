import unittest
from pprint import pprint
from core.expression import Expression


class ExpressionTest(unittest.TestCase):
    def test_split(self):
        self.assertEqual(
            Expression("4X = 0").split(), 
            (Expression("4X"), Expression("0"))
        )

        self.assertEqual(
            Expression("4X").split(), 
            (Expression("4X"), None)
        )

        self.assertEqual(
            Expression("5X^2 + 4X + 2 = 2").split(),
            (Expression("5X^2 + 4X + 2"), Expression("2"))
        )

        self.assertEqual(
            Expression("").split(),
            (None, None)
        )

    def test_decompose(self):
        self.assertEqual(
            Expression("4X + 2").decompose(),
            {
                1.0: 4.0,
                0.0: 2.0
            }
        )

        self.assertEqual(
            Expression("1").decompose(),
            {
                0.0: 1.0
            }
        )

        self.assertEqual(
            Expression("").decompose(),
            {}
        )

        self.assertEqual(
            Expression("2X^3 + 2X^2 - 3X + 1").decompose(),
            {
                3.0: 2.0,
                2.0: 2.0,
                1.0: -3.0,
                0.0: 1.0
            }
        )

        self.assertEqual(
            Expression("-2X^3 + 2X^2 - 3X + 1").decompose(),
            {
                3.0: -2.0,
                2.0: 2.0,
                1.0: -3.0,
                0.0: 1.0
            }
        )

        self.assertEqual(
            Expression("-2.3X^3.2 + 2X^2 - 3X + 1").decompose(),
            {
                3.2: -2.3,
                2.0: 2.0,
                1.0: -3.0,
                0.0: 1.0
            }
        )

        self.assertEqual(
            Expression("-2.3X^3.2 + 2.4X^2 - 3X + 1.4").decompose(),
            {
                3.2: -2.3,
                2.0: 2.4,
                1.0: -3.0,
                0.0: 1.4
            }
        )

    def test_invert(self):
        self.assertEqual(
            Expression("2X + 1").invert(),
            {
                1.0: -2.0,
                0.0: -1.0
            }
        )

        self.assertEqual(
            Expression("2X^2 + X - 2").invert(),
            {
                2.0: -2.0,
                1.0: -1.0,
                0.0: 2.0
            }
        )

        self.assertEqual(
            Expression("").invert(),
            {}
        )

    def test_pass_to_left(self):
        left, right = Expression("-2X^3 + 2X^2 - 3X + 1 = 2X + 3").split()

        self.assertEqual(
            left.pass_to_left(right),
            {
                3.0: -2.0,
                2.0:  2.0,
                1.0: -5.0,
                0.0: -2.0
            }
        )

        left, right = Expression("-2X^3 + 2X^2 - 3X + 1 = 2X").split()
        self.assertEqual(
            left.pass_to_left(right),
            {
                3.0: -2.0,
                2.0:  2.0,
                1.0: -5.0,
                0.0:  1.0
            }
        )

        left, right = Expression("0 = 0").split()
        self.assertEqual(
            left.pass_to_left(right),
            { 0.0: 0.0 }
        )

        left, right = Expression("-2X^3 + 2X^2 - 3X + 1 = -2X^3 + 2X").split()
        self.assertEqual(
            left.pass_to_left(right),
            {
                3.0:  0.0,
                2.0:  2.0,
                1.0: -5.0,
                0.0:  1.0
            }
        )

        left, right = Expression("-2X^3 + 2X^2 - 3X + 1 = -2X^3 + 2X^2 - 3X + 1").split()
        self.assertEqual(
            left.pass_to_left(right),
            {
                3.0: 0.0,
                2.0: 0.0,
                1.0: 0.0,
                0.0: 0.0
            }
        )

if __name__ == "__main__":
    unittest.main()