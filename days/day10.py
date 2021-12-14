from utils.aoc_utils import AOCDay, day

@day(10)
class Day10(AOCDay):
    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")
        # print(self.inputData)
        return 0

    def part1(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
        total = 0
        points = {")":3, "]":57, "}":1197, ">":25137}
        for line in self.inputData:
            openings = []
            for char in line:
                if char in ["(", "<", "[", "{"]:
                    openings.append(char)
                elif char in [")", ">", "]", "}"]:
                    last_opening = openings.pop()
                    if last_opening == "(" and char != ")" :
                        total += points[char]
                    elif last_opening == "[" and char != "]" :
                        total += points[char]
                    elif last_opening == "<" and char != ">" :
                        total += points[char]
                    elif last_opening == "{" and char != "}" :
                        total += points[char]
                    else:
                        pass
        return total
    
    def part2(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
        totals = []
        points = {"(":1, "[":2, "{":3, "<":4}
        for line in self.inputData:
            valid_line = True
            openings = []
            total = 0
            for char in line:
                if char in ["(", "<", "[", "{"]:
                    openings.append(char)
                elif char in [")", ">", "]", "}"]:
                    last_opening = openings.pop()
                    if last_opening == "(" and char != ")" :
                        valid_line = False
                        break
                    elif last_opening == "[" and char != "]" :
                        valid_line = False
                        break
                    elif last_opening == "<" and char != ">" :
                        valid_line = False
                        break
                    elif last_opening == "{" and char != "}" :
                        valid_line = False
                        break
                    else:
                        pass
            
            if valid_line:
                while(len(openings)>0):
                    total = 5*total + points[openings.pop()]
                
                totals.append(total)

        totals = sorted(totals)
        return totals[int(len(totals)/2)]