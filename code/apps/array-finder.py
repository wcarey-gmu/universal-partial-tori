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

"""
Author: Stefan Popescu

The code in this module deals with universal partial matrices (upmatrices). 
Upmatrices are defined in Section 2, and computational search results for 
upmatrices are shown in Section 3.

To execute the code, run `python3 array-finder.py <length> <width> <alphabet-size>` 
to search an entire solution space. For example, `python3 array-finder 5 3 2` 
will iterate over all of the possible 5-by-3 matrices for the binary alphabet and 
create a file called `output.txt` with all of the upmatrices found. In the paper, 
the only upmatrices found computationall have 2-by-2 submatrices and are over the 
binary alphabet.
"""
import sys

"""
This function tests for whether a candidate is a universal partial word (upword) for a particular
alphabet and subword length. It is not used anywhere else in the code.
"""
def isUpword(candidate, alphabet, subwordLength):
    words = []
    for i in range(len(candidate) - subwordLength + 1):
        word = [""]
        for j in range(subwordLength):
            newCharacter = candidate[i + j]
            if newCharacter == "⋄":
                word *= len(alphabet)
                for k in range(len(word)):
                    word[k] += alphabet[k * len(alphabet) // len(word)]
            else:
                for k in range(len(word)):
                    word[k] += newCharacter
        for j in range(len(word)):
            if word[j] in words:
                return False
            words.append(word[j])
    if len(words) == len(alphabet) ** subwordLength:
        return True
    return False

"""
This function tests for whether a candidate is an upmatrix for a particular alphabet and a
particular sub-matrix size. In the paper, all upmatrices shown have a 2-by-2 submatrix size.
"""
def isUpmatrix(candidate, alphabet, submatrixLength, submatrixWidth):
    matrices = []
    for i in range(len(candidate) - submatrixLength + 1):
        for j in range(len(candidate[0]) - submatrixWidth + 1):
            matrix = [""]
            for k in range(submatrixLength):
                for l in range(submatrixWidth):
                    newCharacter = candidate[i + k][j + l]
                    if newCharacter == "⋄":
                        matrix *= len(alphabet)
                        for m in range(len(matrix)):
                            matrix[m] += alphabet[m * len(alphabet) // len(matrix)]
                    else:
                        for m in range(len(matrix)):
                            matrix[m] += newCharacter
            for k in range(len(matrix)):
                if matrix[k] in matrices:
                    return False
                matrices.append(matrix[k])
    if len(matrices) == len(alphabet) ** (submatrixLength * submatrixWidth):
        return True
    return False

"""
This function generates a particular upword, which will be brute-forced later. This function is
also used within `generateUpmatrix()`.
n = The particular upword to generate.
l = The length of the words.
a = The length of the alphabet.
For example, `generateUpword(1, 5, 2)` will return "00001".
"""
def generateUpword(n, l, a):
    s = ""
    while n > 0:
        if n % (a + 1) == a:
            s = "⋄" + s
            n -= a
        else:
            s = str(n % (a + 1)) + s
        n //= (a + 1)
    while len(s) < l:
        s = "0" + s
    return s

"""
Similar to the above, this function generates a specific matrix. In the main loop, we will run
this function to iterate over the entire solution space.
"""
def generateUpmatrix(n, l, w, a):
    m = ["0" * l for i in range(w)]
    i = w - 1
    while n > 0:
        q = n % ((a + 1) ** l)
        m[i] = generateUpword(q, l, a)
        n //= ((a + 1) ** l)
        i -= 1
    
    return m

"""
This is the main loop of the code that actually executes everything. It will iterate over the
entire solution space and store the found upmatrices in a file called `output.txt`.
"""
if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        print("Usage: python3 array-finder.py <length> <width> <alphabet-size>")
        sys.exit(1)
    
    l = int(sys.argv[1])
    w = int(sys.argv[2])
    a = int(sys.argv[3])
    
    n = (a + 1) ** (l * w)
    
    outfile = open("output.txt", "w", encoding="utf-8")
    outfile.close()
    
    print(f"Iterating over {n} possible candidates...")
    
    for i in range(n):
        m = generateUpmatrix(i, l, w, 2)
        print(f"\r{i + 1} / {n} complete.", end="", flush=True)
        
        if isUpmatrix(m, "0123456789"[0 : a], 2, 2):
            with open("output.txt", "a", encoding="utf-8") as file:
                file.write(f"Matrix #{i}\n")
                for j in range(w):
                    file.write(f"{m[j]}\n")
                file.write("\n")
