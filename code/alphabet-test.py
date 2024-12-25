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

# Various n-ary alphabets
a2 = Alphabet(["0","1"], "w")
a3 = Alphabet(["0","1","2"], "w")
a4 = Alphabet(["0","1","2","3"], "w")
a6 = Alphabet(["0","1","2","3","4","5"], "w")

# Test Word Generation

words = a2.wordsOfLength(0)
assert(words == [''])

words = a2.wordsOfLength(2)
assert(words == ['00','01','10','11'])

words = a2.wordsOfLength(3)
assert(words == ['000','001','010','011','100','101','110','111'])

words = a3.wordsOfLength(2)
assert(words == ['00', '01', '02', '10', '11', '12', '20', '21', '22'])

# Test Symbol Equality

assert(a2.areEqualSymbols('0','0'))
assert(not a2.areEqualSymbols('0','1'))

assert(a2.areEqualSymbols('0','w'))
assert(not a2.areEqualSymbols('0','s')) # s is not the wildcard character

# Test Word Equality

assert(a2.areEqualWords("0010","0010"))
assert(not a2.areEqualWords("0011","0010"))

assert(a2.areEqualWords("001w","0010"))
assert(a2.areEqualWords("001w","0011"))
assert(a2.areEqualWords("001w","001w"))

# Test Subword Presence
assert(a2.isPresentExactlyOnce("001w110w", "0011"))
assert(not a2.isPresentExactlyOnce("001w110w", "1001")) # not cyclic.
assert(not a2.isPresentExactlyOnce("001w110w", "10"))
assert(not a2.isPresentExactlyOnce("001w110w", "111"))

# Test Covering Structures

assert(a2.isUniversalWord("00110", 2))

assert(not a2.isUniversalWord("0011", 2))
assert(not a2.isUniversalWord("0w10", 2))

assert(a2.isUniversalWord("0w011100", 3)) # https://www.sciencedirect.com/science/article/abs/pii/S1571065317301282

assert(a2.isUniversalWord("1111110w0000001w1110111w0001010w1110110w0001101w0110010w1001101w1010010w0101101w1110010w0001000w1110011w0001100w1110101w0001001w1111110", 8))

assert(a2.isDeBruijnCycle("0011", 2))
assert(not a2.isDeBruijnCycle("0011", 3))

