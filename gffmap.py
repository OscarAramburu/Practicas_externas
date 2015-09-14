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

    posiciones['inicio']=int(inicio)

    posiciones['fin']=int(fin)

    direccion = data[6]

    posiciones['direccion']=direccion

    anotaciones = data[8]

    target = anotaciones.split(sep=';')[1]

    target1 = target.replace('Target=','')

    identd, iniciod, find, direcciond = target1.split(sep=' ')

    destino={}

    destino['identificador']=identd

    destino['inicio']=int(iniciod)

    destino['fin']=int(find)

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

grch37.close()


"""====================================="""
def remap(cromosoma, posicion):

    if cromosoma in mapeo:

        for segmento in mapeo[cromosoma]:

            if posicion >= segmento['inicio'] and posicion <= segmento['fin']:

                pos_inicio = posicion - segmento['inicio']

                posicion_final = pos_inicio + segmento['destino']['inicio']

                destino = (segmento['destino']['identificador'],
                           posicion_final)
    
                       
                return destino



        

print(remap('NW_003315958.1', 112852))
