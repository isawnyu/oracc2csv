<!--
This file is part of "oracc2csv"
by Tom Elliott for the Institute for the Study of the Ancient World (NYU)
(c) Copyright 2022 by New York University
Licensed under the AGPL-3.0; see LICENSE.txt file.
-->

# oracc2csv

The [Open Richly Annotated Cuneiform Corpus (ORACC)](http://oracc.museum.upenn.edu/) publishes JSON data for each of its projects. Sometimes you want the catalog data listing each text to be in CSV format. This package does that.

This program was written by [Tom Elliott](https://orcid.org/0000-0002-4114-6677) for the [Institute for the Study of the Ancient World (NYU)](https://isaw.nyu.edu) and is Copyright 2022 by New York University. It is licensed under the GNU Affero General Public License (see LICENSE.txt).

## Install

Create a python 3.10.4+ virtual environment. Download or clone this package from GitHub. Run:

```
pip install -U -r requirements_dev.txt
```

## Use

Download the zip file of the ORACC project you're interested in (e.g., http://oracc.org/json/hbtin.zip). Run the oracc2csv `dump` script:

```
> python scripts/dump.py -v ~/oracc/hbtin ~/scratch
INFO:root:logging level changed to INFO via command line option; was WARNING
INFO:oracc2csv:Loaded corpus from /Users/banana/oracc/hbtin:
HBTIN: Hellenistic Babylonia: Texts, Iconography, Names
Cuneiform texts, iconography and onomastic data from Hellenistic Babylonia, primarily from Uruk. HBTIN texts form the demonstrator corpus of the <a href="http://berkeleyprosopography.org/">Berkeley Prosopography Service</a> (BPS).  Directed by Laurie Pearce at UC Berkeley.
572 entries
INFO:oracc2csv:Wrote corpus to /Users/banana/scratch
```

