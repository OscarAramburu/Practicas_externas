from Bio import Entrez
from Bio.SeqIO.InsdcIO import GenBankIterator


Entrez.email = 'oscararamburugonzale@gmail.com'


def genbankid_to_chromosome(ident):
    handle = Entrez.efetch(db='nucleotide',
                           id=ident,
                           rettype='gb',
                           retmode='text')
    #list_of_features = [SR.features for SR in GenBankIterator(handle)]
    for records in GenBankIterator(handle):
        chromosome = records.features[0].qualifiers['chromosome'][0]

    return chromosome
