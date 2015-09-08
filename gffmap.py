grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores=[]

for line in grch37:
    if line.startswith('#'):
        pass
    else:
        identificadores.append(line.split(sep='\t')[0])


print(identificadores[:5])
    
grch37.close()



