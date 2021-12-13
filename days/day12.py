from utils.aoc_utils import AOCDay, day

@day(12)
class Day12(AOCDay):
    neighbors = {}
    def common(self):
        print("\n\n== Common ==")
        for line in self.inputData:
            if(line == ""):
                break

            start_end = line.split("-")

            if start_end[0] not in self.neighbors:
                self.neighbors[start_end[0]] = []

            self.neighbors[start_end[0]].append(start_end[1])
            
            if start_end[1] not in self.neighbors:
                self.neighbors[start_end[1]] = []

            self.neighbors[start_end[1]].append(start_end[0])
        
        print(self.neighbors)
        return 0 

    def attemptPath_part1(self, path, current_node):
        paths = []

        curr_path = path.copy()
        if current_node not in self.neighbors:
            print("Not a node!")
            return []
        
        curr_path.append(current_node)

        if (current_node == "end"):
            return [curr_path]
        
        for next_choice in self.neighbors[current_node]:
            if next_choice.islower() and next_choice in path:
                continue
                
            for new_path in self.attemptPath_part1(curr_path, next_choice):
                paths.append(new_path)

        return paths


    def attemptPath_part2(self, path, double_used, current_node):
        paths = []

        curr_path = path.copy()
        if current_node not in self.neighbors:
            print("Not a node!")
            return []
        
        curr_path.append(current_node)

        if (current_node == "end"):
            return [curr_path]
        
        for next_choice in self.neighbors[current_node]:
            if next_choice.islower() and next_choice in path:
                if (next_choice in ["start", "end"] or double_used):
                    continue
                
            for new_path in self.attemptPath_part2(curr_path, double_used or (next_choice.islower() and next_choice in path), next_choice):
                paths.append(new_path)

        return paths

    def part1(self):
        print("\n\n== Part 1 ==")
        paths = self.attemptPath_part1([], "start")
        return len(paths)
    
    def part2(self):
        print("\n\n== Part 2 ==")
        paths = self.attemptPath_part2([], "", "start")
        return len(paths)

class NodeSingles():
    nodes = {}
    
    def get_node(name):
        if not name in nodes:
            nodes[name] = Node(name)
        
        return nodes[name]

class Node():
    name = ""
    neighbors = []
    
    def __init__(self, name):
        self.name = name
        
    def add_neighbor(self, node):
        if not node in self.neighbors:
            self.neighbors.append(node)
