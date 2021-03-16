import collections
from os import sep

DNA = open("C:/Users/nayan/Downloads/rosalind_revp.txt", "r").readlines()
#DNA = open("C:/Users/nayan/Desktop/new 7.txt", "r").readlines()




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


DNA_string = dict_mk()
Compliment_DNA_string = dict_mk().replace('T','1').replace('A','2').replace('G','3').replace('C','4').replace('1','A').replace('2','T').replace('3','C').replace('4','G')

#print(DNA_string,Compliment_DNA_string,sep= '\n')


Result_dict = {}
for n in range(0,len(DNA_string)):
    for i in range(0,len(DNA_string)):
        if (i+n+4) - (0+i) == len(DNA_string[0+i:i+4+n]):
            if len(DNA_string[0+i:i+4+n]) <= 12:
                #print(DNA_string[0+i:i+n+4])
                if DNA_string[0+i:i+n+4] == Compliment_DNA_string[0+i:i+n+4][::-1]:
                    #print(DNA_string[0+i:i+n+4],Compliment_DNA_string[0+i:i+n+4][::-1],sep= '\n')
                    #print()
                    Result_dict[i+1] = len(DNA_string[0+i:i+n+4])

            
dict = collections.OrderedDict(sorted(Result_dict.items()))
for i,n in dict.items():
    print(i,n)