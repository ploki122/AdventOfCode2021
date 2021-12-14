from utils.aoc_utils import AOCDay, day

@day(4)
class Day4(AOCDay):
    numbers = []
    cards = []

    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")
        self.numbers = self.inputData[0].split(",")
        i=2
        while i < len(self.inputData):
            self.cards.append(BingoCard(self.inputData[i:i+5]))
            i+= 6

        return 0

    def part1(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
        for i in range(6, len(self.numbers)) :
            for card in self.cards:
                if card.has_bingo(self.numbers[0:i]):
                    return card.score(self.numbers[0:i])
                    
        return 0
    
    def part2(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
        for i in range(6, len(self.numbers)) :
            remaining_cards = []

            for card in self.cards:
                if card.has_bingo(self.numbers[0:i]):
                    if len(self.cards) == 1:
                        return card.score(self.numbers[0:i])
                else:
                    remaining_cards.append(card)
            
            self.cards = remaining_cards

        return 0

class BingoCard():
    lines = []
    def __init__(self, lines):
        self.lines = [[line[i:i+2].strip() for i in range(0, 14, 3)] for line in lines]


    def has_bingo(self, numbers):
        return False in [False in [self.lines[i][j] in numbers for i in range(0, 5)] for j in range(0, 5)] or False in [False in [self.lines[j][i] in numbers for i in range(0, 5)] for j in range(0, 5)]
        
    def score(self, numbers) :
        score = 0
        printStr = ""
        for i in range(0, 5):
            printStr += "\n"
            for j in range(0, 5):
                if self.lines[i][j] in numbers:
                    printStr += "\033[2m"

                printStr += self.lines[i][j].rjust(2, " ")

                if not self.lines[i][j] in numbers:
                    score += int(self.lines[i][j])
        
                if self.lines[i][j] in numbers:
                    printStr += "\033[0m"
                    
                printStr += " "

        # print(printStr)
        # print(str(score) + " * " + numbers[len(numbers)-1])
        return score * int(numbers[len(numbers)-1])
