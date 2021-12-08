from utils.aoc_utils import AOCDay, day

global char_segments
char_segments = ["abcefg", 
                 "cf", 
                 "acdeg", 
                 "acdfg", 
                 "bcdf", 
                 "abdfg", 
                 "abdefg", 
                 "acf", 
                 "abcdefg", 
                 "abcdfg"]

@day(8)
class Day8(AOCDay):
    def common(self):
        print("\n\n== Common ==")
        parsedData = []
        for line in self.inputData:
            if line == "":
                break

            parsedData.append(Display(line))
        
        self.inputData = parsedData
        return 0

    def part1(self):
        print("\n\n== Part 1 ==")
        count = 0
        for line in self.inputData:
            for word in line.outputs:
                if len(word) in [2, 4, 3, 7]:
                    count += 1
        return count
    
    def part2(self):
        print("\n\n== Part 2 ==")
        total = 0
        for line in self.inputData:
            line.solve()
            total += line.compute_value()

        return total

class Display():
    segments = {}

    inputs = []
    outputs = []
    
    def __init__(self, line):
        self.inputs = line[:line.index("|")-1].split(" ")
        self.outputs = line[line.index("|")+2:].split(" ")
        self.segments = {"a":Segment(), "b":Segment(), "c":Segment(), "d":Segment(), "e":Segment(), "f":Segment(), "g":Segment()}

    def __str__(self):
        return " ".join(self.inputs + ["|"] + self.outputs)

    def solve(self):
        progress_is_made = True
        while (progress_is_made):
            progress_is_made = False
            for display in self.inputs + self.outputs:
                for (key, segment) in self.segments.items():
                    if key in display:
                        progress_is_made = segment.is_in_segments(display) or progress_is_made
                    else:
                        progress_is_made = segment.is_not_in_segments(display) or progress_is_made
            
            for (key, segment) in self.segments.items():
                if segment.value() is not None:
                    for (key2, segment2) in self.segments.items():
                        if key2 != key:
                            progress_is_made = segment2.remove_options(segment.value()) and progress_is_made
            
            
    def compute_value(self):
        total = 0
        for i in range(len(self.outputs)):
            total += self.what_number(self.outputs[i]) * 10**(len(self.outputs)-i-1)

        return total
        
    def what_number(self, segments):
        expected_match = "".join(sorted(set("".join([self.segments[char].possible for char in segments]))))
        
        for i in range(0, 10):
            if char_segments[i] == expected_match :
                return i
        

class Segment():
    possible = "abcdefg"
    
    def value(self):
        if len(self.possible) == 1:
            return self.possible

        return "z"
    
    def is_in_segments(self, display):
        length = len(display)
        # 2 = [1]
        # 3 = [7]
        # 4 = [4]
        # 5 = [2, 3, 5]
        # 6 = [0, 6, 9]
        # 7 = [8]

        if length == 2 :
            return self.remove_options("abdeg")
        elif length == 3 :
            return self.remove_options("bdeg")
        elif length == 4 :
            return self.remove_options("aeg")
        elif length == 5 :
            return False
        elif length == 6 :
            return False
        elif length == 7 :
            return False
        else :
            print("What the fuck?", display, length)
            return False

    def is_not_in_segments(self, display):
        length = len(display)
        # 2 = [1]
        # 3 = [7]
        # 4 = [4]
        # 5 = [2, 3, 5]
        # 6 = [0, 6, 9]
        # 7 = [8]

        if length == 2 :
            return self.remove_options("cf")
        elif length == 3 :
            return self.remove_options("acf")
        elif length == 4 :
            return self.remove_options("bcdf")
        elif length == 5 :
            return self.remove_options("adg")
        elif length == 6 :
            return self.remove_options("abfg")
        elif length == 7 :
            return False
        else :
            print("What the fuck?", display, length)
            return False

    def remove_options(self, segments):
        previous_self = self.possible
        self.possible = self.possible.translate({ord(char): None for char in segments})
        return self.possible != previous_self