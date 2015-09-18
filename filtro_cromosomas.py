import json
import NCBI_chr

mapeo = json.load(open('mapeo.json','r'))
cromosomas = {}

for ident in mapeo:
    nombre_chr = NCBI_chr.genbankid_to_chromosome(ident)
    if len(nombre_chr) <3:
        cromosomas[nombre_chr] = mapeo[ident]

print(cromosomas)

#TODO: guardar el diccionario "cromosomas" en un archivo que se llame
# cromosomas.json.
# - SE utiliza la función 'open' para abrir el archivo.
# - Se utiliza la función 'json.dump' para guardar un diccionario.