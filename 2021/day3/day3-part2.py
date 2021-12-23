'''
Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. 
Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find: 
To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, 
and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values 
with a 0 in the position being considered.
'''
cleaned_list = []
gamma = 0
epsilon = 0
gamma_rate = []
epsilon_rate = []

def gamma_calc(iteration):
    zeros = 0
    ones = 0
    for line in cleaned_list:
        if line[iteration] == '0':
            zeros += 1
        if line[iteration] == '1':
            ones += 1
    if zeros > ones:
        gamma_rate.append('0')
    if ones > zeros:
        gamma_rate.append('1')

def epsilon_calc(iteration):
    zeros = 0
    ones = 0
    for line in cleaned_list:
        if line[iteration] == '0':
            zeros += 1
        if line[iteration] == '1':
            ones += 1
    if zeros < ones:
        epsilon_rate.append('0')
    if ones < zeros:
        epsilon_rate.append('1')


with open('./2021/day3/input.txt') as f:
    input = f.readlines()

for lines in input:
    cleaned_list.append(lines.replace("\n", ""))

for i in range(0, len(lines)):
    gamma_calc(i)
    epsilon_calc(i)

for element in gamma_rate:
    gamma = "".join(gamma_rate)

for element in epsilon_rate:
    epsilon = "".join(epsilon_rate)

gamma_dec = (int(gamma, 2))
epsilon_dec = (int(epsilon, 2))

print(gamma_dec * epsilon_dec)

