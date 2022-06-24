# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
	i = 1

	# An Infinite loop to generate squares
	while True:
		yield i*i
		# Next execution resumes from this point
		i += 1
		
# Driver Code
for num in nextSquare():
	if num > 1000:
		break
	print(num)
