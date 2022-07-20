
def gcdExtended(a, b):
	
	# base case
	if a == 0:
		return b, 0, 1
	
	gcd, x1, y1 = gcdExtended(b % a, a)
	
	# update x and y using results of recursive call
	x = y1 - (b//a) * x1
	y = x1
	
	return gcd, x, y
	
	
a, b = 6, 6

g, x, y = gcdExtended(a, b)

print("gcd(", a, ",", b, ") = ", g)
