inputList = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]

def cycleCounter(listx):
	"""Take an input list and find the max element and spread its value throughout.
		If same list occurs again, stop loop and return cycles used.
	"""
	tester = [[10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]]
	tries = 0
	while True:
		i = listx.index(max(listx))
		value = listx[i]
		listx[i] = 0
		i += 1
		while value > 0:
			if i<len(listx):
				listx[i] += 1
			else:
				i = (len(listx) - i)
				listx[i] += 1
			i += 1
			value -= 1
		tries += 1
		if listx not in tester:
			tester.append(listx[:])
		else:
			ind = tester.index(listx[:])
			length = len(tester)
			print("Cycles since last occurance => " + str(length - ind))
			break
	return tries

print(cycleCounter(inputList))