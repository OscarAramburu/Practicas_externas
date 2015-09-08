grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores=[]



for line in grch37:
    if line.startswith('#'):
        pass
    else:
    
        ident=line.split(sep='\t')[0]
        if ident in identificadores:
            pass
        else:
            identificadores.append(ident)
        
        

print(identificadores[:20])
    
grch37.close()



