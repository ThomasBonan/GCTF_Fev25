cipher_tab = [17462, 9122, 14541, 12651, 17372, 25012, 33058, 1314, 16165, 14504, 22617, 16165, 4360, 16196, 13802, 3376, 12290, 16165, 12651, 16196, 9883, 902, 28581]
public_key = (35953, 257)
tab = []
flag = ''

# On utiliser le site : https://www.dcode.fr/decomposition-nombres-premiers
# Pour factoriser N et retrouver p et q

e = 257
N = 35953
p = 157
q = 229
phi_N = (p-1)*(q-1) 

d = pow(e, -1, phi_N)

for i in range (len(cipher_tab)):
    tmp = cipher_tab[i]
    tab.append(pow(tmp, d, N))


for j in range (len(tab)):
    flag += chr(tab[j])

print(flag)

