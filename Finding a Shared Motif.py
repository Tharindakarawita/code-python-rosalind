"""Problem"""
#  A common substring of a collection of strings is a substring of every member of the
#  collection. We say that a common substring is a longest common substring if there does
#  not exist a longer common substring. For example, "CG" is a common substring of
#  "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case,
#  "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for a simple example,
#  "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist,
# you may return any single solution.)

# Sample Dataset
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA

# Sample Output
# AC


from statistics import mode 
DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_lcsm.txt", "r")
Fasta_dict = {}
Fasta_label = ""
DNA = DNA.readlines()
def dict_mk():
    for line in DNA:
        line = line.rstrip()
        if line.startswith(">"):
            Fasta_label = line[1:] 
            Fasta_dict[Fasta_label] =""
        else:
            Fasta_dict[Fasta_label] += line
    return Fasta_dict

Fasta_seq = list(dict_mk().values())
seq = []
for n in range(0,len(Fasta_seq)):
    print(Fasta_seq[n])
    for m in range(0,len(Fasta_seq[n])):
        for i in range(0,len(Fasta_seq[n])):
            seq1 = Fasta_seq[n][0+i:2+i+m]
#            print(Fasta_seq[n][-2-i:0-i])
            if (2+i+m) - (0+i) == len(seq1):
#                print(seq1)
                for b in range(0,len(Fasta_seq)):
                    if not n == b:
                            for c in range(0,len(Fasta_seq[b])):
                                for a in range(0,len(Fasta_seq[b])):
                                    seq2 = Fasta_seq[b][0+a:2+a+c]
                                    if (2+a+c) - (0+a) == len(seq2):
                                        if seq1 == seq2:
                                            print(seq1)
                                            seq.append(seq1)

print(seq)
longest_seq = []
num = seq[0] 
#print(seq)
for r in seq: 
    curr_frequency = seq.count(r) 
    if curr_frequency >= (len(Fasta_seq))*2: #2 is wrong / there must be same seq in the same string 
        longest_seq.append(r)

print(max(longest_seq,key=len))



        


