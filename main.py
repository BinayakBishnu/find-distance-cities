import math


class Coordinates:
    def __init__(self):
        self.x_coordinate = '0.0N'
        self.y_coordinate = '0.0E'

    def extract_numbers(self):
        self.x_numeric = float(self.x_coordinate[0:len(
            self.x_coordinate)-1:1].strip())

        self.y_numeric = float(self.y_coordinate[0:len(
            self.y_coordinate)-1:1].strip())

        print(self.x_numeric, self.y_numeric)

    def extract_hemisphere(self):
        if self.x_coordinate[-1] == 'N':
            self.x_hemisphere = 'N'
        if self.x_coordinate[-1] == 'S':
            self.x_hemisphere = 'S'

        if self.y_coordinate[-1] == 'E':
            self.y_hemisphere = 'E'
        if self.y_coordinate[-1] == 'W':
            self.y_hemisphere = 'W'

        print(self.x_hemisphere, self.y_hemisphere)

    def get_coordinates(self):
        self.x_coordinate = input("Enter x coordinate: ")
        self.y_coordinate = input("Enter y coordinate: ")

        self.extract_numbers()
        self.extract_hemisphere()

    def show_coordinates(self):
        print(self.x_numeric, self.x_hemisphere,
              '|', self.y_numeric, self.y_hemisphere)

    def calculate_distance(self, other):
        if self.x_hemisphere == other.x_hemisphere:
            x_distance = abs(self.x_numeric - other.x_numeric)

        else:
            x_distance = self.x_numeric + other.y_numeric

        x_distance = x_distance
        print(x_distance)

        if self.y_hemisphere == other.y_hemisphere:
            y_distance = abs(self.y_numeric - other.y_numeric)

        else:
            y_distance = self.y_numeric + other.y_hemisphere

        y_distance = y_distance
        print(y_distance)

        sum_of_squares = (x_distance*x_distance) + (y_distance*y_distance)
        distance = math.sqrt(sum_of_squares)

        print(round(distance*111, 3))


A = Coordinates()
A.get_coordinates()
A.show_coordinates()

B = Coordinates()
B.get_coordinates()
B.show_coordinates()

A.calculate_distance(B)
