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


#------------------------------------------------------------------------------
class Vars(pyframe.core.Algorithm):
    """
    computes variables and puts them in the store
    """
    #__________________________________________________________________________
    def __init__(self,
                 name      = 'Vars',
                 ):
        pyframe.core.Algorithm.__init__(self, name)

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)

        self.store["dummy"] = self.chain.tau_0_pt + self.chain.lep_0_pt

        return True



# EOF 








