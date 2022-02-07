from utils.aoc_utils import AOCDay, day

@day(19)
class Day19(AOCDay):
    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")
            print(self.inputData)
        return 0

    def part1(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
        return 0
    
    def part2(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
        return 0

class Beacon():
    x = 0
    y = 0
    z = 0
    neighbors = []

    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def neighbors(self, orientation):
        transformed_neighbors = []
        for neighbor in neighbors:
            transformed_neighbor = ()
            if orientation//6 == 0:
                transformed_neighbor = (neighbor[0], neighbor[1], neighbor[2])
            elif orientation//6 == 1:
                transformed_neighbor = (neighbor[0], neighbor[2], neighbor[1])
            elif orientation//6 == 2:
                transformed_neighbor = (neighbor[1], neighbor[0], neighbor[2])
            elif orientation//6 == 3:
                transformed_neighbor = (neighbor[1], neighbor[2], neighbor[0])
            elif orientation//6 == 4:
                transformed_neighbor = (neighbor[2], neighbor[0], neighbor[1])
            elif orientation//6 == 5:
                transformed_neighbor = (neighbor[2], neighbor[1], neighbor[0])
            
            if orientation % 4 == 1:
                transformed_neighbor = (-transformed_neighbor[0], -transformed_neighbor[1], -transformed_neighbor[2])
            elif orientation % 4 == 2:
                transformed_neighbor = (-transformed_neighbor[0], -transformed_neighbor[1], transformed_neighbor[2])
            elif orientation % 4 == 3:
                transformed_neighbor = (transformed_neighbor[0], transformed_neighbor[1], -transformed_neighbor[2])

            transformed_neighbors.append(transformed_neighbor)
        
        return transformed_neighbors
                

