while True:
	try:
		a = int(input("Enter a number: "))
		break
	except:
		print("Sorry, you need to enter a whole number")

while True:
	try:
		b = int(input("Enter another number: "))
		break
	except:
		print("Sorry, you need to enter a whole number")
	
def euclid(a, b):
	return b and euclid(b, a%b) or a

result = euclid(a, b)

print("The highest common divisor is {} ".format(result))
