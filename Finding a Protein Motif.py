# Finding a Protein Motif

# Problem
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

# http://www.uniprot.org/uniprot/uniprot_id
# Alternatively, you can obtain a protein sequence in FASTA format by following

# http://www.uniprot.org/uniprot/uniprot_id.fasta
# For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

# Given: At most 15 UniProt Protein Database access IDs.

# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

# Sample Dataset

# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST

# Sample Output

# B5ZC00
# 85 118 142 306 395
# P07204_TRBM_HUMAN
# 47 115 116 382 409
# P20840_SAG1_YEAST
# 79 109 135 248 306 348 364 402 485 501 614



import urllib.request
from itertools import product

from numpy.core.fromnumeric import sort

Protein_Motif = "N{P}[ST]{P}"  #N{P}[ST]{P}
iterable = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]

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
    return Fasta_dict



Protein_motif_ID = open("C:/Users/Tharinda Karawita/Downloads/rosalind_mprt (2).txt", "r").readlines()
Protein_motif_ID_list = []
for line in Protein_motif_ID:
    line = line.rstrip()
    Protein_motif_ID_list.append(line)
for ID in Protein_motif_ID_list:
    DNA = urllib.request.urlopen("https://www.uniprot.org/uniprot/"+ID+".fasta").readlines()
    #print(DNA)
    dict_mk()


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

def SEQ():
    for sequence_position in range(0,len(list(Fasta_dict.keys()))):
        key = Protein_motif_ID_list[sequence_position]
        motif = protein_motif(create_motif(),list(Fasta_dict.values())[sequence_position]) 
        if not len(motif) == 0:
            print(key)
            print(" ".join(map(str,motif)))

    return
    
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
        # op = sort(protein_motif)
        # res = str(op)[1:-1] 
    protein_motif = sort(protein_motif)
    return protein_motif 
    




SEQ()

      






