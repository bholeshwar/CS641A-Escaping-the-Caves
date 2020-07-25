import binascii

# This function solves for the small roots of polynomial
def solve(padding, e, c, n):
    ZmodN = Zmod(n) # mod n field
    e = ZmodN(e)
    c = ZmodN(c)
    p = ZmodN(padding)
    P.<x> = PolynomialRing(ZmodN)
    f_x = (p + x)^e - c
    f_x = f_x.monic()
    x0 = f_x.small_roots() # small roots of f_x

    return x0

# Given RSA values
e = 5
c = 58851190819355714547275899558441715663746139847246075619270745338657007055698378740637742775361768899700888858087050662614318305443064448898026503556757610342938490741361643696285051867260278567896991927351964557374977619644763633229896668511752432222528159214013173319855645351619393871433455550581741643299
n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093

# Padding
p = "This door has RSA encryption with exponent 5 and the password is "

# Iterating over possible length of password: 0 bytes to 25 bytes
for x0_length in range(0, 25):
    p_hex = binascii.hexlify(p)
    p_int = int(p_hex, 16)
    roots = solve(p_int, e, c, n)
    if(len(roots) != 0):
        break # We have found the password
    else:
        p = p + '\x00' # Left shifting the padding by 1 byte

ans = Integer(roots[0])
ans_hex = hex(ans)
print binascii.unhexlify(ans_hex)









