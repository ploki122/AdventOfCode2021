from utils.aoc_utils import AOCDay, day

global charset
charset = {"0":"abcefg", 
           "1":"cf", 
           "2":"acdeg", 
           "3":"acdfg", 
           "4":"bcdf", 
           "5":"abdfg", 
           "6":"abdefg", 
           "7":"acf", 
           "8":"abcdefg", 
           "9":"abcdfg"}

global segment_list
segment_list = "".join(sorted("".join(set("".join(charset.values())))))

global chars_by_length
chars_by_length = {length:list(filter(lambda x: (len(x) == length), charset.values())) for length in range(len(segment_list)+1)}

global mandatory_segments_by_length
mandatory_segments_by_length = {key:"".join(list(filter(lambda c:("".join(chars_by_length[key])).count(c)==len(chars_by_length[key]) and len(chars_by_length[key]) > 0, [char for char in segment_list]))) for key in chars_by_length.keys()}
    
global obsolete_segments_by_length
obsolete_segments_by_length = {key:"".join(list(filter(lambda c:("".join(chars_by_length[key])).count(c)==0, [char for char in segment_list]))) for key in chars_by_length.keys()}

@day(8)
class Day8(AOCDay):
    charset = {}
    segment_list = []
    chars_by_length = {}
    mandatory_segments_by_length = {}
    obsolete_segments_by_length = {}

    def common(self):
        print("\n\n== Common ==")
        print("charset", charset)
        print("segment_list", segment_list)
        print("chars_by_length", chars_by_length)
        print("mandatory_segments_by_length", mandatory_segments_by_length)
        print("obsolete_segments_by_length", obsolete_segments_by_length)
        
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
            total += int(line.compute_value(), len(charset))

        return total

class Display():
    segments = {}
    inputs = []
    outputs = []

    def __init__(self, line):
        self.inputs = line[:line.index("|")-1].split(" ")
        self.outputs = line[line.index("|")+2:].split(" ")
        self.segments = {segment:Segment() for segment in segment_list}

    def __str__(self):
        return " ".join(self.inputs + ["|"] + self.outputs)

    def solve(self):
        progress_is_made = True
        useful_cryptos = self.outputs
        while (progress_is_made):
            progress_is_made = False
            for display in self.outputs + self.inputs:
                for (key, segment) in self.segments.items():
                    if key in display:
                        progress_is_made = segment.is_in_length(len(display)) or progress_is_made
                    else:
                        progress_is_made = segment.is_not_in_length(len(display)) or progress_is_made
            
            for (key, segment) in self.segments.items():
                if segment.value() is not None:
                    for (key2, segment2) in self.segments.items():
                        if key2 != key:
                            progress_is_made = segment2.remove(segment.value()) and progress_is_made
                
    def compute_value(self):
        value = ""
        for i in range(len(self.outputs)):
            value += self.decode(self.outputs[i])

        return value
      
    def decode(self, segments):
        expected_match = "".join(sorted(set("".join([self.segments[char].possible for char in segments]))))
        if len(expected_match) != len(segments):
            return None

        for (char, pattern) in charset.items() :
            if pattern == expected_match :
                return char
                
        return None
        
class Segment():
    possible = segment_list
    
    def value(self):
        if len(self.possible) == 1:
            return self.possible
    
    def is_in_length(self, length):
        has_changed = False
        if len(chars_by_length[length]) == 1:
            has_changed = self.keep(chars_by_length[length][0])
        
        has_changed = self.remove(obsolete_segments_by_length[length]) and has_changed
        
        return has_changed

    def is_not_in_length(self, length):
        has_changed = False
        if len(chars_by_length[length]) == 1:
            has_changed = self.remove(chars_by_length[length][0])
        
        has_changed = self.remove(mandatory_segments_by_length[length]) and has_changed

        return has_changed

    def remove(self, segments):
        previous_self = self.possible
        self.possible = self.possible.translate({ord(char): None for char in segments})
        return self.possible != previous_self

    def keep(self, segments):
        segments_to_remove = segment_list.translate({ord(char): None for char in segments})
        return self.remove(segments_to_remove)