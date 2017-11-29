#!/usr/bin/env python

import sys
import vcr

sys.argv.pop(0)

with vcr.use_cassette('fixtures/api.yml'):
    execfile(sys.argv[0])
