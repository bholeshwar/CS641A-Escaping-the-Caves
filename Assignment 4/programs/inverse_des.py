import des_3round

des_key = ['1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0']

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

# To change output to bits
def to_bits(s):
    to_bits_dict = {"f": "0000", "g": "0001", "h": "0010", "i": "0011", "j": "0100", "k": "0101","l":"0110", "m":"0111","n": "1000","o": "1001", "p": "1010","q":"1011","r":"1100","s":"1101","t":"1110","u": "1111"}

    t = ""
    for i in s:
        if i=='\n':
            break
        t += to_bits_dict[i] 

    return t


# To apply IP to output
def IP(s):
    ip = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]

    t = ""

    for i in range(64):
        t += s[ip[i]-1]

    return t


def IP_inv(s):
    ip_inverse = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

    t = ""

    for i in range(64):
        t += s[ip_inverse[i]-1]

    return t


def swap(s):
    # swap left and right parts
    return s[32:64] + s[0:32]

def to_char(s):
    to_letter = {"0000": "f", "0001": "g", "0010": "h", "0011": "i", "0100": "j", "0101": "k","0110":"l", "0111":"m","1000": "n","1001": "o", "1010": "p","1011":"q","1100":"r","1101":"s","1110":"t","1111": "u"}
    i = 0
    t = ""

    while i < 64:
        tmp = s[i:i+4]
        t += to_letter[tmp]
        i += 4

    return t

in0 = "hshjsijnrkptugsi"

in0 = to_bits(in0)
in0 = IP(in0)

k1 = getroundKey(des_key, 1)
k2 = getroundKey(des_key, 2)
k3 = getroundKey(des_key, 3)

out0 = des_3round.des(in0, k3, k2, k1)

out0 = swap(out0)
out0 = IP_inv(out0)
out0 = to_char(out0)

in1 = "fifnluhuphpkpqnm"

in1 = to_bits(in1)
in1 = IP(in1)

out1 = des_3round.des(in1, k3, k2, k1)

out1 = swap(out1)
out1 = IP_inv(out1)
out1 = to_char(out1)

out = out0 + out1

print ("The password for the round is " + out)