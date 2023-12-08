a1 = [121, 144, 19, 161, 19, 144, 19, 11,-1]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19,1]

a1.sort()
a2.sort()

if len(a1) == len(a2):
    lenght_list = len(a1)
else:
    print(False)

for position in range(lenght_list):
    if a1[position] ** 2 == a2[position]:
        print("Funciona")
    else:
        print(False)
print(True)
