# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
"""
Manage an ORACC corpus
"""

from oracc2csv.catalogue import OCatalogue
from oracc2csv.metadata import OMetadata
from pathlib import Path


class CorpusIntegrityError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class OCorpus:
    def __init__(self, whence: Path):
        self.components = {
            "catalogue": OCatalogue(whence),
            "metadata": OMetadata(whence),
        }
        self.check_integrity()

    def check_integrity(self):
        common_attrs = ["project", "source"]
        vals = dict()
        for k, o in self.components.items():
            for attrname in common_attrs:
                try:
                    vals[attrname]
                except KeyError:
                    pass
                else:
                    if getattr(o, attrname) != vals[attrname]:
                        raise CorpusIntegrityError(
                            f"{k}.{attrname}=='{getattr(o, attrname)}' but previous component(s) used {vals[attrname]}."
                        )
                finally:
                    vals[attrname] = getattr(o, attrname)

    @property
    def abbrev(self):
        return self.components["metadata"].abbrev

    @property
    def description(self):
        return self.components["metadata"].description

    @property
    def fieldnames(self):
        return self.components["catalogue"].fieldnames

    @property
    def license(self):
        return self.components["metadata"].license

    @property
    def name(self):
        return self.components["metadata"].name

    @property
    def project(self):
        return self.components["metadata"].project

    @property
    def source(self):
        return self.components["metadata"].source

    def __len__(self):
        return len(self.components["catalogue"])
