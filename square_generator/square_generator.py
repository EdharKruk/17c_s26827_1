import math
from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass



class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if start > end:
            raise ValueError("Start of range cannot be greater than end")
        return [i**3 for i in range(start, end + 1)]


