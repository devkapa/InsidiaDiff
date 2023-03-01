from symengine import Symbol, sympify, symbols
from symengine.lib.symengine_wrapper import solve as sol
from sympy import solveset, EmptySet


class Relation:

    equation: str
    colour: tuple
    x_values: object
    y_values: object

    def __init__(self, equation, colour) -> None:
        self.equation = equation
        self.colour = colour
        x = Symbol('x')
        y = Symbol('y')
        self.x_values = sympify(solveset(self.get_expression(), x))
        self.y_values = sympify(solveset(self.get_expression(), y))

    def get_expression(self) -> object:
        return self.equation

    def get_colour(self) -> tuple:
        return self.colour

    def f(self) -> int:
        return self.x_values, self.y_values
