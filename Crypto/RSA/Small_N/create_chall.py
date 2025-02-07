
# Création du tableau de nombre pour le chiffrement
flag = "GCTF{RS@_Is_Qu1t3_FuN!}"
tab = []
cipher_tab = []

for i in range (len(flag)):
    tab.append(ord(flag[i]))

print(tab)


# Choix des valeurs pour le RSA
p = 157
q = 229
e = 257

# Calcul des clefs privées et publiques ainsi que du coefficient d'euleur phi_N

phi_N = (p-1)*(q-1)
N = p*q
d = pow(e, -1, phi_N)

public_key = (e,N)
private_key = (d,N)

print(d)

# Chiffrement avec des nombres faibles de départ

for i in range(len(tab)):
    tmp = tab[i]
    cipher_tab.append(pow(tmp, e, N))

print(cipher_tab)