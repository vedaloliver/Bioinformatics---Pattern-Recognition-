import random
virus_file = 'lambda_virus.fa'
pattern = 'AGGAGGTT'

numreads = 0
readlen = 0
nummatched = 0



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
    occurrences = []
    # naive algorithm implementation
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
    # functionality to also look for reverse complement variation
    # this functionality was extended to remove complement variation if the pattern and reverse complement was the same
    occurrences = []
    # naive algorithm implementation
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
    # makes random reads from the given genome so we can test the matching algorithm without having to find a genome and corresponding reads

    reads = []
    for i in range(numreads):
        start = random.randint(0, len(genome)-readlen) - 1
        reads.append(genome[start: start+readlen])
    return reads


def read_checker(reads):
    # checks if the reads match the genome
    reads = ''
    choice = 0

    def algorithm_choice():
        global nummatched
        print('\nWhat algorithm do you want to check your reads against?')
        while True:
            print('\nGeneric Naive = 1\n\nNaive with reverse complement checks = 2\n\nNaive with mismatch allowance = 3\n\nExit Program = 4:')
            choice = ((input()))
            if choice == str(1):
                print('Executing generic naive algorithm.')
                for r in reads:
                    matches = naive(r, genome)
                    print(('%d / %d reads matched.' % (nummatched+1, len(reads))))
                    if len(matches) > 0:
                        nummatched += 1
                break
            elif choice == str(2):
                print('(NOT FINISHED FUNCTIONALITY.).')
                break
            elif choice == str(3):
                print('\nExecuting the naive algorithm with mismatch allowance.\n')
                for r in reads:
                    matches = naive_2mm(r, genome)
                    print(('%d / %d reads matched.' % (nummatched+1, len(reads))))
                    if len(matches) > 0:
                        nummatched += 1
                break
            elif choice == str(4):
                print('\nProgram terminated.\n')
                break
            else:
                print("Invalid. Please try again.")


    print('\nWelcome. Do you already have reads corresponding to the genome, or would you like us to randomly generate reads?\n')
    while True:
        print('Have reads = 1\n\nRandomly Generate reads = 2\n\nTerminate program = 3\n')
        choice = ((input()))
        if choice == str(1):
            print('(NOT FINISHED FUNCTIONALITY.).')
        elif choice == str(2):
            print('Starting random generation of reads.')
            reads = randomreads
            algorithm_choice()
            break
        elif choice == str(3):
            print('\nProgram terminated.\n')
            break
        else:
            print("Invalid. Please try again.")

        

    
    result = ('Finished. The result is: %d / %d reads matched.' % (nummatched, len(reads)))
    print (result)

# reads the genome for use in code bas
genome = readGenome(virus_file)
#generates random reads 
randomreads = generatereads(genome, 5, 100)

read_checker(randomreads)
# #print (reversecomplement(randomreads))

#generates a reverse complement for each randomly generated read
# for i in range(len(randomreads)):
#     print (reversecomplement(randomreads[i]))




#print(read_checker(randomreads))
#print (naive(pattern,reversecomplement(pattern), readGenome(virus_file)))
#print (naive_2mm(pattern, readGenome(virus_file)))
