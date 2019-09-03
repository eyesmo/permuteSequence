
# coding: utf-8

# In[ ]:


#Permutation Examples to demonstrate functionality

#Return all DNA permutations 3 nucleotides long
testPermute1 = genSeqPermutations(seqLen = 3,
                                 seqToExtendFrom = '',
                                 baseSet = ['A', 'G', 'C', 'T'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = False,
                                 minPermuteSeqLen = 3)

#Return all DNA permutations 2 and 3 nucleotides long
testPermute2 = genSeqPermutations(seqLen = 3,
                                 seqToExtendFrom = '',
                                 baseSet = ['A', 'G', 'C', 'T'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = False,
                                 minPermuteSeqLen = 2)


testPermute3 = genSeqPermutations(seqLen = 3,
                                 seqToExtendFrom = '',
                                 baseSet = ['A', 'G', 'C', 'T'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = True)

#Can append the permutations to a constant previous sequence
testPermute4 = genSeqPermutations(seqLen = 3,
                                 seqToExtendFrom = 'GATTACA',
                                 baseSet = ['A', 'G', 'C', 'T'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = True)

#Works for subsets of nucleotides, or for RNA nucleotides
testPermute5 = genSeqPermutations(seqLen = 3,
                                 seqToExtendFrom = '',
                                 baseSet = ['G', 'U'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = True)

#Works for protein
testPermute5 = genSeqPermutations(seqLen = 3,
                                 seqToExtendFrom = '',
                                 baseSet = ['G', 'U'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = True)

print testPermute1[0:12]
print testPermute2[0:12]
print testPermute3[0:12]
print testPermute4[0:12]
print testPermute5[0:12]

testPermute6 = genSeqPermutations(seqLen = 12,
                                 seqToExtendFrom = '',
                                 baseSet = ['A', 'G', 'C', 'T'],
                                 preventTooManyPerms = True,
                                 tooManyPerms = 1000000,
                                 returnAllSeqLens = True)

