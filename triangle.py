def is_triangle(a, b, c):
    
	if (a + b > c):
		if (b + c > a):
			if (c + a > b):
				return True
    
	return False

print(is_triangle(1, 2, 2))
print(is_triangle(7, 2, 2))