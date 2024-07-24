
i = 1
while i< n:
	newArr = list(oldArr)
	for j in range(len(oldArr)-1,-1,-1):
		newArr.append((2**i)+oldArr[j])
	oldArr = newArr
	i+=1
return oldArr
