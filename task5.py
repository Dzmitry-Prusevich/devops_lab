# ENTER MOVING OF ROBOT
move = list(input("ENTER MOVING STEPS OF ROBOT: "))
in_hor_pos = 0
in_ver_pos = 0
hor_pos = 0
ver_pos = 0
# making moves
for i in move:
    if i == "R":
        hor_pos += 1
    elif i == "L":
        hor_pos -= 1
    elif i == "D":
        ver_pos -= 1
    elif i == "U":
        ver_pos += 1
# compare results
print(hor_pos == in_hor_pos and ver_pos == in_ver_pos)

