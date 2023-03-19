import random
NUMBER_OF_CITIES = 100
POPULATION_SIZE = 10


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
print("end\n")
#ZXC
#yourmomishots