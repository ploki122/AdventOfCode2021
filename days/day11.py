from utils.aoc_utils import AOCDay, day


@day(11)
class Day11(AOCDay):
    array = None
    def common(self):
        print("\n\n== Common ==")
        return 0

    def part1(self):
        print("\n\n== Part 1 ==")
        self.array = PoulpeArray(self.inputData)
        total = 0

        for days in range(0, 100):
            for line in self.array.poulpes:
                for poulpe in line:
                    poulpe.increment(1)
                    
            for line in self.array.poulpes:
                for poulpe in line:
                    total += poulpe.try_reset()
                    
        return total
    
    def part2(self):
        print("\n\n== Part 2 ==")
        self.array = PoulpeArray(self.inputData)

        array_size = len(self.array.poulpes) * len(self.array.poulpes[0])
        for days in range(1, 10001):
            total = 0
            for line in self.array.poulpes:
                for poulpe in line:
                    poulpe.increment(1)
                    
            for line in self.array.poulpes:
                for poulpe in line:
                    total += poulpe.try_reset()

            if days in [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                print("After step", days)
                print(self.array)

            if total == array_size:
                return days
                    
        return 0

    def neighbors(self, i, j):
        neighbors = []
        if (i>0):
            if(j>0):
                neighbors.append(self.inputData[i-1][j-1])

class PoulpeArray():
    poulpes = []
    
    def __init__(self, inputData):
        self.poulpes = []
        for i, line in enumerate(inputData):
            self.poulpes.append([])
            if line == "": break
            
            for j, char in enumerate(line):
                new_poulpe = Poulpe(j, i, int(char))
                self.poulpes[i].append(new_poulpe)
                self.try_add_neighbor(j-1, i-1, new_poulpe)
                self.try_add_neighbor(j  , i-1, new_poulpe)
                self.try_add_neighbor(j+1, i-1, new_poulpe)
                self.try_add_neighbor(j-1, i  , new_poulpe)

        if len(self.poulpes) > 0:
            del self.poulpes[len(self.poulpes) - 1]
            
    def __str__(self) :
        ret = ""
        for line in self.poulpes:
            for poulpe in line:
                if poulpe.valeur != 0 :
                    ret += "\033[2m" + str(poulpe.valeur) + "\033[0m"
                else:
                    ret += str(poulpe.valeur)
            ret += "\n"

        return ret

    def try_add_neighbor(self, x, y, poulpe):
        if y < 0: return
        if y > len(self.poulpes)-1: return
        if x < 0: return
        if x > len(self.poulpes[y])-1: return

        poulpe.neighbors.append(self.poulpes[y][x])
        self.poulpes[y][x].neighbors.append(poulpe)

class Poulpe():
    pos_x = 0
    pos_y = 0
    valeur = 0
    neighbors = []
    is_flashing = False

    def __init__(self, x, y, value) :
        self.pos_x = x
        self.pos_y = y
        self.valeur = value
        self.neighbors = []
        self.is_flashing = False

    def __str__(self) :
        return "(" + str(self.pos_x) + " " + str(self.pos_y) + ") " + str(self.valeur)

    def try_flash(self) :
        if self.is_flashing: return

        if self.valeur > 9:
            self.is_flashing = True
            for neighbor in self.neighbors:
                neighbor.increment(1)

    def increment(self, n):
        self.valeur += 1
        self.try_flash()
        
    def try_reset(self):
        if self.is_flashing:
            self.is_flashing = False
            self.valeur = 0
            return 1
        
        else:
            return 0
