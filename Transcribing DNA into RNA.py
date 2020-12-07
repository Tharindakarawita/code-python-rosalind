DNA = open("C:/Users/Tharinda Karawita/Downloads/rosalind_revc.txt").read()
RDNA=DNA[::-1]
seq_dict = {65:84,84:65,71:67,67:71}
print(RDNA.translate(seq_dict))