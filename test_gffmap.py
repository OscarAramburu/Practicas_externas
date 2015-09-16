"""Tests para gffmap."""
from gffmap import parse_line

from gffmap import remap

from gffmap import calcular_shift

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
    """Test remap is doing the right sums."""

    mapeo = {
        'NT_187509.1': [{
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
    assert remap('NT_187509.1', 3525, mapeo) is None
    # Valor mapeado en una insercion
    assert remap('NT_187509.1', 6700, mapeo) == ('NT_113885.1', 71479)


def test_remap_reverse():
    """Test reversed segments are correctly calculated."""
    mapeo = {
        "NT_187499.1": [{
            "ident": "NT_187499.1",
            "inicio": 72411,
            "fin": 100559,
            "direccion": "+",
            "gap": "M5585 D1 M1503 I1 M2 I1 M293 D3 M1494 D8 M1106 D4 M218 " +
                   "D4 M70 D1 M1 D1 M4 I2 M390 D4 M871 I1 M99 I1 M469 I4 M1 " +
                   "I14 M4 I6 M10 I3 M1 I4 M2 I3 M3 I6 M2 I4 M6 I7 M7 I2 M1 " +
                   "I5 M1044 D1 M520 I1 M302 D1 M139 D33 M897 D1 M1095 I2 " +
                   "M78 D7 M201 D1 M572 D24 M852 D1 M1221 D1 M623 I3 M939 " +
                   "I3 M1676 D1 M74 I2 M154 I1 M284 I24 M1283 I1 M1562 D1 " +
                   "M219 I3 M1919 D2 M253",
            "destino": {"identificador": "NT_113888.1",
                        "inicio": 33744,
                        "fin": 61896,
                        "direccion": "-"}}]}

    assert remap('NT_187499.1', 72412, mapeo) == ('NT_113888.1', 61895)
    # Las posiciones que caen en un D deben devolver NULL.
    assert remap('NT_187499.1', 77996, mapeo) is None

def test_calcular_shift():
    gap='M62 D47 M3126 I4 M725 D1 M3371'

    assert calcular_shift(gap, 4000-3463)== (-47)
    assert calcular_shift(gap, 3525-3463)== (None)
