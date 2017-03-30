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

	print(addR)
	print(subR)
	print(mulR)
	print(divR)
	print("results")

def loopFunc(x, func):
	for i in range(x):
		print(func(i, i))

loopFunc(11, Div)

testLoop()

class Loop:
	
	def __init__(self):
		print("Init Loop")

	def loopAdd(self):
		pass
	
	def loopSub(self):
		pass
 # Advance Dec Class


<<<<<<< HEAD
testLoop()
# everything is working fine
=======
>>>>>>> advanceDecClass
 
