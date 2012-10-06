# Write a program that reads two arguments from the command line:
# a symbol, +, -, *, or /
# a natural number n (≥ 0)
# And uses them to output a nice table for the operation from 0 to n, like this (for "+ 4"):
# +  |  0  1  2  3  4
# -------------------
# 0  |  0  1  2  3  4 
# 1  |  1  2  3  4  5
# 2  |  2  3  4  5  6
# 3  |  3  4  5  6  7
# 4  |  4  5  6  7  8
# If you want, you can format your output using the reddit table syntax:
# |+|0|1
# |:|:|:
# |**0**|0|1
# |**1**|1|2
# Becomes this:
# +	0	1
# 0	0	1
# 1	1	2

def operate(op1, op2, operator):
	if operator == "+":
		return op1+op2
	elif operator == "*":
		return op1*op2


def main():
	operator = "+"
	n = 5
	print("%s | " % operator,end="")
	for i in range(0,n):
		print("%d " % i, end="")

	print()		
	
	for i in range(0,n):
		print("---", end="")

	print()

	for i in range(0,n):
		print("%d | " % i, end="")
		for j in range(0,n):
			print("%d " % operate(i,j,operator), end="")
		print()

if __name__ == '__main__':
	main()