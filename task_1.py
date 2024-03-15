

def generate_squares(start, end):
    return [i**2 for i in range(start, end + 1)]



if __name__ == '__main__':
    squares = [i ** 2 for i in range(1, 11)]
    print(squares)
    squares = generate_squares(1, 10)
    print(squares)





