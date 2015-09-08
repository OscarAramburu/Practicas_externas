grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores=[]

for line in grch37:
    print(line.split(sep='\t')[0])
    
grch37.close()



