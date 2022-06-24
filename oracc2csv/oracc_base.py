# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
"""
Base class for working with ORACC JSON
"""
import json
from pathlib import Path


class OBase:
    def __init__(self, filepath: Path):
        with open(filepath, "r", encoding="utf-8") as fp:
            self.json = json.load(fp)
        del fp

    def _attr_by_name(self, attrname):
        _attrname = f"_{attrname}"
        try:
            return getattr(self, _attrname)
        except AttributeError:
            json_key = attrname.replace("_", "-")
            setattr(self, _attrname, self.json[json_key])
        return getattr(self, _attrname)

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
