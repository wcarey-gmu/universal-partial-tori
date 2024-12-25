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

# Some test cases from De Bruijn 1946
a = Alphabet(["0","1"])

a.isDeBruijnCycle('0000100110101111', 4)

# subword length = 1

assert(a.isDeBruijnCycle('01', 1)) # should be the only one.
assert(a.isDeBruijnCycle('10', 1)) # differs only by rotation.

assert(not a.isDeBruijnCycle('1', 1)) # fails because 0 does not appear.
assert(not a.isDeBruijnCycle('100', 1)) # fails because 0 appears more than once.

# subword length = 2

assert(a.isDeBruijnCycle('0011', 2)) # should be the only one.
assert(a.isDeBruijnCycle('0110', 2)) # differs only by rotation.

assert(not a.isDeBruijnCycle('001', 2)) # faily because 11 does not appear
assert(not a.isDeBruijnCycle('0101', 2)) # fails because 11 and 00 do not appear
assert(not a.isDeBruijnCycle('00110', 2)) # fails because 00 appears twice

#subword length = 3

assert(a.isDeBruijnCycle('00010111', 3)) # example in paper
assert(not a.isDeBruijnCycle('000101110', 3)) # fails because 000 appears twice
assert(not a.isDeBruijnCycle('0001011', 3)) # fails because 111 does not appear

# Some test cases from Professor Kirsch's notes:

a = Alphabet(["0","1","2"])

assert(a.isDeBruijnCycle('001122102', 2)) # Class example
assert(a.isDeBruijnCycle('201221100', 2)) # Reflection
assert(not a.isDeBruijnCycle('20122110', 2)) # fails because 00 does not appear
assert(not a.isDeBruijnCycle('2012211000', 2)) # fails because 00 appears twice

# Some test cases from Sawada, Williams, Wong

a = Alphabet(["0","1"])

assert(a.isDeBruijnCycle('00000111110111001100010110101001', 5))
assert(a.isDeBruijnCycle('00000111110110101110010100110001', 5))

# Test case from Dr. Kirsch's paper

a = Alphabet(["0","1",], "w")
assert(a.isUniversalPartialCycle("001w110w",4))

# Lift of the upcycle 001w110w003w112w021w130w023w132w201w310w203w312w221w330w223w332w
a = Alphabet(["0", "1", "2", "3"])
assert(a.isUniversalPartialCycle("0010110000301120021013000230132020103100203031202210330022303320001111010031112102111301023113212011310120313121221133012231332100121102003211220212130202321322201231022032312222123302223233220013110300331123021313030233132320133103203331232213330322333323", 4))

# Lift of the upcycle 001w110w003w112w021w130w023w132w201w310w203w312w221w330w223w332w
assert(a.isUniversalPartialCycle("0010110000301120021013000230132020103100203031202210330022303320001211020032112202121302023213222012310220323122221233022232332200111101003111210211130102311321201131012031312122113301223133210013110300331123021313030233132320133103203331232213330322333323", 4))

# I'm surprised this one works?
# Lift of the upcycle 001w110w003w112w021w130w023w132w201w310w203w312w221w330w223w332w
assert(a.isUniversalPartialCycle("0010110000301120021013000230132020103100203031202210330022303320001211020032112202121302023213222012310220323122221233022232332200111101003111210211130102311321201131012031312122113301223133210013110300331123021313030233132320133103203331232213330322333323", 4))