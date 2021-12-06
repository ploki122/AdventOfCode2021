from utils.aoc_utils import AOCDay, day

@day(1)
class DayTemplate(AOCDay):
    def common(self):
        return 0

    def part1(self):
        nbResult = 0
        for i in range(len(self.inputData)-1):
            if (int(self.inputData[i]) < int(self.inputData[i+1])):
                nbResult += 1
        
        print(nbResult)
        return nbResult
    
    def part2(self):
        nbResult = 0
        for i in range(len(self.inputData)-3):
            if (int(self.inputData[i]) < int(self.inputData[i+3])):
                nbResult += 1
        
        print(nbResult)
        return nbResult