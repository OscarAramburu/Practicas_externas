import os
from unittest.mock import patch

from NCBI_chr import genbankid_to_chromosome


def efetch_from_disk(id=None, db=None, retmode=None, rettype=None):
    if os.path.isfile(os.path.join("test_files", id + ".gb")):
        handle = open(os.path.join("test_files", id + ".gb"))
        return handle


@patch("Bio.Entrez.efetch", side_effect=efetch_from_disk)
def test_genbankid_to_chromosome(efetch_mock):

    assert genbankid_to_chromosome('NC_000001.11') == '1'
    assert genbankid_to_chromosome('NT_113888.1') == '14-Unknown'
    assert genbankid_to_chromosome('NT_187509.1') == 'Unknown'
