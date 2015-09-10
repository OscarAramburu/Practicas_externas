"""Esto hace tal cosa."""
grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores=[]

for line in grch37:

    if not line.startswith('#'):

        ident = line.split(sep='\t')[0]

        if ident not in identificadores:

            identificadores.append(ident)


print(identificadores[:20])

grch37.close()
