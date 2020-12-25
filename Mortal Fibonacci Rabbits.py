def mortal_rabbits(n,m): # n = position of the sequence / m = rabbit pair life from mounth
    Adult = [0,1]
    Died =  []
    amaturer = [1]
    seq = [1]
    for k in range(0,m):
        Died.append(0)
    for i in range(0,n):
        amaturer.append(Adult[i])
        seq.append(Adult[i+1]+amaturer[i+1])
        Adult.append(seq[i+1]-Died[i+2])
        Died.append(amaturer[i])
    return print(seq[n-1])


mortal_rabbits(99,17)

