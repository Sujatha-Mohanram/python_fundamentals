# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:50:11 2023

@author: Sujatha
"""

x = 5
PI = 3.14
y = 'Hey there!'
bo = False
nums = [1,2,3]

print(x)
print(PI)
print(y)
print(bo)
print (nums)

if(10 < 5):
   print('Math is broken!')
elif(10 == 20):
   print('Math is broken!')
else:
    print('Math works!')
    
if( (10 < 5 or 10 < 20) and 1 == 1):
   print('Math works!')
else:
   print('Math is broken')


for i in range(10):
   print(i)


nums = [1,2,3,4]
for num in nums:
    print(num)
    
def do_something(arg1, arg2):
    print(arg1)
    print(arg2)


print('Not in the function!')
do_something('Hey there', 1000)


def check_if_large(test_number):
    if(test_number > 1000):
        return True;
    else:
        return False;


numbers = [100,10000,200,2000,30000]
for number in numbers:
    is_large = check_if_large(number)
    if(is_large):
        print('That’s a huge number!')
    else:
        print('That is NOT a huge number!')
