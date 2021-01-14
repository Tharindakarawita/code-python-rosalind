# RNA Splicing

# Problem
# After identifying the exons and introns of an RNA string, we only need to delete the 
# introns and concatenate the exons to form a new string ready for translation.

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s 
# acting as introns. All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. 
# (Note: Only one solution will exist for the dataset provided.)

# Sample Dataset

# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT

# Sample Output

# MVYIADKQHVASREAYGHMFKVCA


map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_gc.txt", "r").readlines()
Fasta_dict = {}
Fasta_label = ""
def dict_mk():
    for line in DNA:
        line = line.rstrip()
        if line.startswith(">"):
            Fasta_label = line[1:] 
            Fasta_dict[Fasta_label] =""
        else:
            Fasta_dict[Fasta_label] += line
    Main_seq = list(Fasta_dict.values())[0]
    substring = list(Fasta_dict.values())[1:]
    return Main_seq,substring


def motif(Main_seq = dict_mk()[0],substring = dict_mk()[1]):
    exon_seq = Main_seq
    for singal_substring in substring:
        y = len(singal_substring)
        for i in range(0,len(Main_seq)):
            x = exon_seq.find(singal_substring,i,i+y)
            if x != -1:
                exon_seq = exon_seq[:x]+ exon_seq[x+y:]
    exon_seq = exon_seq.replace("T","U")
    return exon_seq

def RNA_Translation():
    AA_seq = ""
    for i in range(0,len(motif()),3):
        codon = motif()[i:i+3]
        AA = map.get(codon)
        AA = str(AA)
        if AA == "STOP":
            pass
        else:
            AA_seq += AA
    return print(AA_seq)


RNA_Translation()

