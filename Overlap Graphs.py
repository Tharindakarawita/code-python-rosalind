DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_grph (5).txt", "r")
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
fasta_seqs=list(dict_mk().values())    
fasta_keys=list(dict_mk().keys())

for n in range(len(fasta_seqs)):
    for m in range(len(fasta_seqs)):
        if not m == n:
            if fasta_seqs[m][:3] == fasta_seqs[n][-3:]:
                print(fasta_keys[n],fasta_keys[m])        
              


