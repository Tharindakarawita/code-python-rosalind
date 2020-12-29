"""Problem"""
# A matrix is a rectangular table of values divided into rows and columns.
# An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,
# j to indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings, all having the same length n.
# Their profile matrix is a 4×n matrix P in which P1,j represents the number
# of times that 'A' occurs in the jth position of one of the strings, P2,j represents
# the number of times that C occurs in the jth position, and so on (see below).

# A consensus string c is a string of length n formed from our collection by taking
# the most common symbol at each position; the jth symbol of c therefore corresponds
# to the symbol having the maximum value in the j-th column of the profile matrix.
# Of course, there may be more than one most common symbol, leading to multiple 
# possible consensus strings.

#             A T C C A G C T
#             G G G C A A C T
#             A T G G A T C T
# DNA Strings	A A G C A A C C
#             T T G G A A C T
#             A T G C C A T T
#             A T G G C A C T

#             A   5 1 0 0 5 5 0 0
# Profile	    C   0 0 1 4 2 0 6 1
#             G   1 1 6 3 0 1 0 0
#             T   1 5 0 0 0 1 1 6
# Consensus	A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus 
#         strings exist, then you may return any one of them.)

# Sample Dataset
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Sample Output
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

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

