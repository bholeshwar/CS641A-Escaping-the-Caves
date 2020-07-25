def xor_(s, t):
    ans = ""
    
    for i in range(len(s)):
        if s[i] == t[i]:
            ans += "0"
        else:
            ans += "1"
    
    return ans


f = open("random_inputs.txt", "r")

inputs_xor = []

for i in range(10):
    p1 = f.readline().rstrip()
    p2 = f.readline().rstrip()
    
    inputs_xor.append(xor_(p1, p2))

f.close()

for i in inputs_xor:
    print (i)