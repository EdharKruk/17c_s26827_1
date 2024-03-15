import math

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than start")
        return [i**2 for i in range(start, end + 1)]

    def generate_square_roots(self, start, end):
        try:
            return [math.sqrt(i) for i in self.generate_squares(start, end)]
        except ValueError as e:
            print(e)
            return []


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than start")
        return [i**3 for i in range(start, end + 1)]
