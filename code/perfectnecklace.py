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

class PerfectNecklace(object):
    def __init__(self, alphabet, wordLength, modularLength):
        self.alphabet = alphabet
        self.wordLength = wordLength
        self.modularLength = modularLength
        words = self.alphabet.wordsOfLength(wordLength)
        self.values = ""
        for w in words:
            self.values += str(w * (int(modularLength / wordLength)))
            
    def addDiamondicity(self, interval):
        newValues = ""
        for n in range(0, int(len(self.values) / (interval-1))):
            newValues += self.values[n*(interval-1):n*(interval-1)+(interval-1)] + self.alphabet.wildcard
        self.values = newValues
