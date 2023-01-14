from nikhil import *

for i in range(8):
	lst1 = [0]*i + [1] + [0]*(7-i)
	lst2 = [0]*i + [2] + [0]*(7-i)
	one = list_to_str(lst1)
	two = list_to_str(lst2)
	ciphertext_one = query_server(one)
	ciphertext_two = query_server(two)
	print(lst1, one, ciphertext_one)
	print(lst2, two, ciphertext_two)
	print(" ")
