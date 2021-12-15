from utils.aoc_utils import AOCDay, day

@day(15)
class Day15(AOCDay):
    width = 0
    height = 0
    mult_part_2 = 5

    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")

        self.height = len(self.inputData)
        self.width = len(self.inputData[0])
        return 0

    def get(self, x, y, max_mult = 1):
        if y < 0 or y >= self.height * max_mult:
            return None
        
        if x < 0 or x >= self.width * max_mult:
            return None
        
        fetch_x = x % self.width
        fetch_y = y % self.height

        offset = x//self.width + y//self.height
        return (int(self.inputData[fetch_y][fetch_x]) + offset - 1) % 9 + 1

    def part1(self):
        start = (0,0)
        end = (self.width - 1, self.height - 1)
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
            print(start,  "->", end)
        
        distances = {(0,0):0}
        next_steps = {0:[(0,0)]}
        curr_distance = 0
        predecessors = {}
        next_node = None

        while end != next_node:
            while curr_distance not in next_steps or len(next_steps[curr_distance]) == 0:
                curr_distance += 1
                if curr_distance >= (self.width + self.height) * 9:
                    print("SHIT!")
                    return
                
            next_node = next_steps[curr_distance].pop()
            if distances[next_node] < curr_distance: # useless iteration that wasn't cleaned up because I'm lazy
                continue

            for diff in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                coord_calc = (next_node[0] + diff[0], next_node[1] + diff[1])
                next_val = self.get(*coord_calc)
                
                if next_val is None:
                    continue
                
                distance_coord = curr_distance + next_val
                if coord_calc in distances and distances[coord_calc] <= distance_coord:
                    continue

                distances[coord_calc] = distance_coord
                predecessors[coord_calc] = next_node
                
                if distance_coord not in next_steps:
                    next_steps[distance_coord] = []
                next_steps[distance_coord].append(coord_calc)
                
        return distances[end]
    
    def part2(self):
        start = (0,0)
        end = (self.width * self.mult_part_2 - 1, self.height * self.mult_part_2 - 1)
        
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
            print(start,  "->", end)
        
        distances = {(0,0):0}
        next_steps = {0:[(0,0)]}
        curr_distance = 0
        predecessors = {}
        next_node = None

        while end != next_node:
            while curr_distance not in next_steps or len(next_steps[curr_distance]) == 0:
                curr_distance += 1
                if curr_distance >= (self.width + self.height) * self.mult_part_2 * 9:
                    print("SHIT!", curr_distance)
                    return
                
            next_node = next_steps[curr_distance].pop()
            if distances[next_node] < curr_distance: # useless iteration that wasn't cleaned up because I'm lazy
                continue

            for diff in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                coord_calc = (next_node[0] + diff[0], next_node[1] + diff[1])
                next_val = self.get(*coord_calc, self.mult_part_2)
                
                if next_val is None:
                    continue
                
                distance_coord = curr_distance + next_val
                if coord_calc in distances and distances[coord_calc] <= distance_coord:
                    continue

                distances[coord_calc] = distance_coord
                predecessors[coord_calc] = next_node
                
                if distance_coord not in next_steps:
                    next_steps[distance_coord] = []
                next_steps[distance_coord].append(coord_calc)
                
        return distances[end]