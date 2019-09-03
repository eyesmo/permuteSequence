
# coding: utf-8

# In[ ]:


#And now, here's a connected function that enables the filtering of the output permutation list
#By the length of the output sequence
def genSeqPermutations(seqLen,
                       seqToExtendFrom = '',
                       baseSet = ['A', 'G', 'C', 'T'],
                       preventTooManyPerms = True,
                       tooManyPerms = 1000000,
                       returnAllSeqLens = False,
                       minPermuteSeqLen = 0):
    
    permutationList = permuteSeq(seqLen = seqLen,
                                 seqToExtendFrom = seqToExtendFrom,
                                 baseSet = baseSet,
                                 preventTooManyPerms = preventTooManyPerms,
                                 tooManyPerms = tooManyPerms)
    if(returnAllSeqLens):
        return permutationList
    else:
        return [seq for seq in permutationList if len(seq) >= minPermuteSeqLen]

