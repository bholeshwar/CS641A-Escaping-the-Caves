def decimalToBinary(n, bits):
    return bin(n).replace("0b", "").zfill(bits)

def xor_(s, t):
    ans = ""
    
    for i in range(len(s)):
        if s[i] == t[i]:
            ans += "0"
        else:
            ans += "1"
    
    return ans

def sbox(s, sbox_no):
    # s is 6-bit input to the s-box sbox_no

    s_box = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0],
        [15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13]],
    
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9]],
    
    [[10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
    [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    
    [[12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ]
        
    ans = ""
    
    out = s_box[sbox_no][(2*int(s[0])+int(s[5]))][(8*int(s[1])+4*int(s[2])+2*int(s[3])+int(s[4]))]
    ans += decimalToBinary(out, 4)

    return ans


def expansion(s):
    expand = [32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1]

    ans = ""
    for i in range(48):
        ans += s[expand[i]-1]

    return ans


def permute(s):
    p = [16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25]

    ans = ""
    for i in range(32):
        ans += s[p[i]-1]
    
    return ans


def inv_permute(s):
    ip =[9,17,23,31,13,28,2,18,24,
    16,30,6,26,20,10,1,8,14,25,3,4,
    29,11,19,32,12,22,7,5,27,15,21]

    ans = ""
    for i in range(32):
        ans += s[ip[i]-1]

    return ans


f1 = open("outputs_after_IP_swap.txt", "r")
f2 = open("outputs_xor.txt", "r")
f3 = open("inputs_xor.txt", "r")


set1 = [set() for _ in range(10)]
set2 = [set() for _ in range(10)]
set3 = [set() for _ in range(10)]
set4 = [set() for _ in range(10)]
set5 = [set() for _ in range(10)]
set6 = [set() for _ in range(10)]
set7 = [set() for _ in range(10)]
set8 = [set() for _ in range(10)]

sets = [set1, set2, set3, set4, set5, set6, set7, set8]

for j in range(10):
    C1 = f1.readline().rstrip()
    C2 = f1.readline().rstrip()
    C_xor = f2.readline().rstrip()
    P_xor = f3.readline().rstrip()

    R3_xor = C_xor[32:64]
    L3_xor = C_xor[0:32]
    L0_xor = P_xor[0:32]

    L3_1 = expansion(C1[0:32])
    L3_2 = expansion(C2[0:32])
    R2_1 = L3_1
    R2_2 = L3_2
    
    R3_xor = xor_(R3_xor, L0_xor)

    R2_xor = expansion(L3_xor)
    R3_xor = inv_permute(R3_xor)

    in_ind = 0
    out_ind = 0
    
    for i in range(8):
        input_xor = R2_xor[in_ind:in_ind+6]
        output_xor = R3_xor[out_ind:out_ind+4]

        a1 = R2_1[in_ind:in_ind+6]
        a2 = R2_2[out_ind:out_ind+6]
        
        for k in range(64):
            i1 = decimalToBinary(k, 6)
            i2 = xor_(i1, input_xor)

            sbox_i1 = sbox(i1, i)
            sbox_i2 = sbox(i2, i)
            
            if xor_(sbox_i1,sbox_i2) == output_xor:
                k1 = xor_(i1, a1)
                k2 = xor_(i2, a2)
                k3 = xor_(i1, a2)
                k4 = xor_(i2, a1)
                sets[i][j].add(k1)
                sets[i][j].add(k2)
                sets[i][j].add(k3)
                sets[i][j].add(k4)

        in_ind += 6
        out_ind += 4



k3 = ""

for i in range(8):
    ans = set.intersection(*sets[i])

    for x in ans:
        k3 += x

print "The key k3 is", k3

f1.close()
f2.close()
f3.close()