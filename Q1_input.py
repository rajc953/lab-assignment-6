''' 1. Write a Python function to check whether a number is perfect or not. According to 
Wikipedia : In number theory, a perfect number is a positive integer that is equal to the 
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the 
number itself (also known as its aliquot sum). Equivalently, a perfect number is a 
number that is half the sum of all of its positive divisors (including itself)'''


def perfect_number(number):
    sum = 0
    for i in range(1,number):
        if number % i ==0:
            sum +=i
    if sum == number:
        print("The number is perfect!")
    else:
        print('The number is not perfect!')
        
perfect_number(28)
perfect_number(82)
