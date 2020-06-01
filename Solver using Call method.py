"""
This Program is an example code to know how to use Special Method Call to make an Arithmetic Solver/Calculator
and use it to directly pass Values and Operation name directly by invoking Object directly instead of its methods.
The object takes in three parametres(operand1, operator, operand2) i.e. (3,"Plus",5) so if we invoke its object and pass
parameters, it would call plus method inside class automatically and return value. 4 Basic Operations of Plus, Minus,
Multiplication and Division are mentioned here.
"""


class Solver(object):
    def __call__(self, operand1, operator, operand2):
        self.operand1 = operand1
        self.operator = operator
        self.operand2 = operand2
        if self.operator == 'Plus':
            return self.Plus()
        elif self.operator == 'Times':
            return self.Times()
        elif self.operator == 'Minus':
            return self.Minus()
        elif self.operator == 'Divide':
            return self.Divide()
        else:
            return 'Wrong Function Passed as Parameter'

    def Plus(self):
        self.plus = self.operand1 + self.operand2
        return self.plus

    def Minus(self):
        self.minus = self.operand1 - self.operand2
        return self.minus

    def Times(self):
        self.times = self.operand1 * self.operand2
        return self.times

    def Divide(self):
        self.divide = self.operand1 / self.operand2
        return self.divide


if __name__ == "__main__":
    a = Solver()
    plus = a(2, "Plus", 8)
    print(plus)
    minus = a(4, "Minus", 8)
    print(minus)
    divide = a(4, "Divide", 8)
    print(divide)
    times = a(4, "Times", 8)
    print(times)

