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
from perfectnecklace import PerfectNecklace
from cyclicstring import CyclicString
from cyclicfamily import CyclicFamily

a2 = Alphabet(["0","1"], "w")
a3 = Alphabet(["0","1","2"], "w")
a4 = Alphabet(["0","1","2","3"], "w")
a6 = Alphabet(["0","1","2","3","4","5"], "w")

family = CyclicFamily(a4)

family.addCyclicString("001w110w003w112w021w130w023w132w")
family.addCyclicString("20103100201131012012310220133103")
family.addCyclicString("20303120203131212032312220333123")
family.addCyclicString("22103300221133012212330222133303")
family.addCyclicString("22303320223133212232332222333323")

assert(family.isUniversalPartialFamily(4))

# Test using the alphabet multiplier theorem to produce an upfamily:

a = 2
k = 3
n = 4
d = 1

u = CyclicString(a2, 8)
u.setValues("001w110w")

pn = PerfectNecklace(a3,3,6)
pn.addDiamondicity(4)

v = CyclicString(a6, len(pn.values))
v.setValues(pn.values)

v.scalarMultiply(2)
print("            av:", v)

print(len(v.values), len(u.values))

u.concatenate(int(len(v.values) / len(u.values)))

print("     u^(k^n-d):", u)

u.alphabet = a6
u.add(v)


cf = CyclicString(a6, len(u.values))
cf.setValues("001w110w003w112w005w114w021w130w023w132w025w134w041w150w043w152w045w154w201w310w203w312w205w314w221w330w223w332w225w334w241w350w243w352w245w354w401w510w403w512w405w514w421w530w423w532w425w534w441w550w443w552w445w554w")

for offset in range(0,len(u.values)):
    cf.rotateLeft()
    
    print(len(u.values))

    members = 27
    element_length = int(len(u.values) / members)

    #for d in range(0,len(u.values)):
    f = CyclicFamily(a6)
    for i in range(0,members):
        x = str(cf)[element_length*i:element_length*(i+1)]
        print(x)
        f.addCyclicString(x)
    if (f.isDeBruijnFamily(4)):
        print("YES: Slice Offset %s" % offset)
    else:
        print("NO: Slice Offset %s" % offset)