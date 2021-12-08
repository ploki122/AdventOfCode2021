from utils.aoc_utils import AOCDay, day

@day(7)
class Day7(AOCDay):
    min = 0
    max = 0
    avg = 0

    def common(self):
        print("\n\n== Common ==")
        self.inputData = [int(x) for x in self.inputData[0].split(",")]
        
        self.min = min(self.inputData)
        self.max = max(self.inputData)
        self.avg = sum(self.inputData)/len(self.inputData)
        print(self.min, self.avg, self.max)

        return 0

    def part1(self):
        print("\n\n== Part 1 ==")
        distances = [sum([abs(datum - index) for datum in self.inputData]) for index in range(self.min, self.max)]
        return min(distances[self.min:self.max])
    
    def part2(self):
        print("\n\n== Part 2 ==")
        distances = [sum([(abs(datum - index)**2+abs(datum - index))/2 for datum in self.inputData]) for index in range(self.min, self.max)]
        return min(distances[self.min:self.max])