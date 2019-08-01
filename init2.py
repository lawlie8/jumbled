import sys
import os
import time
def check(get,list,x,hell):
    for c in list:
        if get[0] == c:
            pos = list.index(c)
            pos1 = lines[pos]
            pos2 = lines[pos+1]
            hell = hell[pos1:pos2]
            print(pos1,pos2)
            for yell in hell:
                if yell == get:
                    print(yell,time.strftime('%H:%M:%S'))
x = open('words_alpha.txt')
y = open('output\\sortlist.txt')
hell = x.readlines()
there = y.readlines()
list  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lines = [1, 25418, 43831, 75937, 94670, 108867, 120760, 131713, 145456, 159798, 162638, 166590, 176592, 196397, 209855, 222536, 257396, 259189, 275972, 314736, 333555, 356322, 361651, 368210,368717]
for get in there:
    check(get,list,x,hell)
print('Process completed at',time.strftime('%H:%M:%S'))
