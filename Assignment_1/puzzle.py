list_a = ['goat','tiger', 'grass']
list_b = []
import random
def safe_check(list_c) :
	if 'tiger' in list_c and 'goat' in list_c:
		return False
	elif 'grass' in list_c and 'goat' in list_c:
		return False
	else :
		return True
while len(list_a) != 0 :
	result = list_a.pop()
	if safe_check(list_a) == False :
		list_a.insert(0,result)
		

	else :
		print ('take {}'.format(result))
		list_b.append (result)
		if len (list_b) == 2 and safe_check(list_b) == False :
			if 'tiger' in list_b and 'goat' in list_b:
				list_b.remove('goat')
			elif 'grass' in list_b and 'goat' in list_b:
				list_b.remove('goat')
			list_a.insert (0, 'goat')
			print ('take back goat')
