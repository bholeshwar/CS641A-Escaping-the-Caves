import des_3round

k = ['0', '1', '0', '0', '1', '0', '1', None, '1', '1', '0', '0', '1', '0', '0', None, '1', '0', None, '1', '0', None, '1', None, '0', None, '1', '0', '0', '1', '0', None, '1', '0', '0', '1', '1', '1', '1', None, '1', '1', '0', '0', None, None, '0', None, '0', '0', '0', None, '1', '1', None, None, None, '1', '0', '0', '0', '1', '0', None]

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

def decimalToBinary(n, bits):
    return bin(n).replace("0b", "").zfill(bits)

def Permutation(listforPermutation, permutationList, numberofbits):
	elementsAfterPerm = [None]*numberofbits
	for i in xrange(0,numberofbits):
		index = permutationList[i]
		elementsAfterPerm[i] = listforPermutation[index-1]
	return elementsAfterPerm

#method to do the keyScheduling to get the round key
def getroundKey(key,roundNumber):
	
	#applying the pc1 permutation
	# pc1key = Permutation(key, pc1,56)
	pc1key = key[:]
		#circular left shift each half once for i up to the round number but double shift all except 1,2,9 and 16
	for k in xrange(1,roundNumber+1):
		temp = pc1key[0]
		for i in xrange(0,28):
			pc1key[i] = pc1key[i+1]
		pc1key[27]=temp
		temp = pc1key[28]
		for i in xrange(28,55):
			pc1key[i]=pc1key[i+1]
		pc1key[55] = temp
		if k == 1 or k == 2 or k == 9 or k == 16 :
			continue
		temp = pc1key[0]
		for i in xrange(0,28):
			pc1key[i] = pc1key[i+1]
		pc1key[27]=temp
		temp = pc1key[28]
		for i in xrange(28,55):
			pc1key[i]=pc1key[i+1]
		pc1key[55] = temp

	#applying pc2 permutation
	pc2key = Permutation(pc1key,pc2,48)
	return pc2key



pc1key = Permutation(k ,pc1, 56)

# k1 = getroundKey(pc1key, 1)
# k2 = getroundKey(pc1key, 2)
# k3 = getroundKey(pc1key, 3)

# print (pc1key)
# print (k1)
# print (k2)
# print (k3)

key_ind = []

for i in range(56):
    if pc1key[i] == None:
        key_ind.append(i)

# print (key_ind)

f1 = open("random_inputs.txt", "r")
f2 = open("outputs_after_IP_swap.txt", "r")

inputs = []
outputs = []

for j in range(20):
    inputs.append(f1.readline().rstrip())
    outputs.append(f2.readline().rstrip())


# print(inputs)
# print(outputs)

keys = []
correct_key = [None]*56

for j in range(2**8):
    key_probable_bits = decimalToBinary(j, 8)
    # print pc1key

    for k in range(8):
        pc1key[key_ind[k]] = key_probable_bits[k]

    # print pc1key

    k1 = getroundKey(pc1key, 1)
    k2 = getroundKey(pc1key, 2)
    k3 = getroundKey(pc1key, 3)

    # print pc1key

    # print k1
    # print k2
    # print k3

    flag = 0

    for i in range(20):
        if(des_3round.des(inputs[i], k1, k2, k3) == outputs[i]):
            # print ("YAAAAAY")
            flag = 1
        else:
            flag = 0
            break

    # print ("-----------")

    if (flag == 1):
        print (pc1key)
        correct_key = pc1key[:]
    

print (correct_key)