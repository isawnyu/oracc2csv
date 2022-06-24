# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
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
