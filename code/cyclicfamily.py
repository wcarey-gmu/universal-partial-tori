#!/usr/bin/env python3
###############################################################################
#
#  Project:  MEGL Universal Partial Tori
#  Authors:  William Carey <wcarey1@gmu.edu>
#            Matthew Kearney <mkearne@gmu.edu>
#            Rachel Kirsch <rkirsch4@gmu.edu>
#            Stefan Popescu <spopesc@gmu.edu>
#
#  Acknowledgements: We would like to thank the Mason Experimental Geometry 
#                    Lab (MEGL) for supporting this project and Charles 
#                    Landreaux for collaboration in early stages of the 
#                    research. The third author is supported in part by 
#                    Simons Foundation Grant MP-TSM-00002688.
# 
#  Copyright (c) 2023-2024, William Carey, Matthew Kearney, Rachel Kirsch, Stefan Popescu
#  SPDX-License-Identifier: MIT
#

from alphabet import Alphabet
from cyclicstring import CyclicString

class CyclicFamily(object):
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.values = []
        
    def __str__(self):
        s = ""
        for x in self.values:
            s += str(x) + "\n"
        return s
        
    def addCyclicString(self, chars):
        c = CyclicString(self.alphabet, len(chars))
        c.setValues(chars)
        self.values.append(c)
    
    def isDeBruijnFamily(self, subwordLength):
        """Returns true if @candidate is a de Bruijn family (i.e. a 
           collection of strings that cover all subwords of length 
           @subwordLength exactly once in one member).
        """
        for w in self.alphabet.wordsOfLength(subwordLength):
            totalCount = 0
            for s in self.values:
                totalCount += s.substringCount(w)
            if totalCount != 1:
                return False
        return True
        
    def isUniversalPartialFamily(self, subwordLength):
        """Returns true if @candidate is an upfamily (i.e. a de Bruijn family with 
           at least one wildcard) for subwords of length @subwordLength.
        """
        wildcardPresent = False
        for c in self.values:
            if c.containsWildcard():
                wildcardPresent = True
        if not wildcardPresent:
            return False
        return self.isDeBruijnFamily(subwordLength)
        