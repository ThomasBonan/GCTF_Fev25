
# Création du tableau de nombre pour le chiffrement
flag = "GCTF{N3veR_U2e_S@me_M0dulu2!}"
tab = []
cipher_tab_1 = []
cipher_tab_2 = []

for i in range (len(flag)):
    tab.append(ord(flag[i]))


# Définissions des variables RSA
p = 28879
q = 32971
N = p*q
phi_N = (p-1)*(q-1)

e1 = 23
e2 = 31
print(N)

pub_key_1 = (N, e1)
pub_key_2 = (N, e2)

# Chiffrement de la chaine de caractère avec 2 exposant différents mais le même modulo
for i in range(len(tab)):
    tmp = tab[i]
    cipher_tab_1.append(pow(tmp, e1, N))
    cipher_tab_2.append(pow(tmp, e2, N))

print(cipher_tab_1)
print(cipher_tab_2)