import math


class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than start")
        return [i ** 2 for i in range(start, end + 1)]

    def generate_square_roots(self, start, end):
        try:
            return [math.sqrt(i) for i in self.generate_squares(start, end)]
        except ValueError as e:
            print(e)
            return []


def generate_squares(start, end):
    return [i**2 for i in range(start, end + 1)]



if __name__ == '__main__':
    squares = [i ** 2 for i in range(1, 11)]
    print(squares)
    squares1 = generate_squares(1, 10)
    print(squares1)
    generator = SquareGenerator()
    squares2 = generator.generate_squares(1, 10)
    print(squares2)
    generator = SquareGenerator()
    square_roots = generator.generate_square_roots(1, 10)
    print(square_roots)
    generator = SquareGenerator()
    try:
        square_roots = generator.generate_square_roots(10, 1)
    except ValueError as e:
        print(e)









