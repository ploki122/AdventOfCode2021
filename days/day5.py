from utils.aoc_utils import AOCDay, day

@day(5)
class Day5(AOCDay):
    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")
        return 0

    def part1(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
        ocean_floor = [[0 for i in range(0, 1000)] for j in range(0, 1000)]

        for line in self.inputData:
            coord1, coord2 = self.parseline(line)
            if coord1.x == coord2.x or coord1.y == coord2.y:
                if self.minimalisticTrace: 
                    print(str(coord1) + " -> " + str(coord2))
                for i in range(min(coord1.x, coord2.x), max(coord1.x, coord2.x)+1):
                    for j in range(min(coord1.y, coord2.y), max(coord1.y, coord2.y)+1):
                        ocean_floor[i][j] += 1
        
        count = 0
        for line in ocean_floor:
            for datum in line:
                if datum > 1:
                    count += 1

        return count
    
    def part2(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
        ocean_floor = [[0 for i in range(0, 1000)] for j in range(0, 1000)]

        for line in self.inputData:
            coord1, coord2 = self.parseline(line)
            minx = min(coord1.x, coord2.x)
            miny = min(coord1.y, coord2.y)
            maxx = max(coord1.x, coord2.x)
            maxy = max(coord1.y, coord2.y)

            if coord1.x == coord2.x or coord1.y == coord2.y:
                if self.minimalisticTrace: 
                    print(str(coord1) + " -> " + str(coord2))
                for i in range(minx, maxx+1):
                    for j in range(miny, maxy+1):
                        ocean_floor[i][j] += 1
                        
            elif maxx-minx == maxy-miny:
                if self.minimalisticTrace: 
                    print(str(coord1) + " -> " + str(coord2))
                factor_x = 1 if coord2.x >= coord1.x else -1
                factor_y = 1 if coord2.y >= coord1.y else -1
                for i in range(0, maxx-minx+1):
                    ocean_floor[coord1.x + (i*factor_x)][coord1.y + (i*factor_y)] += 1
                    
            else:
                if self.minimalisticTrace: 
                    print("Skip : " + str(coord1) + " -> " + str(coord2))
        
        count = 0
        for line in ocean_floor:
            for datum in line:
                if datum > 1:
                    count += 1

        return count

    def parseline(self, line):
        coords = [coord.split(",") for coord in line.split(" -> ")]
        return Coord(coords[0][0], coords[0][1]), Coord(coords[1][0], coords[1][1])
    
class Coord():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"