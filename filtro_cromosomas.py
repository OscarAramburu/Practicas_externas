import json
import NCBI_chr

mapeo = json.load(open('mapeo.json','r'))
cromosomas = {}

for ident in mapeo:
    nombre_chr = NCBI_chr.genbankid_to_chromosome(ident)
    if len(nombre_chr) <3:
        cromosomas[nombre_chr] = mapeo[ident]


chr = open('cromosomas.json','w')
json.dump(cromosomas,chr)
chr.close()

#TODO: guardar el diccionario "cromosomas" en un archivo que se llame
# cromosomas.json.
# - SE utiliza la funcion 'open' para abrir el archivo.
# - Se utiliza la funcion 'json.dump' para guardar un diccionario.