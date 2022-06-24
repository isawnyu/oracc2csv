# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

from pathlib import Path
from oracc2csv.corpus import OCorpus


class TestCorpus:
    def test_integrity(self):
        whence = Path("tests/data/adsd")
        corpus = OCorpus(whence)
