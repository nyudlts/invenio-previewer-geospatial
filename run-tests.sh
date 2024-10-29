#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.


# Usage:
#   ./run-tests.sh

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest
python -m sphinx.cmd.build -qnNW docs docs/_build/html
python -m pytest
tests_exit_code=$?
python -m sphinx.cmd.build -qnNW -b doctest docs docs/_build/doctest
exit "$tests_exit_code"
