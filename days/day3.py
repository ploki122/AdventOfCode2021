from utils.aoc_utils import AOCDay, day

@day(3)
class Day3(AOCDay):    
    def most_common_digit(self, scrub_list, position):
        nb1 = 0
        for line in scrub_list:
            nb1 += int(line[position])

        if nb1 >= len(scrub_list)/2:
            return "1"
        else:
            return "0"

    def common(self):
        return 0

    def part1(self):
        binOmega = ""

        for i in range(len(self.inputData[0])):
            binOmega += self.most_common_digit(self.inputData, i)

        decOmega = int(binOmega, 2)
        decEpsilon = decOmega ^ (pow(2, len(self.inputData[0]))-1)
        
        return decOmega * decEpsilon
    
    def part2(self):
        oxy_gen = self.inputData
        co2_scrub = self.inputData

        for i in range(len(self.inputData[0])):
            most_common_oxy = self.most_common_digit(oxy_gen, i)
            new_oxy = []
            for line_oxy in oxy_gen:
                if (line_oxy[i] == most_common_oxy):
                    new_oxy.append(line_oxy)
            oxy_gen = new_oxy
            if len(oxy_gen)== 1:
                break

        for i in range(len(self.inputData[0])):
            most_common_co2 = self.most_common_digit(co2_scrub, i)
            if self.minimalisticTrace: 
                print("")
                print("most_common_digit(self, " + str(co2_scrub) + ", " + str(i) + ") = " + most_common_co2)
            new_co2 = []
            for line_co2 in co2_scrub:
                if (line_co2[i] != most_common_co2):
                    new_co2.append(line_co2)

            co2_scrub = new_co2
            if len(co2_scrub)== 1:
                break
        
        if self.minimalisticTrace: 
            print("oxy : " + str(oxy_gen))
            print("co2 : " + str(co2_scrub))
        dec_oxy = int(oxy_gen[0], 2)
        dec_co2 = int(co2_scrub[0], 2)

        return dec_oxy * dec_co2