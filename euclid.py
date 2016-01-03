import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def euclid(a, b):
	return b and euclid(b, a%b) or a

result = euclid(a, b)

print result
