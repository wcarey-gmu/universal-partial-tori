# universal-partial-tori

Code and data supporting the paper [Universal Partial Tori](https://arxiv.org/abs/2409.12417). A De Bruijn cycle is a cyclic sequence in which every word of length n over an alphabet appears exactly once. De Bruijn tori are a two-dimensional analogue. Motivated by recent progress on universal partial cycles and words, which shorten De Bruijn cycles using a wildcard character, we introduce universal partial tori and matrices. We find them computationally and construct infinitely many of them using one-dimensional variants of universal cycles, including a new variant called a universal partial family.

## Data

This folder contains examples of upmatrices and uptori identified or constructed by the code in this repository. Each file contains a collection of objects for a particular combination of alphabet and subarray dimensions and is named accordingly. The general scheme for the name of the files is _object[s]-alphabet-rows-columns.txt_. For example, _upmatrix-2-3-4.txt_ would contain a single upmatrix for the binary alphabet whose subarrays have three rows and four columns. Likewise, _upmatrices-2-2-2.txt_ would contain more than one upmatrix for the binary alphabet whose subarrays have two rows and two columns. Note that the objects in a particular file may have different dimensions (e.g. _upmatrices-2-2-2.txt_ contains some upmatrices with 3 rows and 5 columns and some upmatrices with 4 rows and 4 columns).

Within the files, each individual obejct is formatted with a newline after each row and two newlines between objects. The _w_ character represents the "wildcard", which we usually represent as $\diam$ in our paper.

## Code

This folder contains libraries for manipulating cyclic combinatorial objects in one and two dimensions. The /apps folder contains programs used to generate examples in the paper.
