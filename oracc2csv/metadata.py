# This file is part of "oracc2csv"
# by Tom Elliott for the Institute for the Study of the Ancient World (NYU)
# (c) Copyright 2022 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
"""
ORACC Metadata
"""
from oracc2csv.oracc_base import OBase
from pathlib import Path


class MetadataError(Exception):
    def __init__(self, msg: str):
        Exception.__init__(self, msg)


class OMetadata(OBase):
    def __init__(self, whence: Path):
        filepath = whence / "metadata.json"
        OBase.__init__(self, filepath)

    @property
    def abbrev(self):
        try:
            return self._abbrev
        except AttributeError:
            self._abbrev = self.json["config"]["abbrev"]
            return self._abbrev

    @property
    def blurb(self):
        try:
            return self._blurb
        except AttributeError:
            self._blurb = self.json["config"]["blurb"]
            return self._blurb

    @property
    def description(self):
        return self.blurb

    @property
    def name(self):
        try:
            return self._name
        except AttributeError:
            self._name = self.json["config"]["name"]
            return self._name
