''' Write a Python function that prints out the first n rows of Pascal's triangle. Note:
Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Sample Pascal's triangle:
Each number is the two numbers above it added together'''


# Print Pascal's Triangle in Python
from math import factorial

# input n
def pascal_triangle(n):

    for i in range(n):
	    for j in range(n-i+1):

		    # for left spacing
		    print(end=" ")

	    for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		    print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	    print()
# driver code
pascal_triangle(5)
