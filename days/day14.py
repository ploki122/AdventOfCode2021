from utils.aoc_utils import AOCDay, day

@day(14)
class Day14(AOCDay):
    polymer = ""
    equations = {}
    pairs = {}
    def common(self):
        print("\n\n== Common ==")
        for line in self.inputData:
            if self.polymer == "":
                self.polymer = line
            else:
                if line == "":
                    continue
                key = line.split(" -> ")[0]
                value = [key[0] + line.split(" -> ")[1], line.split(" -> ")[1] + key[1]]
                self.equations[key] = value

        for i in range(0, len(self.polymer)-1):
            fragment = self.polymer[i:i+2]
            if fragment not in self.pairs:
                self.pairs[fragment] = 0
            self.pairs[fragment] += 1

        print(self.polymer, self.pairs, self.equations)
        return 0

    def part1(self):
        print("\n\n== Part 1 ==")
        work_pairs = self.pairs.copy()
        print(0, work_pairs)
        print(self.equations)
        for step in range(0, 10):
            new_pairs = {}
            for (pair, num) in work_pairs.items():
                if pair in self.equations:
                    for result in self.equations[pair]:
                        if result not in new_pairs:
                            new_pairs[result] = 0
                        new_pairs[result] += num
            work_pairs = new_pairs
            print(step, work_pairs)
        
        occurences = {}
        for (pair, num) in work_pairs.items():
            for i in range (0,2):
                if pair[i] not in occurences:
                    occurences[pair[i]] = 0
                occurences[pair[i]] += num
        occurences[self.polymer[0]] += 1
        occurences[self.polymer[len(self.polymer)-1]] += 1

        my_min = min(occurences.values())
        my_max = max(occurences.values())

        return int((my_max - my_min)/2)
    
    def part2(self):
        print("\n\n== Part 2 ==")
        work_pairs = self.pairs.copy()
        print(0, work_pairs)
        print(self.equations)
        for step in range(0, 40):
            new_pairs = {}
            for (pair, num) in work_pairs.items():
                print(pair, num)
                if pair in self.equations:
                    for result in self.equations[pair]:
                        if result not in new_pairs:
                            new_pairs[result] = 0
                        new_pairs[result] += num
            work_pairs = new_pairs
            print(step, work_pairs)
        
        occurences = {}
        for (pair, num) in work_pairs.items():
            for i in range (0,2):
                if pair[i] not in occurences:
                    occurences[pair[i]] = 0
                occurences[pair[i]] += num
        occurences[self.polymer[0]] += 1
        occurences[self.polymer[len(self.polymer)-1]] += 1

        print(self.polymer[0], self.polymer[len(self.polymer)-1], occurences.values(), min(occurences.values()), max(occurences.values()))
        my_min = min(occurences.values())
        my_max = max(occurences.values())

        return int((my_max - my_min)/2)