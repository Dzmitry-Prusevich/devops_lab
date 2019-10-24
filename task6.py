num_m = int(input("Enter number of elements in set M: "))
space_m = str(input("Enter {0} elements in set M: ".format(num_m)))
m_elem = set(map(int, space_m.split()))
num_n = int(input("Enter number of elements in set N: "))
space_n = str(input("Enter {0} elements in set N: ".format(num_n)))
n_elem = set(map(int, space_n.split()))
dif_elem = n_elem ^ m_elem
list_dif = list(sorted(dif_elem))
for i in range(len(list_dif)):
    print(list_dif[i])
