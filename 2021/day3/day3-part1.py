'''
Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, 
then multiply them together. What is the power consumption of the submarine? 
(Be sure to represent your answer in decimal, not binary.)
'''
cleaned_list = []
gamma = 0
epsilon = 1
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

