'''
Calculate the horizontal position and depth 
you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''

cleaned_list = []
split_list = []
horizontal = 0
vertical = 0

with open('./2021/day2/input.txt') as f:
    lines = f.readlines()

for x in lines:
    cleaned_list.append(x.replace("\n", ""))

for i in cleaned_list:
    split_list = i.split(" ")
    if 'forward' in split_list[0]:
        horizontal += int(split_list[1])
    if 'up' in split_list[0]:
        vertical -= int(split_list[1])
    elif 'down' in split_list[0]:
       vertical += int(split_list[1])
       
print(horizontal * vertical)
