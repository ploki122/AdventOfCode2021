from utils.aoc_utils import AOCDay, day

@day(13)
class Day13(AOCDay):
    sheet = []
    instructions = []
    def common(self):
        print("\n\n== Common ==")
        dots = []
        first_half = True
        for line in self.inputData:
            if line == "":
                first_half = False
                continue

            if first_half:
                dots.append({"x":int(line.split(",")[0]), "y":int(line.split(",")[1])})
            else:
                self.instructions.append({"axis":line.split(" ")[2].split("=")[0], "coord": line.split(" ")[2].split("=")[1]})

        length = max([int(dot["x"]) for dot in dots]) + 1
        height = max([int(dot["y"]) for dot in dots]) + 1
        for n in range(0, height):
            self.sheet.append([False] * length)

        print("height", len(self.sheet), "width", len(self.sheet[0]))
        for dot in dots:
            self.sheet[dot["y"]][dot["x"]] = True

        return 0
    
    def mark_dot(self, x, y):
        while len(self.dots)-1 < y:
            pass

    def fold (self, sheet, instruction):
        print(instruction)

        new_sheet = []
        fold_x = len(sheet[0])
        fold_y = len(sheet)

        foldx = instruction["axis"] == "x"
        if foldx:
            fold_x = int(instruction["coord"])
        else: 
            fold_y = int(instruction["coord"])
        
        for y in range(0, fold_y):
            new_sheet.append([])
            for x in range(0, fold_x):
                new_x = fold_x + abs(fold_x - x) if foldx else x
                new_y = fold_y + abs(fold_y - y) if not foldx else y
                if len(sheet) > new_y and len(sheet[new_y]) > new_x:
                    new_sheet[y].append(sheet[y][x] or sheet[new_y][new_x])
                else:
                    val = sheet[y][x]
                    new_sheet[y].append(val) 

        return new_sheet

    def part1(self):
        print("\n\n== Part 1 ==")
        
        new_dots = self.fold(self.sheet, self.instructions[0])
        return sum([int(v) for line in new_dots for v in line])
    
    def part2(self):
        print("\n\n== Part 2 ==")
        new_sheet = self.sheet
        for inst in self.instructions:
            new_sheet = self.fold(new_sheet, inst);        
        
        for line in new_sheet:
            print()
            for dot in line:
                print("#" if dot else ".", end="")

        print()
        print()

        return 0