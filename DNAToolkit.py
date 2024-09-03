Nucleotides = ['A','T','G','C'] # adenine (A), thymine (T), guanine (G), and cytosine (C)
import collections
def validateDNAseq(dna_seq):
    '''This function validates a DNA sequence'''
    dna_seq = dna_seq.upper()
    for nuc in dna_seq:
        if nuc not in Nucleotides:
            return False
    return dna_seq

def countNucleotides(dna_seq):
    '''This function counts the number of adenine (A), thymine (T), guanine (G), and cytosine (C) in a DNA sequence'''
    # return {'A': dna_seq.count('A'), 'T': dna_seq.count('T'), 'G': dna_seq.count('G'), 'C': dna_seq.count('C')}
    # return dict(collections.Counter(dna_seq))
    nucleotides_freq = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for nuc in dna_seq:
        nucleotides_freq[nuc] += 1
    return nucleotides_freq
    