# This file is part of "oracc2csv"
# by Tom Elliott
# (c) Copyright 2022 by Tom Elliott
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#
"""
Dump an ORACC corpus to CSV
"""

from airtight.cli import configure_commandline
from oracc2csv.corpus import OCorpus
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = logging.WARNING
OPTIONAL_ARGUMENTS = [
    [
        "-l",
        "--loglevel",
        "NOTSET",
        "desired logging level ("
        + "case-insensitive string: DEBUG, INFO, WARNING, or ERROR",
        False,
    ],
    ["-v", "--verbose", False, "verbose output (logging level == INFO)", False],
    [
        "-w",
        "--veryverbose",
        False,
        "very verbose output (logging level == DEBUG)",
        False,
    ],
]
POSITIONAL_ARGUMENTS = [
    # each row is a list with 3 elements: name, type, help
    ["source", str, "path to directory containing the ORACC JSON data to dump"],
    ["destination", str, "path to a DIRECTORY where the CSV file should be written"],
]


def main(**kwargs):
    """
    main function
    """
    # logger = logging.getLogger(sys._getframe().f_code.co_name)
    whence = Path(kwargs["source"]).expanduser().resolve()
    where = Path(kwargs["destination"]).expanduser().resolve()
    corpus = OCorpus(whence=whence)
    logger.info(f"Loaded corpus from {whence}: {corpus.name} ({len(corpus)} entries)")
    corpus.dump_csv(where)
    logger.info(f"Wrote corpus to {where}")


if __name__ == "__main__":
    main(
        **configure_commandline(
            OPTIONAL_ARGUMENTS, POSITIONAL_ARGUMENTS, DEFAULT_LOG_LEVEL
        )
    )
