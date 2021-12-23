from utils.aoc_utils import AOCDay, day

@day(18)
class Day18(AOCDay):
    def common(self):
        if self.minimalisticTrace: 
            print("\n\n== Common ==")
            # print(self.inputData)
        return 0

    def part1(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 1 ==")
        
        # long_line = ""
        # 
        # for line in self.inputData:
        #     input_line = ""
        #     temp_line = line
        # 
        #     if long_line != "":
        #         if self.minimalisticTrace:
        #             print("after addition:", "["+long_line+","+line+"]")
        #         long_line = self.red("["+long_line+","+line+"]")
        #     else:
        #         long_line = line
        # 
        # return self.magnitude(long_line)

        long_line = ""
        for line in self.inputData:
            if long_line != "":
                long_line = "[{left},{right}]".format(left=long_line, right=line)
                
                simplify_node = Node(long_line, 1)

                redo = True
                while redo:
                    (_, _, redo, _) = simplify_node.try_explode(None, None)
                    # if redo: print("explode", simplify_node)

                    if not redo:
                        redo = simplify_node.try_split()
                        # if redo: print("split", simplify_node)

                # print(simplify_node)
                
                long_line = str(simplify_node)
            else:
                long_line = line
        
        return Node(long_line, 1).magnitude()

    
    def part2(self):
        if self.minimalisticTrace: 
            print("\n\n== Part 2 ==")
        
        max_magnitude = 0

        for line1 in self.inputData:
            for line2 in self.inputData:
                if line1 == line2:
                    continue

                simplify_node = Node("[{left},{right}]".format(left=line1, right=line2), 1)

                redo = True
                while redo:
                    (_, _, redo, _) = simplify_node.try_explode(None, None)
                    # if redo: print("explode", simplify_node)

                    if not redo:
                        redo = simplify_node.try_split()
                        # if redo: print("split", simplify_node)
                
                if simplify_node.magnitude() > max_magnitude:
                    max_magnitude = simplify_node.magnitude()
                
        return max_magnitude

class Node():
    left = None
    right = None
    value = None
    depth = 0

    def __init__(self, work_string, depth):
        self.depth = depth
        if "," in work_string:
            nesting = 1
            for i in range(1, len(work_string)):
                if work_string[i] == "[":
                    nesting += 1
                elif work_string[i] == "]":
                    nesting -= 1

                if nesting == 1:
                    if not work_string[i+1] == ",":
                        print("fuck!", work_string, i)
                    else:
                        self.left = Node(work_string[1:i+1], depth+1)
                        self.right = Node(work_string[i+2:-1], depth+1)
                        break
        else:
            self.value = int(work_string)

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        elif self.depth >= 5:
            return "\033[2m[{left},{right}]\033[0m".format(left=self.left, right=self.right)
        else:
            return "[{left},{right}]".format(left=self.left, right=self.right)

    def magnitude(self):
        if self.value is not None:
            return self.value
        else:
            return 3*self.left.magnitude() + 2*self.right.magnitude()

    def increase_depth(self):
        self.depth += 1
        self.left.increase_depth()
        self.right.increase_depth()

    def get_leftmost(self):
        if self.value is not None:
            return self.value
        else:
            return self.left.get_leftmost()

    def set_leftmost(self, value):
        if self.value is not None:
            self.value = value
        else:
            self.left.set_leftmost(value)

    def get_rightmost(self):
        if self.value is not None:
            return self.value
        else:
            return self.right.get_rightmost()

    def set_rightmost(self, value):
        if self.value is not None:
            self.value = value
        else:
            self.right.set_rightmost(value)

    def try_split(self):
        if self.value is not None:
            if self.value >= 10:
                self.left = Node(str(self.value//2), self.depth+1)
                self.right = Node(str(self.value - self.left.value), self.depth+1)
                self.value = None

                return True
        else:
            if self.left.try_split(): return True
            if self.right.try_split(): return True

        return False

    def try_explode(self, first_left, first_right):
        if self.value is not None:
            return (first_left, first_right, False, self)

        redo3 = False
        (first_left, new_right, redo1, self.left) = self.left.try_explode(first_left, self.right.get_leftmost())
        self.right.set_leftmost(new_right)
        
        (new_left, first_right, redo2, self.right) = self.right.try_explode(self.left.get_rightmost(), first_right)
        self.left.set_rightmost(new_left)

        if self.depth >= 5:
            if first_left is not None: first_left += self.left.value
            if first_right is not None: first_right += self.right.value
            self.value = 0
            self.left = None
            self.right = None
            redo3 = True

        return (first_left, first_right, redo1 or redo2 or redo3, self)