# This file is part of "oracc2csv"
# by Tom Elliott for the Institute for the Study of the Ancient World (NYU)
# (c) Copyright 2022 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

import json
from oracc2csv.metadata import OMetadata
from pathlib import Path


class TestMetadata:
    def test_json_present(self):
        whence = Path("tests/data/adsd/metadata.json")
        with open(whence, "r", encoding="utf-8") as fp:
            j = json.load(fp)
        del fp
        assert j["type"] == "metadata"
        assert j["project"] == "adsd"

    def test_metadata_read(self):
        whence = Path("tests/data/adsd")
        meta = OMetadata(whence)
        assert meta.json["type"] == "metadata"
        assert meta.json["project"] == "adsd"

    def test_attributes(self):
        whence = Path("tests/data/adsd")
        meta = OMetadata(whence)
        assert meta.type == "metadata"
        assert meta.project == "adsd"
        assert meta.source == "http://oracc.org/adsd"
        assert meta.license == (
            "This data is released under the CC0 license",
            "https://creativecommons.org/publicdomain/zero/1.0/",
        )
        assert meta.timestamp == "2021-03-24T13:58:01Z"
        assert meta.abbrev == "ADsD"
        assert meta.description.startswith(
            "ADsD provides an online edition of the Babylonian Astronomical Diaries. The"
        )
        assert meta.name == "Astronomical Diaries Digital"
