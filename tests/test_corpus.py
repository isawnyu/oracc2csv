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

    def test_corpus_level_deets(self):
        whence = Path("tests/data/adsd")
        corpus = OCorpus(whence)
        assert corpus.abbrev == "ADsD"
        assert corpus.description.startswith(
            "ADsD provides an online edition of the Babylonian Astronomical Diaries. The"
        )
        assert corpus.license == (
            "This data is released under the CC0 license",
            "https://creativecommons.org/publicdomain/zero/1.0/",
        )
        assert corpus.name == "Astronomical Diaries Digital"
        assert len(corpus) == 401
