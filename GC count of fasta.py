DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_gc.txt", "r")
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
  for Seq_id in Fasta_dict.keys():
    Seq_find = Fasta_dict.get(Seq_id)
    GC_ratio = (float(Seq_find.count("C")+Seq_find.count("G"))/float(len(Seq_find)))*100
    Fasta_dict.update({Seq_id:GC_ratio})
  return Fasta_dict
print(dict_mk())



