from utils.aoc_utils import AOCDay, day
import math

@day(16)
class Day16(AOCDay):
    packet = None

    def common(self):
        if self.minimalisticTrace:
            print("\n\n== Common ==")
        self.packet = Packet(bin(int(self.inputData[0], 16))[2:].rjust(len(self.inputData[0])*4, "0"))
        return 0

    def part1(self):
        if self.minimalisticTrace:
            print("\n\n== Part 1 ==")
        return self.packet.sum_of_version()
    
    def part2(self):
        if self.minimalisticTrace:
            print("\n\n== Part 2 ==")
        return self.packet.value

class Packet():
    version = 0
    packet_type = 0
    content = ""
    value = 0
    length = 0

    def __init__(self, content):
        self.content = content
        self.extract_version(content)
        self.extract_type(content)
        self.extract_value(content)

    def extract_version(self, content):
        bin_version = content[0:3]
        self.version = int(bin_version, 2)
        
    def extract_type(self, content):
        bin_type = content[3:6]
        self.packet_type = int(bin_type, 2)
        
    def extract_value(self, content):
        bin_value = ""
        if(self.packet_type == 4):
            for chunk_start in range(6, len(content), 5):
                next_chunk = content[chunk_start : chunk_start+5]
                bin_value += next_chunk[1:]
                if next_chunk[0] == "0":
                    break

            self.value = int(bin_value, 2)
            self.length = chunk_start + 5
        else:
            self.value = []
            length_type = content[6]
            upper_bound = 0
            exit_counter = 0
            
            if(length_type == "0"):
                self.length = 22
                upper_bound = int(content[7:22], 2)
            else:
                self.length = 18
                upper_bound = int(content[7:18], 2)
            
            while(exit_counter < upper_bound):
                sub_content = content[self.length : ]
                next_packet = Packet(sub_content)

                self.length += next_packet.length
                self.value.append(next_packet)

                if(length_type == "0"):
                    exit_counter += next_packet.length
                else:
                    exit_counter += 1

            if (self.packet_type == 0):
                self.value = sum([child.value for child in self.value])
            elif (self.packet_type == 1):
                self.value = math.prod([child.value for child in self.value])
            elif (self.packet_type == 2):
                self.value = min([child.value for child in self.value])
            elif (self.packet_type == 3):
                self.value = max([child.value for child in self.value])
            elif (self.packet_type == 5):
                self.value = int(self.value[0].value > self.value[1].value)
            elif (self.packet_type == 6):
                self.value = int(self.value[0].value < self.value[1].value)
            elif (self.packet_type == 7):
                self.value = int(self.value[0].value == self.value[1].value)

    def sum_of_version(self):
        ver_sum = self.version
        if isinstance(self.value, list):
            ver_sum += sum([child.sum_of_version() for child in self.value])
        
        return ver_sum
