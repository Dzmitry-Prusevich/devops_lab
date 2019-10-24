# enter your number
n = int(input("Enter number for calculate factorial: "))
fact = 1
for i in range(n):
    fact *= (i + 1)
print("{0}! = {1}".format(n, fact))
