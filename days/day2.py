from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    parsedData = []

    def common(self):
        for line in self.inputData:
            self.parsedData.append(line.split(" "))

        return 0

    def part1(self):
        coords = [0, 0]
        for actions in self.parsedData:
            if (actions[0] == "forward"):
                coords[0] += int(actions[1])
            elif (actions[0] == "back"):
                coords[0] -= int(actions[1])
            elif (actions[0] == "up"):
                coords[1] -= int(actions[1])
            elif (actions[0] == "down"):
                coords[1] += int(actions[1])
            else:
                print("command is sus : " + actions[0])

        return coords[0] * coords[1]
    
    def part2(self):
        coords = [0, 0, 0] # X, Y, Aim
        for actions in self.parsedData:
            if (actions[0] == "forward"):
                coords[0] += int(actions[1])
                coords[1] += int(actions[1]) * coords[2]
            elif (actions[0] == "back"):
                coords[0] -= int(actions[1])
                coords[1] -= int(actions[1]) * coords[2]
            elif (actions[0] == "up"):
                coords[2] -= int(actions[1])
            elif (actions[0] == "down"):
                coords[2] += int(actions[1])
            else:
                print("command is sus : " + actions[0])

        return coords[0] * coords[1]