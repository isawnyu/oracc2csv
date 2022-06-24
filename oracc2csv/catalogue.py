# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
"""
Catalogue
"""
import json
from pathlib import Path


class OCatalogue:
    def __init__(self, whence: Path):
        filepath = whence / "catalogue.json"
        with open(filepath, "r", encoding="utf-8") as fp:
            self.json = json.load(fp)
        del fp
