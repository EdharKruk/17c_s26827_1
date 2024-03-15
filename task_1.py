import math


from square_generator import CubicGenerator


generator = SquareGenerator()
try:
    squares = generator.generate_squares(1, 10)
    print(squares)
    square_roots = generator.generate_square_roots(1, 10)
    print(square_roots)
except ValueError as e:
    print(e)



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

cubic_generator = CubicGenerator()
try:
    cubes = cubic_generator.generate_squares(11, 10)
    print(cubes)
except ValueError as e:
    print(f"Error: {e}")







