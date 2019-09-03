
# coding: utf-8

# In[ ]:


#Method for permuting a DNA sequence of a specified length
#Technically, this method should be able to generate all possible strings of any given set of characters,
#just by changing the baseSet. So this could be used to permute protein or RNA sequences as well.
def permuteSeq(seqLen,
               seqToExtendFrom = '',
               baseSet = ['A', 'G', 'C', 'T'],
               preventTooManyPerms = True,
               tooManyPerms = 1000000):

    if((len(baseSet) ** seqLen > tooManyPerms) & (preventTooManyPerms == True)):
        print 'Requested sequence length is too long! Will generate >' + str(tooManyPerms) + ' sequence permutations.'
    else:
        seqSet = []
        if seqLen == 0:
            return seqSet
        for i in range(len(baseSet)):
            appendedSeq = seqToExtendFrom + baseSet[i]
            #print appendedSeq
            
            seqSet.extend(permuteSeq(seqLen-1,
                                     seqToExtendFrom = appendedSeq,
                                     baseSet = baseSet,
                                     preventTooManyPerms = False))
            seqSet.append(appendedSeq)
                
        return seqSet

