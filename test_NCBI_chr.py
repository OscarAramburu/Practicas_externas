from NCBI_chr import genbankid_to_chromosome


def test_genbankid_to_chromosome():

    assert genbankid_to_chromosome('NC_000001.11') == '1'
    assert genbankid_to_chromosome('NC_113888.1') == '14-Unknown'
    assert genbankid_to_chromosome('NC_187509.1') == 'Unknown'