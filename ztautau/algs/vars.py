#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
met.py - For building met.
"""

import math
import os
from itertools import combinations
from copy import copy, deepcopy
from types import MethodType

import pyframe
import ROOT

GeV = 1000.0

import logging
log = logging.getLogger(__name__)

def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))


# EOF 








