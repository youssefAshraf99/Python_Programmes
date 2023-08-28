inputfile="DNA_sequence_original.txt" 
f=open(inputfile,"r")
seq=f.read()
seq=seq.replace("\n","") 
seq=seq.replace("\r","")
print("Numper of Nucludieds in DNA is:",len(seq),"\n")

print("Numper of Adenine is:",seq.count("A"),"\n")
print("Numper of Cytosine is:",seq.count("C"),"\n")
print("Numper of Guanine is:",seq.count("G"),"\n")
print("Numper of Thymine is:",seq.count("T"),"\n")

print("#"*50,"\n")


table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 #الجدول بتاع تحول الحمض النووي ل برونين
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
         }

count = {}

for i in range(0, len(seq)-2, 3):
    codon = seq[i:i+3]
    #print(codon)
    aa = table[codon]
    if aa not in count:
        count[aa] = 0
    count[aa] += 1

for aa in sorted(count.keys()):
    print("Numper of amino Acide","{}  {}".format(aa, count[aa]),"\n")

print("#"*50,"\n")
print("Translated DNA IS:","\n")
def translate(seq):
   
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 #الجدول بتاع تحول الحمض النووي ل برونين
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein=""
    if len(seq)%3==0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protein+=table[codon]
    return protein
def read_seq(inputfile):
    with open(inputfile,"r") as f:
        seq=f.read()
    seq=seq.replace("\n","")
    seq=seq.replace("\r","")
    return seq
prt = read_seq("amino_acid_sequence_original.txt")
dna = read_seq("DNA_sequence_original.txt")

p=translate(dna[20:935])
print (p,"\n")
if(p==prt):
    print ("The analysis was completed successfully \n  ")

