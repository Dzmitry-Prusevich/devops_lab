def input_m(space_m):
    m_elem = set(map(int, space_m.split()))
    return m_elem


def input_n(space_n):
    n_elem = set(map(int, space_n.split()))
    return n_elem


def listdif(dif_elem):
    list_dif = list(sorted(dif_elem))
    for i in range(len(list_dif)):
        print(list_dif[i])
    return list_dif


def input_num_m():
    num_m = int(input("Enter number of elements in set M: "))
    return num_m


def input_num_n():
    num_n = int(input("Enter number of elements in set N: "))
    return num_n


if __name__ == '__main__':
    space_m = input("Enter {0} elements in set M: ".format(input_num_m()))
    m_elem = input_m(space_m)
    space_n = input("Enter {0} elements in set N: ".format(input_num_n()))
    n_elem = input_n(space_n)
    dif_elem = n_elem ^ m_elem
    listdif(dif_elem)
