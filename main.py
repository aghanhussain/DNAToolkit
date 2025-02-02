from DNAToolkit import *
import random

# Test Cases
rndDNAStr = 'ATTTGCTAA'

rndDNAStr1 = 'ATTTGCaagtcTAA'

rndDNAStr2 = 'AXTTTGCTAA'

'''
print(validateDNAseq(rndDNAStr))
print(validateDNAseq(rndDNAStr1))
print(validateDNAseq(rndDNAStr2))
'''
randDNAStr= ''.join([random.choice(Nucleotides) for nuc in range(20)])

validatedDNAStr = validateDNAseq(randDNAStr)

print(validatedDNAStr)
print(countNucleotides(validatedDNAStr))