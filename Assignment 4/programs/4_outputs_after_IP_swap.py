# Changing to chars

def to_bits(s):
    to_bits_dict = {"f": "0000", "g": "0001", "h": "0010", "i": "0011", "j": "0100", "k": "0101","l":"0110", "m":"0111","n": "1000","o": "1001", "p": "1010","q":"1011","r":"1100","s":"1101","t":"1110","u": "1111"}

    t = ""
    for i in s:
        if i=='\n':
            break
        t += to_bits_dict[i] 

    return t

f = open("generated_outputs.txt", 'r')
content = []

with f:
    content = f.readlines()

outputs_bits = []

for i in content:
    outputs_bits.append(to_bits(i))


# Applying IP

ip = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]


outputs_bits_after_IP = []

for o in outputs_bits:
    ans = ""

    for i in range(64):
        ans += o[ip[i]-1]

    outputs_bits_after_IP.append(ans)


# Swapping L & R

outputs_bits_after_IP_after_swap = []

for i in outputs_bits_after_IP:
    ans = ""

    ans += i[32:64]
    ans += i[0:32]

    outputs_bits_after_IP_after_swap.append(ans)

for i in outputs_bits_after_IP_after_swap:
    print i