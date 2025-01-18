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

from itertools import product

class Alphabet(object):
    """An Alphabet represents a collection of combinatorial objects possibly 
       including wildcard symbols. Because universal cycles and words are 
       defined (in great part) by the alphabet they represent, the logic for 
       detecting those is included here.
    """
    
    def __init__(self, symbols, wildcard=""):
        self.symbols = symbols
        self.wildcard = wildcard
        
    def __str__(self):
        return str(self.symbols) + " with " + str(self.wildcard) + " wild."

# Cartesian Product --------------------------------------------------------- #
    
    def wordsOfLength(self, wordLength):
        """Returns a dict of strings representing all words of length 
           @wordLength that can be formed in the alphabet. Return a^n words, 
           where n is the number of symbols in the alphabet and a is the 
           length of each word.
        """
        words = []
        for w in product(self.symbols, repeat=wordLength):
            words.append(''.join(map(str, w)))
        return words
        
# Symbol Equality ----------------------------------------------------------- #
 
    def areEqualSymbols(self, a, b):
        """Returns true iff the symbols a and b are equal or if either is the 
           wildcard.
        """
        return (a == b) or (a == self.wildcard) or (b == self.wildcard)

    def areEqualWords(self, a, b):
        """Returns true iff the words a and b are equal to one another 
           (using wildcards)
        """
        if len(a) != len(b):
            return False
        for i in range(0, len(a)):
            if not self.areEqualSymbols(a[i], b[i]):
                return False
        return True

# Subword Word Presence ----------------------------------------------------- #

    def isPresentExactlyOnce(self, word, substring):
        """Returns true if @substring appears exactly once as a substring
           of @word. Sensitive to repeating overlapping substrings unlike
           the built in count() function"""
        if len(substring) > len(word):
            return False
        count = 0
        for j in range(len(word)):
            if self.areEqualWords(substring, word[j:j+len(substring)]):
                count += 1
        return count == 1

# Covering Structures ------------------------------------------------------- #
 
    def isUniversalWord(self, candidate, length):
        """Returns true if @candidate is a universal word for subwords of 
           length @length. @candidate should be a string rather than a
           dict.
        """
        for w in self.wordsOfLength(length):
            if not self.isPresentExactlyOnce(candidate, ''.join(map(str, w))):
                return False
        return True
    
    def isDeBruijnCycle(self, candidate, subwordLength):
        """Returns true if @candidate is a de Bruijn cycle for subwords of 
           length @subwordLength.
        """
        extendedWord = candidate+candidate[:subwordLength-1]
        return self.isUniversalWord(extendedWord, subwordLength)

    def isUniversalPartialCycle(self, candidate, subwordLength):
        """Returns true if @candidate is an upcycle (i.e. a de Bruijn cycle with 
           at least one wildcard) for subwords of length @subwordLength.
        """
        if not self.wildcard in candidate:
            return False
        return self.isDeBruijnCycle(candidate, subwordLength)

# Covering Sets ------------------------------------------------------------- #

    def coveringSet(self, s):
        """Returns a dict containing all the words that @s covers in this
           alphabet. If @s has no wildcards, the dictionary will contain
           @s. Currently fails and assertion if @s has more than one wildcard.
        """
        #TODO: Improve this to recursively parse @s to produce the full 
        #      covering set.
        assert(s.count(self.wildcard) < 2)

        coveringSet = []
        if self.wildcard == "":
            return [s]

        for c in self.symbols:
            equivalenceElement = s
            coveringSet.append(equivalenceElement.replace(self.wildcard, c))
        return coveringSet