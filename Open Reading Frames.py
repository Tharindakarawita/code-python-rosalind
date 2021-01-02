DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_gc.txt", "r")
Fasta_dict = {}
Fasta_label = ""
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

Fasta_seqs = list(dict_mk().values())

RDNA=Fasta_seqs[0][::-1]

RDNA = RDNA.translate({65:84,84:65,71:67,67:71})
RDNA2 = RDNA.translate({84:85})
RDNA1 = Fasta_seqs[0].translate({84:85})
print(RDNA1)
print(RDNA2)


for seq in RDNA1,RDNA2:
    AA_seq = ""
    for i in range(0,len(seq)):
        codon = seq[i:i+3]
        AA = map.get(codon)
        AA = str(AA)
        if AA == "M":
            print("K")

    
