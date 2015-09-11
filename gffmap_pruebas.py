"""Esto hace tal cosa."""

grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores = []

mapeo = {}


for line in grch37:

    data = line.split(sep='\t')

    if not line.startswith('#'):

        ident = data[0]

        if ident not in mapeo:

            mapeo[ident] = []

        inicio, fin = data[3:5]

        posiciones={}

        posiciones['inicio']=inicio

        posiciones['fin']=fin

        mapeo[ident].append(posiciones)

        direccion = data[6]

        posiciones['direccion']=direccion

        anotaciones = data[8]

        target = anotaciones.split(sep=';')[1]

        target1 = target.replace('Target=','')

        identd, iniciod, find, direcciond = target1.split(sep=' ')

        destino={}

        destino['identificador']=identd

        destino['inicio']=iniciod

        destino['fin']=find

        destino['direccion']=direcciond

        posiciones['destino']=destino


        print(mapeo)
        break


print(list(mapeo.items())[:1])

grch37.close()


print(identificadores[:20])

grch37.close()
