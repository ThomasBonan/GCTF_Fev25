
# Enoncé
cipher_tab_1 = [445009065, 549798567, 144418091, 451003240, 580134070, 678402995, 919363569, 786611290, 892141306, 747211718, 766430021, 121657850, 940376888, 892141306, 766430021, 689294036, 49933161, 872013481, 892141306, 766430021, 878789496, 711414238, 71936969, 155230051, 123204028, 155230051, 940376888, 100126390, 569566296]
cipher_tab_2 = [941918574, 430269109, 790633154, 422601387, 303117009, 898407447, 582690174, 243821318, 712431482, 891174166, 717705518, 729489304, 213668217, 712431482, 717705518, 349060439, 922301846, 905429366, 712431482, 717705518, 209399456, 585977533, 149980147, 130251232, 275409216, 130251232, 213668217, 575226018, 419515814]

pub_key_1 = (952169509, 23)
pub_key_2 = (952169509, 31)


# On récupère N dans les clefs publiques, ainsi que e1 et e2
N = 952169509
e1 = 23
e2 = 31

# On trouve x et y en résolvant e1*x+e2*y=1
x = -4
y = 3

# On trouve D pour transformer la puissance négative en positive
D = []

for i in range (len(cipher_tab_1)):
    D.append(pow(cipher_tab_1[i], -1, N))


# On déchiffre les caractère un à un
temp = []

for j in range (len(cipher_tab_2)):
    temp.append((pow(D[j],4)*pow(cipher_tab_2[j],3))%N)


# On reconstruit le flag
flag = ''

for k in range(len(temp)):
    flag += chr(temp[k])

print(flag)