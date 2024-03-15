
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return "End must be greater than start"
        return [i**2 for i in range(start, end + 1)]



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









