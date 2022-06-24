# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

import json
from oracc2csv.catalogue import OCatalogue
from pathlib import Path


class TestMetadata:
    def test_json_present(self):
        whence = Path("tests/data/adsd/metadata.json")
        with open(whence, "r", encoding="utf-8") as fp:
            j = json.load(fp)
        del fp
        assert j["type"] == "metadata"
        assert j["project"] == "adsd"
