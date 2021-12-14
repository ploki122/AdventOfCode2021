from utils.aoc_utils import AOCDay, day

@day(6)
class Day6(AOCDay):

    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")        
        return 0

    def part1(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
        
        parsedData = [0]*10
        for fish in self.inputData[0].split(","):
            parsedData[int(fish)] += 1

        if self.minimalisticTrace: 
            print("Day 0 : " + str(parsedData))
        nbDay = 1
        while nbDay <= 80:
            parsedData[7] += parsedData[0]
            parsedData[9] += parsedData[0]
            for i in range(0, len(parsedData)-1):
                parsedData[i] = parsedData[i+1]
            parsedData[9] = 0
                
            if self.minimalisticTrace: 
                print("Day " + str(nbDay) + " : " + str(parsedData))
            nbDay += 1

        return sum(parsedData)
    
    def part2(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
        
        parsedData = [0]*10
        for fish in self.inputData[0].split(","):
            parsedData[int(fish)] += 1

        if self.minimalisticTrace: 
            print("Day 0 : " + str(parsedData))
        nbDay = 1
        while nbDay <= 256:
            parsedData[7] += parsedData[0]
            parsedData[9] += parsedData[0]
            for i in range(0, len(parsedData)-1):
                parsedData[i] = parsedData[i+1]
            parsedData[9] = 0
                
            if self.minimalisticTrace: 
                print("Day " + str(nbDay) + " : " + str(parsedData))
            nbDay += 1

        return sum(parsedData)