
# Création du tableau de nombre pour le chiffrement
flag = "GCTF{N3ver_G1ve_Y0ur_SuM}"
tab = []
cipher_tab = []

for i in range (len(flag)):
    tab.append(ord(flag[i]))

print(tab)

# Choix des valeurs pour le RSA
p = 100003831
q = 1000001161
e = 65537

# Calcul des clefs privées et publiques ainsi que du coefficient d'euleur phi_N
phi_N = (p-1)*(q-1)
N = p*q
d = pow(e, -1, phi_N)

public_key = (e,N)
private_key = (d,N)
print(public_key)

# Définition de la somme des valeurs de départ 
x = p+q
print(x)


# Chiffrement
for i in range(len(tab)):
    tmp = tab[i]
    cipher_tab.append(pow(tmp, e, N))

print(cipher_tab)