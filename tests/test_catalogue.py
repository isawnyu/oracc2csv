# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

import json
from oracc2csv.catalogue import OCatalogue
from pathlib import Path


class TestCatalogue:
    def test_json_present(self):
        whence = Path("tests/data/adsd/catalogue.json")
        with open(whence, "r", encoding="utf-8") as fp:
            j = json.load(fp)
        del fp
        assert j["type"] == "catalogue"
        assert j["project"] == "adsd"

    def test_catalogue_read(self):
        whence = Path("tests/data/adsd")
        c = OCatalogue(whence)
        assert c.json["type"] == "catalogue"
        assert c.json["project"] == "adsd"

    def test_attributes(self):
        whence = Path("tests/data/adsd")
        c = OCatalogue(whence)
        assert c.type == "catalogue"
        assert c.project == "adsd"
        assert c.source == "http://oracc.org/adsd"
        assert c.license == (
            "This data is released under the CC0 license",
            "https://creativecommons.org/publicdomain/zero/1.0/",
        )
        assert c.timestamp == "2021-03-24T13:57:35Z"
