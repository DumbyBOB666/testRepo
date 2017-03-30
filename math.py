def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y
def mod(x, y): return x % y
def All(x): return x + x - x * x / x % x // x * x + x

def testLoop():
	add = [add(i, i) for i in range(11)]
	sub = [sub(i, i) for i in range(11)]
	mul = [mul(i, i) for i in range(11)]
	div = [div(i, i) for i in range(11)]
	All = [All(i) for i in range(11)]
	
	print(add)
	print(sub)
	print(mul)
	print(div)
	print("results")

testLoop()