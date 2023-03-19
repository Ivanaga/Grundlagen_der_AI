import random
import math
NUMBER_OF_CITIES = 100
POPULATION_SIZE = 10



print("hui\n")

class Town:
    def __init__(self, index, coordinate_X, coordinate_Y):
        self.index = index
        self.coordinate_X = coordinate_X
        self.coordinate_Y = coordinate_Y


class Individuals:
    def __init__(self, index):
        self.index = index
        self.towns = []

    def add_town(self, town):
        self.towns.append(town)



def distance_computing(city_1, city_2): # city-1 = X; city_2 = Y
    return math.sqrt((city_1.coordinate_X - city_2.coordinate_X) ** 2 + (city_1.coordinate_Y - city_2.coordinate_Y) ** 2)



population = []
for i in range(10):
    population_ = Individuals(i)
    for j in range(100):
        town = Town(j, round(random.uniform(0, 10), 3), round(random.uniform(0, 10), 3))
        population_.add_town(town)
    population.append(population_)
print("begin\n")
print(population[0].towns[99].index)
print(population[0].towns[89].coordinate_X)
print(population[0].towns[89].coordinate_Y)
print("distance: ", distance_computing(population[0].towns[0], population[0].towns[1]))
print("end\n")





