# Open Reading Frames solved 

# Problem
# Either strand of a DNA double helix can serve as the coding strand for RNA
# transcription. Hence, a given DNA string implies six total reading frames,
# or ways in which the same region of DNA can be translated into amino acids:
# three reading frames result from reading the string itself, whereas three more
# result from reading its reverse complement.

# An open reading frame (ORF) is one which starts from the start codon and ends by
# stop codon, without any other stop codons in between. Thus, a candidate protein
# string is derived by translating an open reading frame into amino acids until a
# stop codon is reached.

# Given: A DNA string s of length at most 1 kbp in FASTA format.

# Return: Every distinct candidate protein string that can be translated from ORFs
# of s. Strings can be returned in any order.

# Sample Dataset

# >Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

# Sample Output

# MLLGSFRLIPKETLIQVAGSSPCNLS
# M
# MGMTPRLGLESLLE
# MTPRLGLESLLE

DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_orf.txt", "r")
Fasta_dict = {}
Fasta_label = ""
aa_seq_list =[]
DNA = DNA.readlines()

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


def dict_mk():
    for line in DNA:
        line = line.rstrip()
        if line.startswith(">"):
            Fasta_label = line[1:]
            Fasta_dict[Fasta_label] =""
        else:
            Fasta_dict[Fasta_label] += line
    return Fasta_dict

def DNA_double_helix():
    Fasta_seqs = list(dict_mk().values())
    RDNA=Fasta_seqs[0][::-1]
    RDNA = RDNA.translate({65:84,84:65,71:67,67:71})
    RDNA2 = RDNA.translate({84:85})
    RDNA1 = Fasta_seqs[0].translate({84:85})
    return RDNA1,RDNA2



for seq in DNA_double_helix():
    for i in range(0,len(seq)):
        x = seq.find("AUG",i,i+3)
        if x != -1:
            AA_seq = ""
            # print(x)
            for n in range(x,len(seq),3):
                codon = seq[n:n+3]
                AA = map.get(codon)
                AA = str(AA)
                if AA == "STOP":
                    AA_seq += "-"
                    break
                else:
                    AA_seq += AA
            if AA_seq.endswith("-"):
                if AA_seq not in aa_seq_list:
                    aa_seq_list.append(AA_seq)
                    print(AA_seq[:-1])

    
