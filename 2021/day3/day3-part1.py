'''
Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, 
then multiply them together. What is the power consumption of the submarine? 
(Be sure to represent your answer in decimal, not binary.)
'''
cleaned_list = []

with open('./2021/day3/input.txt') as f:
    input = f.readlines()

for lines in input:
    cleaned_list.append(lines.replace("\n", ""))

for digit in cleaned_list:
    if digit[1] == 1:

    print(digit[1])