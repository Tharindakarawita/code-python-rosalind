import itertools

DNA = open("D:/trash/rosalind_lexf.txt", "r")
line1 = DNA.readlines()
letters = line1[0].replace(' ','').strip()
n = int(line1[1])



perm = itertools.product(letters, repeat = n)


def ttos(tup):
    new_string = ''
    for i in tup:
        new_string += i
    return new_string




output = ''
for n in perm:
    print(ttos(n))
    