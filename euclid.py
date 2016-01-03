import sys

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def euclid(a, b):
	return b and euclid(b, a%b) or a

result = euclid(a, b)

print("The highest common divisor is {} ".format(result))
