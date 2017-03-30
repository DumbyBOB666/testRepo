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

# all math functions

# other functions
def helloW(): print("Hello World!")
def byeW(): print("Goodbye World!")

 