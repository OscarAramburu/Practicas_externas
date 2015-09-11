"""Esto hace tal cosa."""

grch37= open('GRCh37-GRCh38.gff', 'r')

identificadores = []

def parse_line(data):

    """Recive una linea y parsea a un diccionario.

    >>> parse_line(["NT_187509.1", "RefSeq", "match", "3463", "10794", ".", "+",
    ".", "ID=aln4;Target=NT_113885.1 68285 75572 +;"])
    {"ident": "NT_187509.1", "inicio": "3463", "fin": "10794", "direccion": "+",
     {"identificador": "NT_113885.1", "inicio": "68285", "fin": "75572",
      "direccion": "+"}

    """

    posiciones={}

    ident = data[0]

    inicio, fin = data[3:5]

    posiciones['ident']=ident

    posiciones['inicio']=inicio

    posiciones['fin']=fin

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

    return posiciones

mapeo = {}

for line in grch37:

    data = line.split(sep='\t')

    if not line.startswith('#'):

        posiciones = parse_line(data)

        ident = posiciones['ident']

        if not ident in mapeo:

            mapeo[ident] = []

        mapeo[ident].append(posiciones)

print(list(mapeo.items())[:5])

grch37.close()
