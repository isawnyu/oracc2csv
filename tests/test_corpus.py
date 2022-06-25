# This file is part of "oracc2csv"
# by Tom Elliott for the Institute for the Study of the Ancient World (NYU)
# (c) Copyright 2022 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

from pathlib import Path
from oracc2csv.corpus import OCorpus
from shutil import rmtree


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
        assert corpus.fieldnames == {
            "accession_no",
            "ancient_year",
            "bibilography",
            "copy",
            "date_bce",
            "date_comments",
            "designation",
            "genre",
            "id_text",
            "langs",
            "language",
            "material",
            "months_recorded",
            "museum_no",
            "object_type",
            "period",
            "photo",
            "pleiades_coord",
            "pleiades_id",
            "project",
            "provenience",
            "supergenre",
            "tablet_comments",
            "text_comments",
            "trans",
        }

    def test_dump_csv(self):
        whence = Path("tests/data/adsd")
        corpus = OCorpus(whence)
        where = "tests/data/scratch"
        rmtree(where, ignore_errors=True)
        where = Path(where)
        where.mkdir(parents=True)
        corpus.dump_csv(where)
