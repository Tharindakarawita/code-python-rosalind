from numpy import *
DNA_1 = open("C:/Users/Tharinda Karawita/Downloads/rosalind_cons.txt", "r")
DNA = DNA_1.readlines()
a = zeros(8,dtype=int64)
t = zeros(8,dtype=int64)
g = zeros(8,dtype=int64)
c = zeros(8,dtype=int64)
Fasta_label = ""
Consensus_seq = []
Fasta_dict = {}
label = ""
for line in DNA:
    line = line.rstrip()
    if line.startswith(">"):
      Fasta_label = line[1:] 
      Fasta_dict[Fasta_label] =""
    else:
      Fasta_dict[Fasta_label] += line
DNA_seq= list(Fasta_dict.values())
i = len(list(Fasta_dict.values())[0])

a = zeros(i,dtype=int64)
t = zeros(i,dtype=int64)
g = zeros(i,dtype=int64)
c = zeros(i,dtype=int64)

for one_sequence in DNA_seq:      
    A = array([],dtype=int64)
    T = array([],dtype=int64)
    G = array([],dtype=int64) 
    C = array([],dtype=int64)
    for base in one_sequence:
        if base == "A":
            A = append(A,1,axis=None)
            C = append(C,0,axis=None)
            T = append(T,0,axis=None)
            G = append(G,0,axis=None)
        elif base == "T":
            T = append(T,1,axis=None)
            C = append(C,0,axis=None)
            A = append(A,0,axis=None)
            G = append(G,0,axis=None)
        elif base == "C":
            C = append(C,1,axis=None)
            A = append(A,0,axis=None)
            T = append(T,0,axis=None)
            G = append(G,0,axis=None)
        elif base == "G":
            G = append(G,1,axis=None)
            C = append(C,0,axis=None)
            T = append(T,0,axis=None)
            A = append(A,0,axis=None)
    a = A + a
    t = T + t
    g = G + g
    c = C + c

def Consensus():
    for point in range(i):
        if max(a[point],c[point],g[point],t[point]) == a[point]:
            Consensus_seq.append("A")
        elif max(a[point],c[point],g[point],t[point]) == c[point]:
            Consensus_seq.append("C")
        elif max(a[point],c[point],g[point],t[point]) == g[point]:
            Consensus_seq.append("G")
        elif max(a[point],c[point],g[point],t[point]) == t[point]:
            Consensus_seq.append("T")
    return (''.join(Consensus_seq))
print(Consensus())
print("A:",*a)
print("C:",*c)
print("G:",*g)
print("T:",*t)

