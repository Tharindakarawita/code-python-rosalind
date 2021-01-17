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

DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_lcsm (1).txt", "r")
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
    Fasta_seqs = list(Fasta_dict.values())
    return Fasta_seqs

Substring = []
for Fasta_seq_num in range(0,len(dict_mk())):
    Fasta_seq = dict_mk()[Fasta_seq_num]
    Substring.append([])
    for n in range(0,len(Fasta_seq)):
        for i in range(0,len(Fasta_seq)):
            if (i+n+2) - (0+i) == len(Fasta_seq[0+i:i+n+2]):
                Substring[Fasta_seq_num].append(Fasta_seq[0+i:i+n+2])


ls = [set(l) for l in Substring]

exec_string = "ls[{}]"
string = ""
for seq in range(0,len(Substring)):
    string += exec_string.format(seq) + " & "

string = "print(max("+string[0:len(string)-3]+",key=len))"
exec(string)
