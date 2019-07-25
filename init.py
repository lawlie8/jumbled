import sys
import os
import time
x = open('words_alpha.txt')
y = open('output\\wordlist.txt')
hell = x.readlines()
there = y.readlines()
for get in there:
    for yell in hell:
        if yell == get:
            print(yell,time.strftime('%H:%M:%S'))
print('Process completed at',time.strftime('%H:%M:%S'))
