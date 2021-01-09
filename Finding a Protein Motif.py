


from pprint import pprint
import urllib.request
from itertools import product

from numpy.core.fromnumeric import sort

Protein_Motif = "N{P}[ST]{P}"  #N{P}[ST]{P}
iterable = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]




DNA = urllib.request.urlopen("https://www.uniprot.org/uniprot/B5ZC00.fasta").readlines()
Fasta_dict = {}
Fasta_label = ""


def dict_mk():
    for line in DNA:
        line = line.rstrip().decode("utf-8")
        if line.startswith(">"):
            Fasta_label = line[1:] 
            Fasta_dict[Fasta_label] =""
        else:
            Fasta_dict[Fasta_label] += line
    fasta_seq = list(Fasta_dict.values())
    SEQ = fasta_seq[0]
    return SEQ

# def protein_shift_position():
#     motif_list = ["N{0}S{1}","N{0}T{1}"]
#     return motif_list
# protein_shift_position()

# def protein_shift_position():
#     string = Protein_Motif
#     position_c = 0
#     for n in range(0,len(Protein_Motif)):
#         x = Protein_Motif.find("{",n,n+1)
#         if x != -1:
#             string = string[:x+1] + str(position_C) + string[x+2:]
#             position_c += 1
#     return string

def shifting_varible():
    AA_except = []
    for n in range(0,len(Protein_Motif)):
        if Protein_Motif[n] == "{":
            for AA in iterable:
                if AA == Protein_Motif[n+1]:
                    AA_except.append(AA)   
    return AA_except

def create_motif():
    removeable = []
    all_comb =[]
    substring = []
    for comb in product(iterable,repeat = len(shifting_varible())):
        all_comb.append(comb)
        for index,data in enumerate(zip(shifting_varible(), comb)):
            if data[0] == data[1]:
                removeable.append(comb)
        
    for re in all_comb:
        if re not in removeable:
            substring.append("N{0}S{1}".format(re[0],re[1])) #more / substring.append(protein_shift_position().format(re[0],re[1]))
            substring.append("N{0}T{1}".format(re[0],re[1]))
    return substring
    

def protein_motif(substring,SEQ):
    y = len(substring[0])
    protein_motif = []
    for singal in substring:
        for i in range(0,len(SEQ)):
            x = int(SEQ.find(singal,i,i+y))
            if x != -1:
                protein_motif.append(x+1)
            else:
                exit
    protein_motif = sort(protein_motif)
    return print(" ".join(map(str, protein_motif)))



protein_motif(create_motif(),dict_mk())



      






