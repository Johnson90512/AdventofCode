#!/bin/env python3 
 
'''
The first order of business is to figure out how quickly the depth increases, 
just so you know what you're dealing with - you never know if the keys will get
carried into deeper water by an ocean current or a fish or something.
'''

count = 0
x = 0

with open('./2021/day1/input.txt') as f:
    for line in f.readlines():
        line_num = int(line)
        if line_num > x:
            count = count + 1
        
        x = line_num
    print(count - 1)
