'''
Start by comparing the first and second three-measurement windows.
The measurements in the first window are marked A (199, 200, 208);
their sum is 199 + 200 + 208 = 607. The second window is marked B 
(200, 208, 210); its sum is 618. The sum of measurements in the second 
window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this 
sliding window increases from the previous sum. So, compare A with B, then compare 
B with C, then C with D, and so on. Stop when there aren't enough measurements left 
to create a new three-measurement sum.
'''
from itertools import count
import more_itertools
from more_itertools import more

converted_lines = []
x = 0
count = 0

with open('./2021/day1/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        converted_lines.append(int(line))

windowed_list = list(more_itertools.windowed(converted_lines, 3))
for i in windowed_list:
    addition = i[0] + i[1] + i[2]
    if addition > x:
        count = count + 1
    
    x = addition

print(count - 1)