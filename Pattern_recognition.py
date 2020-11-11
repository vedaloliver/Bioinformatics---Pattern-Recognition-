import random
virus_file = 'lambda_virus.fa'
pattern = 'AGGAGGTT'

numreads = 0
readlen = 0


def readGenome(filename):
    # parses the reference genome from the file in FASTA
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def readFastq(filename):
    # Takes individual read data and takes out only the base sequence and quality score
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skips lines 1 and 3
            seq = fh.readline().rstrip()  # base sequence
            fh.readline()
            qual = fh.readline().rstrip()  # base quality line
            if len(seq=0):
                break
            sequences.append(seq)
            qualities.append(qual)
        return sequences, qualities


def reversecomplement(read):
    # The user may not be aware if the reads are going to be in either
    # normal or cDNA, this covers both bases (pardon the pun)
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    t = ''
    for base in read:
        t = complement[base] + t
    return t


def naive(p, t):
    # to determine if the pattern being looked for is in the full strand
    # includes functionality to also look for reverse complement variation
    # this functionality was extended to remove complement variation if the pattern and reverse complement was the same
    occurrences = []
    # naive algorithm
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
        if match:
            occurrences.append(i)

    return occurrences, len(occurrences)


def naive_with_reverse(p, p_rev, t):
    # to determine if the pattern being looked for is in the full strand
    # includes functionality to also look for reverse complement variation
    # this functionality was extended to remove complement variation if the pattern and reverse complement was the same
    occurrences = []
    # naive algorithm
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
        if match:
            occurrences.append(i)
    # naive algorithm applied to the reverse complement; not utilising if pattern == rev_complement
    if pattern != (reversecomplement(pattern)):
        for i in range(len(t) - len(p_rev) + 1):
            match = True
            for j in range(len(p_rev)):
                if not t[i+j] == p_rev[j]:
                    match = False
            if match:
                occurrences.append(i)

    return occurrences, len(occurrences)


def naive_2mm(p, t):
    # Variance of naive algorithm searches for patterns in sequence which have variation of two
    # example Dog and god has a mismatch of two, Oliver and Pliver have a mismatch of one
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        mismatch = 0
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatch += 1
            if mismatch > 2:
                match = False
                break
        if match:
            occurrences.append(i)
    return len(occurrences), occurrences


def generatereads(genome, numreads, readlen):
    # makes random reads from the given genome so we can test the matching algortihm without having to find a genome and corresponding reads

    reads = []
    for i in range(numreads):
        start = random.randint(0, len(genome)-readlen) - 1
        reads.append(genome[start: start+readlen])
    return reads


def read_checker(reads):
    # checks if the reads match the genome
    nummatched = 0
    for r in reads:
        matches = naive(r, genome)
        print(matches)
        if len(matches) > 0:
            nummatched += 1

    result = ('%d / %d reads matched exactly.' % (nummatched, len(reads)))
    return result


genome = readGenome(virus_file)

randomreads = generatereads(genome, 10, 100)
print(randomreads)
print(read_checker(randomreads))
#print (readGenome(virus_file))
#print (naive(pattern,reversecomplement(pattern), readGenome(virus_file)))
#print (naive_2mm(pattern, readGenome(virus_file)))
