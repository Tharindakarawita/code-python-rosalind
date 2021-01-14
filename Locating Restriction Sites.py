DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_gc.txt", "r").readlines()


restriction_enzymes_site  =      """ATGCAT
                                    TGCA
                                    GCATGC
                                    CATG
                                    TATA
                                    ATATGC
                                    ATGCAT
                                    TGCA"""



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
    return Main_seq

table = restriction_enzymes_site.split()

def motif(Main_seq = dict_mk(),substring = table):
    for singal_substring in substring:
        y = len(singal_substring)
        for i in range(0,len(Main_seq)):
            x = Main_seq.find(singal_substring,i,i+y)
            if x != -1:
                print(x+1,y)
    return Main_seq


motif()