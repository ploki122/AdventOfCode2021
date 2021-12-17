from utils.aoc_utils import AOCDay, day

@day(17)
class Day17(AOCDay):
    min_x=0
    min_y=0
    max_x=0
    max_y=0

    def common(self):
        if self.minimalisticTrace:
            print("\n\n== Common ==")
        
        self.min_x = int(self.inputData[0].split(",")[0].split("=")[1].split("..")[0])
        self.max_x = int(self.inputData[0].split(",")[0].split("=")[1].split("..")[1])
        self.min_y = int(self.inputData[0].split(",")[1].split("=")[1].split("..")[0])
        self.max_y = int(self.inputData[0].split(",")[1].split("=")[1].split("..")[1])
        
        if self.minimalisticTrace:
            print(self.min_x, self.max_x, self.min_y, self.max_y)
        return 0

    def part1(self):
        if self.minimalisticTrace:
            print("\n\n== Part 1 ==")
        launch_vel = -self.min_y - 1
        return (launch_vel**2 + launch_vel)/2
    
    def part2(self):
        if self.minimalisticTrace:
            print("\n\n== Part 2 ==")
        options = []
        y_velocities={}
        x_velocities={}
        x_infinites=[]
        
        for x_vel in range(1, self.max_x+1):
            if (x_vel**2 + x_vel)/2 >= self.min_x and (x_vel**2 + x_vel)/2 <= self.max_x:
                dist=0
                for step in range(1, x_vel+1):
                    dist += x_vel - (step - 1)
                    if dist >= self.min_x:
                        x_infinites.append((x_vel, step))
                        break
                
                continue
            
            x_dist = 0     
            step = 0
            remaining_vel = x_vel

            while True:
                step += 1
                x_dist += remaining_vel 
                if remaining_vel > 0:
                    remaining_vel -= 1 
                elif remaining_vel < 0:
                    remaining_vel += 1

                if x_dist > self.max_x or remaining_vel == 0:
                    break

                if x_dist < self.min_x:
                    continue

                if step not in x_velocities:
                    x_velocities[step] = []
                    
                x_velocities[step].append(x_vel)

        for y_vel in range(self.min_y, -1*self.min_y):
            y_dist = 0     
            step = 0
            remaining_vel = y_vel

            while True:
                step += 1
                y_dist += remaining_vel 
                remaining_vel -= 1

                if y_dist < self.min_y:
                    break

                if y_dist > self.max_y:
                    continue
                    
                if step not in y_velocities:
                    y_velocities[step] = []
                    
                y_velocities[step].append(y_vel)

        for step_no, y_steps in y_velocities.items() :
            for infinite, min_step in x_infinites :
                if min_step <= step_no :
                    for y_vel in y_steps:
                        if (infinite, y_vel) not in options:
                            options.append((infinite, y_vel))

            if step_no in x_velocities:
                for x_vel in x_velocities[step_no]:
                    for y_vel in y_steps:
                        if (x_vel, y_vel) not in options:
                            options.append((x_vel, y_vel))

        return len(options)