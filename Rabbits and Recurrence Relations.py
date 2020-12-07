x = [1,1]
for o in range(0,21):
    l = x[o]+x[o+1]
    x.append(l)
print(x)
#28 5  not 71
#29 2  not 64
#5 3 for 19
F1 = 1
F2 = 1
z =[1,1]
for i in range(1,50):
    y = F1 + F2*4
    F2 = F1
    F1 = y
    z.append(y)
print(z[34])
