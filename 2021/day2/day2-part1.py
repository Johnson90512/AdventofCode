'''
Calculate the horizontal position and depth 
you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''
cleaned_list = []

with open('./2021/day2/input.txt') as f:
    lines = f.readlines()

for x in lines:
    cleaned_list.append(x.replace("\n", ""))
print(cleaned_list)

