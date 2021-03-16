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

# ------Version 1.0---------


# DNA = open("C:/Users/nayan/Desktop/new 7.txt", "r")
# Fasta_dict = {}
# Fasta_label = ""
# DNA = DNA.readlines()
# def dict_mk():
#     for line in DNA:
#         line = line.rstrip()
#         if line.startswith(">"):
#             Fasta_label = line[1:] 
#             Fasta_dict[Fasta_label] =""
#         else:
#             Fasta_dict[Fasta_label] += line
#     Fasta_seqs = list(Fasta_dict.values())
#     return Fasta_seqs

# Substring = []
# for Fasta_seq_num in range(0,len(dict_mk())):
#     Fasta_seq = dict_mk()[Fasta_seq_num]
#     Substring.append([])
#     for n in range(0,len(Fasta_seq)):
#         for i in range(0,len(Fasta_seq)):
#             if (i+n+200) - (0+i) == len(Fasta_seq[0+i:i+n+200]):
#                 Substring[Fasta_seq_num].append(Fasta_seq[0+i:i+n+200])

# for o in Substring:
#     for p in o:
#         print(p)
# # ls = [set(l) for l in Substring]

# # exec_string = "ls[{}]"
# # string = ""
# # for seq in range(0,len(Substring)):
# #     string += exec_string.format(seq) + " & "

# # string = "print(max("+string[0:len(string)-3]+",key=len))"
# # exec(string)



# # ------Version 2.0---------

# DNA = open("C:/Users/nayan/Downloads/rosalind_lcsm.txt", "r")

# Fasta_dict = {}
# Fasta_label = ""
# DNA = DNA.readlines()
# def dict_mk():
#     for line in DNA:
#         line = line.rstrip()
#         if line.startswith(">"):
#             Fasta_label = line[1:] 
#             Fasta_dict[Fasta_label] =""
#         else:
#             Fasta_dict[Fasta_label] += line
#     Fasta_seqs = list(Fasta_dict.values())
#     return Fasta_seqs

# def frist_string_separetion():
#     Substring = []
#     Frist_string = dict_mk()[0]
#     for n in range(0,len(Frist_string)):
#         for i in range(0,len(Frist_string)):
#             if (i+n+200) - (0+i) == len(Frist_string[0+i:i+200+n]):
#                 Substring.append(Frist_string[0+i:i+n+200])
#                 #print(Frist_string[0+i:i+n+2])
#     return Substring
                

# def motif(DNA,substring):
#     substring_location = []
#     y = len(substring)
#     for i in range(0,len(DNA)):
#         x = DNA.find(substring,i,i+y)
#         if x != -1:
#             substring_location.append(x+1)
#         else:
#             exit
#     if not substring_location:
#         substring_location = None
#     return substring_location



# generally_share_motif = []
# longest_string = ''
# for sami_sub in frist_string_separetion():
#     counter = 0
#     for Seq_num,Seq in enumerate(dict_mk()): 
#         if Seq_num == 0:
#             continue
#         if motif(Seq,sami_sub) is not None:
#             counter += 1
        
#             if counter == len(dict_mk())-1:
#                 generally_share_motif.append(sami_sub)
#                 #print(motif(Seq,sami_sub),sami_sub,Seq)
#                 if sami_sub>longest_string:
#                     longest_string = sami_sub
#                     print(longest_string)
        
# # print(max(generally_share_motif,key=len))





# # ------Version 3.0---------
from Bio import SeqIO


Fasta_seqs = []
#for record in SeqIO.parse("C:/Users/nayan/Desktop/new 7.txt", 'fasta'):
for record in SeqIO.parse("C:/Users/nayan/Downloads/rosalind_lcsm.txt", 'fasta'):
    Fasta_seqs.append(str(record.seq))
  


def frist_string_separetion():
    Substring = []
    Frist_string = Fasta_seqs[0]
    for n in range(0,len(Frist_string)):
        for i in range(0,len(Frist_string)):
            if (i+n+2) - (0+i) == len(Frist_string[0+i:i+2+n]):
                Substring.append(Frist_string[0+i:i+n+2])
    return Substring
                

print(len(frist_string_separetion()))
longest_string = ''
result = frist_string_separetion()
final_result = []
for sami_sub_num,sami_sub in enumerate(result):
    counter = 0
    for Seq_num,Seq in enumerate(Fasta_seqs): 
        if Seq_num == 0:
            continue
        if str(sami_sub) in str(Seq):
            counter += 1
            if counter == len(Fasta_seqs)-1:
                # print(sami_sub)
                if sami_sub not in final_result:
                    final_result.append(sami_sub)
                    #print(len(final_result))
                


print(max(final_result,key=len))