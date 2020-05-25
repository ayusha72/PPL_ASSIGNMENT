page_list = [1, 2, 3, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25]
for i in range (1, 26):
	present = i in page_list 	#it checks whether i is there in the page_list
	if present == False:
		print (i)
