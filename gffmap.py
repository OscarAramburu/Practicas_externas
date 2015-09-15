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

    target = anotaciones.split(sep=';')

    target1 = target[1].replace('Target=','')

    gap=None
    
    for anotacion in target:

        if anotacion.startswith('Gap='):
        
            gap = anotacion.replace('Gap=','').rstrip()

    posiciones['gap'] = gap
            
    identd, iniciod, find, direcciond = target1.split(sep=' ')

    destino={}

    destino['identificador']=identd

    destino['inicio']=int(iniciod)

    destino['fin']=int(find)

    destino['direccion']=direcciond

    posiciones['destino']=destino

    

    return posiciones


def remap(cromosoma, posicion, mapeo):

    if cromosoma in mapeo:

        for segmento in mapeo[cromosoma]:

            if posicion >= segmento['inicio'] and posicion <= segmento['fin']:

                gap = segmento["gap"].split(sep=' ')
                
                shift = 0
                limit = 0

                for tramo in gap:

                    if limit <= (posicion-segmento['inicio']):

                        if tramo.startswith('M') or tramo.startswith('D'):                        

                            limit = limit + int(tramo[1:])

                            if tramo.startswith('D'):

                                shift = shift - int(tramo[1:])

                        elif tramo.startswith('I') :

                            shift = shift + int(tramo[1:])

                desplazamiento = posicion-segmento['inicio']+shift            
            
                
                posicion_final = segmento['destino']['inicio'] + desplazamiento
                                 
                destino = (segmento['destino']['identificador'],
                           posicion_final)
          
                return destino

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


print(remap('NW_003315958.1', 112852, mapeo))
