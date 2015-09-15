"""Tests para gffmap."""
from gffmap import parse_line

from gffmap import remap


def test_parse_line():
    """Test the GFF parser."""

    line = ["NT_187509.1", "RefSeq", "match", "3463", "10794", ".", "+",
            ".", "ID=aln4;Target=NT_113885.1 68285 75572 +;"
            "Gap=M62 D47 M3126 I4 M725 D1 M3371"]

    assert parse_line(line) == {
        'ident': "NT_187509.1",
        'inicio': 3463,
        'fin': 10794,
        'direccion': "+",
        'gap': 'M62 D47 M3126 I4 M725 D1 M3371',
        'destino': {'identificador': 'NT_113885.1',
                    'inicio': 68285,
                    'fin': 75572,
                    'direccion': '+'}}

def test_remap():

    mapeo = {
        'NT_187509.1':[{
            'ident': "NT_187509.1",
            'inicio': 3463,
            'fin': 10794,
            'direccion': "+",
            'gap': 'M62 D47 M3126 I4 M725 D1 M3371',
            'destino': {'identificador': 'NT_113885.1',
                        'inicio': 68285,
                        'fin': 75572,
                        'direccion': '+'}}]}

    assert remap('NT_187509.1', 4000, mapeo) == ('NT_113885.1', 68775)
    # Valor mapeado en una zona limite.
    assert remap('NT_187509.1', 3463, mapeo) == ('NT_113885.1', 68285)
    assert remap('NT_187509.1', 10794, mapeo) == ('NT_113885.1', 75572)
    # Las posiciones que caen en un D deben devolver NULL.
    assert remap('NT_187509.1', 3525, mapeo) == None
    # Valor mapeado en una insercion
    assert remap('NT_187509.1', 3236, mapeo) == ('NT_113885.1', 68058)
