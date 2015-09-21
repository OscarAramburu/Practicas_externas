"""Maps a hg38 into a hg19 position."""
import NCBI_chr
 import json

def parse_line(data):
    """Devuelve un diccionario con los datos en data.

    >>> parse_line(
    ...     ["NT_187509.1", "RefSeq", "match", "3463", "10794", ".", "+",
    ...      ".", "ID=aln4;Target=NT_113885.1 68285 75572 +;"])
    {"ident": "NT_187509.1", "inicio": "3463", "fin": "10794",
     "direccion": "+", {"identificador": "NT_113885.1",
                        "inicio": "68285",
                        "fin": "75572",
                        "direccion": "+"}}

    """

    posiciones = {}
    destino = {}
    gap = None

    inicio, fin = data[3:5]

    posiciones['ident'] = data[0]
    posiciones['inicio'] = int(inicio)
    posiciones['fin'] = int(fin)
    posiciones['direccion'] = data[6]

    target = data[8].split(sep=';')
    target1 = target[1].replace('Target=', '')

    for anotacion in target:
        if anotacion.startswith('Gap='):
            gap = anotacion.replace('Gap=', '').rstrip()

    posiciones['gap'] = gap

    identd, iniciod, find, direcciond = target1.split(sep=' ')

    destino['identificador'] = identd
    destino['inicio'] = int(iniciod)
    destino['fin'] = int(find)
    destino['direccion'] = direcciond

    posiciones['destino'] = destino

    return posiciones


def calcular_shift(gap, despl):
    """Calcula el desplazamiento con inserciones y deleciones.

    >>> calcular_shift('M5585 D1 M1503 I1 M2', 6000)
    -1
    >>> calcular_shift('M5585 D1 M1503 I1 M2 ',5586)
    None

    """

    shift = 0
    limit = 0

    for tramo in gap.split(sep=' '):

        if limit <= despl:
            if tramo.startswith('M') or tramo.startswith('D'):
                limit += int(tramo[1:])

                if tramo.startswith('D'):
                    shift -= int(tramo[1:])

            elif tramo.startswith('I'):
                shift += int(tramo[1:])

            tramo_anterior = tramo

        else:
            if tramo_anterior.startswith('D'):
                return None

    return shift


def remap(cromosoma, posicion, mapeo):
    """Devuelve la posicion de mapeo para cromosoma y posicion.
    
    >>> remap("NT_187509.1", 4000, {
    ...       'NT_187509.1': [{
    ...       'ident': "NT_187509.1",
    ...       'inicio': 3463,
    ...       'fin': 10794,
    ...       'direccion': "+",
    ...       'gap': 'M62 D47 M3126 I4 M725 D1 M3371',
    ...       'destino': {'identificador': 'NT_113885.1',
    ...                   'inicio': 68285,
    ...                   'fin': 75572,
    ...                   'direccion': '+'}}]})
    ('NT_113885.1', 68775)
    
    """

    if cromosoma in mapeo:
        for segmento in mapeo[cromosoma]:
            if posicion >= segmento['inicio'] and posicion <= segmento['fin']:

                gap = segmento["gap"]

                shift = calcular_shift(gap, posicion - segmento['inicio'])

                if shift is None:
                    return None

                desplazamiento = posicion - segmento['inicio'] + shift
                if segmento['destino']['direccion'] == '-':
                    posicion_final = segmento['destino']['fin'] -\
                        desplazamiento

                else:

                    posicion_final = segmento['destino']['inicio'] +\
                        desplazamiento

                destino = (segmento['destino']['identificador'],
                           posicion_final)

                return destino

if __name__ == "__main__":
    MAPEO = {}


    with open('GRCh37-GRCh38.gff') as grch37:
        for line in grch37:
            data = line.split(sep='\t')

            if not line.startswith('#'):
                posiciones = parse_line(data)
                ident = posiciones['ident']

                if not ident in MAPEO:
                    MAPEO[ident] = []
                    MAPEO[ident].append(posiciones)
                    #print(NCBI_chr.genbankid_to_chromosome(ident))
    json_dump = open('mapeo.json','w')
    json.dump(MAPEO,json_dump)
    json_dump.close()
