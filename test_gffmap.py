from gffmap import parse_line

def test_parse_line():
    """Test the GFF parser."""

    line = ["NT_187509.1", "RefSeq", "match", "3463", "10794", ".", "+",
            ".", "ID=aln4;Target=NT_113885.1 68285 75572 +;"]

    assert parse_line(line) == ""
