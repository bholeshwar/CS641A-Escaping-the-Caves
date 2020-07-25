pc1 = [57,49,41,33,25,17,9,
       1,58,50,42,34,26,18,
       10,2,59,51,43,35,27,
       19,11,3,60,52,44,36,
       63,55,47,39,31,23,15,
       7,62,54,46,38,30,22,
       14,6,61,53,45,37,29,
       21,13,5,28,20,12,4]

pc2 = [14,17,11,24,1,5,
       3,28,15,6,21,10,
       23,19,12,4,26,8,
       16,7,27,20,13,2,
       41,52,31,37,47,55,
       30,40,51,45,33,48,
       44,49,39,56,34,53,
       46,42,50,36,29,32]


def Permutation(listforPermutation, permutationList, numberofbits):
	elementsAfterPerm = [None]*numberofbits
	for i in xrange(0,numberofbits):
		index = permutationList[i]
		elementsAfterPerm[i] = listforPermutation[index-1]
	return elementsAfterPerm

#function to do the inversePermutation
def inversePermutation(functionoutput, permutationList, numberofbits):
	elementsAfterInversePerm = [None]*numberofbits
	i = 0
	for value in permutationList:
		if(functionoutput[i] != None):
			elementsAfterInversePerm[value-1] = functionoutput[i]
		i = i + 1
	return elementsAfterInversePerm

def rightshift(s):
	s_shifted = [None]*56
	s_shifted[0]=s[27]
	for i in xrange(0,28):
		s_shifted[i+1] = s[i]	
	s_shifted[28]=s[55]
	for j in xrange(28,55):
		s_shifted[j+1] = s[j]
	return s_shifted

def reverseKeyScheduling(key):
	
	#applying the reverse permutation on PC2
	pc2_inverse_key = inversePermutation(key, pc2, 56)
	#key is shifted 4 times for generating 3rd round key
	for x in xrange(0,4):
		rightshiftedKey = rightshift(pc2_inverse_key)
		pc2_inverse_key = rightshiftedKey
		
	#applying the reverse permutation on PC1
	pc1_inverse_key = inversePermutation(rightshiftedKey, pc1, 64)
	return pc1_inverse_key



k3 = "011101110000001000011001000110100011100110011101"
key = reverseKeyScheduling(k3)


print (key)