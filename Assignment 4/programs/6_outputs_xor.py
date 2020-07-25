def xor_(s, t):
    ans = ""
    
    for i in range(len(s)):
        if s[i] == t[i]:
            ans += "0"
        else:
            ans += "1"
    
    return ans


f = open("outputs_after_IP_swap.txt", "r")

outputs_xor = []

for i in range(10):
    p1 = f.readline().rstrip()
    p2 = f.readline().rstrip()
    
    outputs_xor.append(xor_(p1, p2))

f.close()

for i in outputs_xor:
    print (i)