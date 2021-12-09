from utils.aoc_utils import AOCDay, day

@day(9)
class Day9(AOCDay):
    rowsize = 0
    basin_per_key = {}
    key_per_basin = {}

    def common(self):
        print("\n\n== Common ==")
        return 0

    def part1(self):
        print("\n\n== Part 1 ==")
        weakspots = []
        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[i])):
                if self.left_square(i, j) <= self.inputData[i][j]:
                    continue

                if self.right_square(i, j) <= self.inputData[i][j]:
                    continue

                if self.up_square(i, j) <= self.inputData[i][j]:
                    continue

                if self.down_square(i, j) <= self.inputData[i][j]:
                    continue

                weakspots.append(int(self.inputData[i][j]))

        print(weakspots)
        return sum(weakspots) + len(weakspots)
    
    def part2(self):
        print("\n\n== Part 2 ==")
        counter = 0
        for i in range(len(self.inputData)):
            counter += 1
            current_basin = counter
            for j in range(len(self.inputData[i])):
                if self.inputData[i][j] == "9":
                    # print("9")
                    counter += 1
                    current_basin = counter
                
                else:
                    # print(i, j, chr(current_basin))
                    
                    if i > 0 and self.inputData[i-1][j] != "9":
                        up_basin = self.basin_per_key[self.key(i-1, j)]
                        if up_basin < current_basin:
                            self.transfer_basin(current_basin, up_basin)
                            current_basin = up_basin
                        elif up_basin > current_basin:
                            self.transfer_basin(up_basin, current_basin)

                    self.add_key_to_basin(self.key(i, j), current_basin)
        
        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[i])):
                key = self.key(i,j)
                if key in self.basin_per_key:
                    print(chr(self.basin_per_key[key]%26+97), end="")
                else:
                    print(" ", end="")
            print()

        biggest_basins = sorted([len(v) for v in self.key_per_basin.values()], reverse=True)
        return biggest_basins[0]*biggest_basins[1]*biggest_basins[2]

    def left_square(self, i, j):
        if i == 0:
            return "9"
        return self.inputData[i-1][j]
        
    def right_square(self, i, j):
        if i == len(self.inputData[i])-1:
            return "9"
        return self.inputData[i+1][j]
    
    def up_square(self, i, j):
        if j == 0:
            return "9"
        return self.inputData[i][j-1]

    def down_square(self, i, j):
        if j == len(self.inputData)-1:
            return "9"
        return self.inputData[i][j+1]

    def add_key_to_basin(self, key, basin):
        # print("cr", key, basin)
        self.basin_per_key[key] = basin

        if not basin in self.key_per_basin: self.key_per_basin[basin] = []
        self.key_per_basin[basin].append(key)
    
    def transfer_basin(self, from_basin, to_basin):
        if not from_basin in self.key_per_basin:
            self.key_per_basin[from_basin] = []
            
        if not to_basin in self.key_per_basin:
            self.key_per_basin[to_basin] = []

        for key in self.key_per_basin[from_basin]:
            # print("rw", key, to_basin)
            self.add_key_to_basin(key, to_basin)

        del self.key_per_basin[from_basin]

    def key(self, i, j):
        return str(i) + ";" + str(j)