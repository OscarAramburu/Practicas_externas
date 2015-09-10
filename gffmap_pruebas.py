grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores = []

mapeo = {}

for line in grch37:
    
    if not line.startswith('#'):
        
        ident = line.split(sep='\t')[0]
        
        if ident not in mapeo:
            
            mapeo[ident] = []
            
        inicio, fin = line.split(sep='\t')[3:5]

        posiciones={}

        posiciones['inicio']=inicio

        posiciones['fin']=fin

        mapeo[ident].append(posiciones)

        

       
print(list(mapeo.items())[:20])
    
grch37.close()



