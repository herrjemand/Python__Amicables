def amicables(min,max):
	amicables = {}
	prime = lambda z: True if z != 0 and 571**(z-1)%z == 1 else False

	def fact_brute(n):
		lst = [n,[1],0]
		a,b,c = 0,0,1
		if n%2 == 0:
			a, b = 2, int(n/2)
		else:
			a, b, c = 3, int(n/3), 2

		for k in range(a,b + 1,c):
			if n%k == 0:
				lst[1] += [k]

		lst[2] += sum(lst[1])
		return lst

	for i in range(min, max + 1):
		temp = []
		if not prime(i) and i not in amicables.keys() and i not in [0,1]:
			temp += [fact_brute(i)]

			if not prime(temp[0][2]) and temp[0][2] not in amicables.keys():
				temp += [fact_brute(temp[0][2])]
				if temp[0][0] == temp[1][2] and temp[1][0] == temp[0][2] and temp[0][2] != temp[1][2]: 
					#print(c_temp, temp[1][2])
					amicables.update({temp[0][0]:temp[0][1],temp[1][0]:temp[1][1]})
					print(str(temp[0]) + '\n' + str(temp[1]))


	return amicables

