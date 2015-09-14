"""Tests para gffmap."""
from gffmap import parse_line


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
        'destino': {'identificador': 'NT_113885.1',
                    'inicio': 68285,
                    'fin': 75572,
                    'direccion': '+'}}
