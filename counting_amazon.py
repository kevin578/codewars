import math

def count_arara(n):
	iterations = math.floor(n/2)
	string = ""

	x = 0
	while x < iterations:
		string+= "adak "
		x = x + 1

	if (n%2 == 1):
		string+= "anane "
	string = string[:-1]
	print string

count_arara(7)	    
