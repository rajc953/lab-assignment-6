'''2. Write a Python function that checks whether a passed string is palindrome or not. Note: 
A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
e.g., madam or nurses run.'''
def palindrome_checker(string):
    
    string = string.replace(" ","")
    string2 = ""
    for i in string:
        string2 = i + string2

    if string2 == string:
        print("The string is a palindrome!")
    else:
        print("The string is not a palindrome!")

# driver code
palindrome_checker('a nut for a jar of tuna')
