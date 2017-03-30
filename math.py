def Add(x, y): return x + y
def Sub(x, y): return x - y
def Mul(x, y): return x * y
def Div(x, y): 
	try: return x / y
	except: return 'error'
def Mod(x, y): return x % y
def All(x): 
	try: return x + x - x * x / x % x // x * x + x
	except: return 'error'
def testLoop():
	addR = [Add(i, i) for i in range(11)]
	subR = [Sub(i, i) for i in range(11)]
	mulR = [Mul(i, i) for i in range(11)]
	divR = [Div(i, i) for i in range(11)]
	AllR = [All(i) for i in range(11)]

	print(addR)
	print(subR)
	print(mulR)
	print(divR)
	print("results")

testLoop()
 