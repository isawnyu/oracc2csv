# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
"""
Catalogue
"""
from oracc2csv.oracc_base import OBase
from pathlib import Path


class CatalogueError(Exception):
    def __init__(self, msg: str):
        Exception.__init__(self, msg)


class OCatalogue(OBase):
    def __init__(self, whence: Path):
        filepath = whence / "catalogue.json"
        OBase.__init__(self, filepath)

    @property
    def fieldnames(self):
        try:
            return self._fieldnames
        except AttributeError:
            fn = set()
            previous = None
            for m_id, m_data in self.json["members"].items():
                current = set(m_data.keys())
                if previous is not None:
                    if current != previous:
                        CatalogueError("Fieldnames vary by member!")
                fn.update(current)
                previous = current
            self._fieldnames = fn
            return self._fieldnames

    def __len__(self):
        try:
            return self._length
        except AttributeError:
            self._length = len(self.json["members"])
        return self._length
