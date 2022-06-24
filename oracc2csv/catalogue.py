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


class CatalogueError(Exception):
    def __init__(self, msg: str):
        Exception.__init__(self, msg)


class OCatalogue:
    def __init__(self, whence: Path):
        filepath = whence / "catalogue.json"
        with open(filepath, "r", encoding="utf-8") as fp:
            self.json = json.load(fp)
        del fp

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

    @property
    def license(self):
        result = list()
        for attrname in ["license", "license_url"]:
            result.append(self._attr_by_name(attrname))
        return tuple(result)

    @property
    def project(self):
        return self._attr_by_name("project")

    @property
    def source(self):
        return self._attr_by_name("source")

    @property
    def timestamp(self):
        ts = self._attr_by_name("UTC_timestamp")
        return ts + "Z"

    @property
    def type(self):
        return self._attr_by_name("type")

    def _attr_by_name(self, attrname):
        _attrname = f"_{attrname}"
        try:
            return getattr(self, _attrname)
        except AttributeError:
            json_key = attrname.replace("_", "-")
            setattr(self, _attrname, self.json[json_key])
        return getattr(self, _attrname)

    def __len__(self):
        try:
            return self._length
        except AttributeError:
            self._length = len(self.json["members"])
        return self._length
