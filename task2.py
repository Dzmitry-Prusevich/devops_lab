# enter list of keys keys
str_key = str(input("Enter list of keys, delimited with , : "))
list_key = str_key.replace(" ", "").split(",")
# enter list of keys values
str_val = str(input("Enter list of values, delimited with , : "))
list_val = str_val.replace(" ", "").split(",")
dict_fin = {}
for i in range(len(list_key)):
    if i < len(list_val):
        dict_fin[list_key[i]] = list_val[i]
    else:
        dict_fin[list_key[i]] = "None"
print(dict_fin)
