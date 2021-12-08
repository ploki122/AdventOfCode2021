from utils.aoc_utils import AOCDay, day

global chars
chars = ["abcefg", 
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
    
    known_patterns = []

    def __init__(self, line):
        self.inputs = line[:line.index("|")-1].split(" ")
        self.outputs = line[line.index("|")+2:].split(" ")
        self.segments = {"a":Segment(), "b":Segment(), "c":Segment(), "d":Segment(), "e":Segment(), "f":Segment(), "g":Segment()}
        self.known_patterns = [""]*10

    def __str__(self):
        return " ".join(self.inputs + ["|"] + self.outputs)

    def match_solve(self):
        # 0 - 6 length, 1, -4, 7
        # 1 - 2 length
        # 2 - 5 length, -1
        # 3 - 5 length, 1, -4, 7
        # 4 - 4 length
        # 5 - 5 length, -1
        # 6 - 6 length, -1
        # 7 - 3 length
        # 8 - 7 length
        # 9 - 6 length, 1, 4, 7

        for display in self.inputs:
            if len(display) == 2:
                self.known_patterns[1] = set(display)
            elif len(display) == 3:
                self.known_patterns[7] = set(display)
            elif len(display) == 4:
                self.known_patterns[4] = set(display)
            elif len(display) == 7:
                self.known_patterns[8] = set(display)
            else:
                display_5_6.append(display)
        
        for display in display_5_6:
            if len(display) == 5:
                if self.known_patterns[1].issubset(set(display)):
                    self.known_patterns[3] = set(display)
                elif len(self.known_patterns[4].difference(set(display))) == 1:
                    self.known_patterns[5] = set(display)
                else:
                    self.known_patterns[2] = set(display)
            elif len(display) == 6:
                if not self.known_patterns[1].issubset(set(display)):
                    self.known_patterns[6] = set(display)
                elif self.known_patterns[4].issubset(set(display)):
                    self.known_patterns[9] = set(display)
                else:
                    self.known_patterns[0] = set(display)
            else:
                print(display, "?")

    def solve(self):
        progress_is_made = True
        while (progress_is_made):
            progress_is_made = False
            for display in self.inputs:
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
            
    def match_compute_value(self):
        total = 0
        for number in self.outputs :
            for i in range(len(self.known_patterns)):
                if self.known_patterns[i] == set(number):
                    total = total * 10 + i
                    break

        print("compute", total)
        return total
            
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

        return "+"
    
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