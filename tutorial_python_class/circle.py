# circle.py
# https://realpython.com/python-classes/#defining-a-class-in-python

import math 


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round (math.pi * self.radius ** 2, 2)
    
