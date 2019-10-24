# enter size
size = str(input("Enter size (odd numbers) of your door mate (N*M): "))
size_n = size.split()
n = int(size_n[0])
m = int(size_n[1])
raw_doors = []
# making raws for finish result
for i in range(n):
    raw_doors.append("")
# filling raws with elements before middle raw
for i in range(n // 2):
    col_dot = i + 1
    for y in range((m // 2 - (i + 1) - i * 2)):
        raw_doors[i] += "-"
    raw_doors[i] += "."
    for y in range(i):
        raw_doors[i] += "|.."
    raw_doors[i] += "|"
    for y in range(i):
        raw_doors[i] += "..|"
    raw_doors[i] += "."
    for y in range((m // 2 - (i + 1) - i * 2)):
        raw_doors[i] += "-"
# making middle raw
for i in range(m // 2 - 3):
    raw_doors[n // 2] += "-"
raw_doors[n // 2] += "WELCOME"
for i in range(m // 2 - 3):
    raw_doors[n // 2] += "-"
# filling raws with elements after middle raw
for i in range(n // 2):
    col_dot = n // 2 + 1
    raw_doors[col_dot + i] += raw_doors[col_dot - 2 - i]
for i in range(n):
    print(raw_doors[i])
