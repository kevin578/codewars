

test_array = [1,2,3,4, 5, 6 ,34, 45, 8]



def first_non_consecutive(arr):


	x = 0
	while x < len(arr) - 1:

		check = arr[x + 1] - arr[x] 


		if check > 1:
			return arr[x + 1]

		x += 1


first_non_consecutive(test_array)