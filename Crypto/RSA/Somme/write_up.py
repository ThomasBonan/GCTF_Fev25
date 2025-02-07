from math import sqrt

# Enoncé
cipher_tab = [20329218722985707, 29459851268133393, 3591763105603898, 77239418497077983, 53221344948556210, 99743169128070354, 54666933477444813, 60409130069252897, 93884405116189774, 41844744275367750, 91141560120508692, 20329218722985707, 82516170560535321, 60409130069252897, 93884405116189774, 91141560120508692, 60000019218853281, 2727427429250995, 95466833169611685, 41844744275367750, 91141560120508692, 71874701747638626, 95466833169611685, 33179960548823333, 37376380876012707]
pub_key = (65537, 100003947104447791)
sum = 1100004992

# Valeurs récupérées
e = 65537
N = 100003947104447791

# On résous l'équation du second odre "-q^2 + x * q - n = 0"
delta = pow(sum,2)-(((4)*(-1))*(-N))

# On trouve les 2 racines du discriminants
p = int(((-1*sum)+sqrt(delta))/(-2))
q = int(((-1*sum)-sqrt(delta))/(-2))


# On refait un calcul RSA classique
phi_N = (p-1)*(q-1)
d = pow(e, -1, phi_N)


# On déchiffre la liste
temp = []

for i in range(len(cipher_tab)):
    tmp = cipher_tab[i]
    temp.append(pow(tmp, d, N))

# On reconstruit le flag
flag = ''

for j in range(len(temp)):
    flag += chr(temp[j])

print(flag)