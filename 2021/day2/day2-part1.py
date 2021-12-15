'''
Calculate the horizontal position and depth 
you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''
cleaned_list = []
split_list = []
count = 0

with open('./2021/day2/input.txt') as f:
    lines = f.readlines()

for x in lines:
    cleaned_list.append(x.replace("\n", ""))

for i in cleaned_list:
    split_list.extend(i.split(" "))

for item in split_list:
    if count % 2 == 0:
        
        count = count + 1

