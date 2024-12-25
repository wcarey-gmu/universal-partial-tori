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

a2 = Alphabet(["0","1"], "w")

s = CyclicString(a2, 4)
s.setValues("0011")

assert(s.isPresentExactlyOnce("00"))
assert(s.isPresentExactlyOnce("01"))
assert(s.isPresentExactlyOnce("10"))
assert(s.isPresentExactlyOnce("11"))

assert(s.isDeBruijnCycle(2))

s = CyclicString(a2, 3)
s.setValues("0w1")

assert(s.isPresentExactlyOnce("00"))
assert(not s.isPresentExactlyOnce("01")) # Appears twice, at indices 0 and 1.
assert(s.isPresentExactlyOnce("10"))
assert(s.isPresentExactlyOnce("11"))

assert(not s.isDeBruijnCycle(2))

a4 = Alphabet(["a","b","c","d"])
s = CyclicString(a4, 8)
s.setValues("abcdaaaa")
s.rotateLeft()

assert(s.valueAt(0) == "b")
assert(s.valueAt(1) == "c")
assert(s.valueAt(2) == "d")
assert(s.valueAt(3) == "a")

s.rotateRight()

assert(s.valueAt(0) == "a")
assert(s.valueAt(1) == "b")
assert(s.valueAt(2) == "c")
assert(s.valueAt(3) == "d")

a = Alphabet(["0","1","2"], "w")

p = CyclicString(a, 3)
p.setValues("0w1")
q = CyclicString(a, 3)
q.setValues("101")
p.add(q)
assert(p.values == "1w2")

p.stripWildcards()
assert(p.length == 2)
assert(p.values == "12")