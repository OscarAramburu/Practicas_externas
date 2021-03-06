from Bio import Entrez
from Bio.SeqIO.InsdcIO import GenBankIterator


Entrez.email = 'oscararamburugonzale@gmail.com'


def genbankid_to_chromosome(ident):
    handle = Entrez.efetch(db='nucleotide',id=ident,rettype='gb',retmode='text')
    #list_of_features = [SR.features for SR in GenBankIterator(handle)]
    for records in GenBankIterator(handle):
        qualifiers = records.features[0].qualifiers
        chromosome = qualifiers['chromosome'][0]
        if 'map' in qualifiers:
            position = qualifiers['map'][0]
            chromosome += position.replace('unlocalized','-Unknown')

    return chromosome
