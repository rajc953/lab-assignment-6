'''5. Write a Python function that accepts a hyphen-separated sequence of words as input 
and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''



def function1(string):
    
    string = string.split('-')
    string.sort()
    string = '-'.join(string)
    print(string)

function1("green-yellow-red-white-black")
