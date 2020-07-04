import matplotlib.pyplot as plt


def reverseComplement(s):
    complement = {'A': 'T', 'C':'G','G':'C','T':'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
reverseComplement('ACCGTCG')


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
#genome = readGenome('/home/zen/workspace/python-dev/django_web/ZenRuan/datasets/lambda_virus.fa')
#genome[:100]


def baseCounts(genomefile):
    genome=readGenome(genomefile)
    counts={'A':0, 'G':0, 'C':0, 'T':0}
    for base in genome:
        counts[base]+=1
    print(counts)
    return counts


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences[:5], qualities[:5]
#seqs, quals = readFastq('SRR835775_1.first1000.fastq')
#print(seqs[:5])


def QtoPhred33(Q):
    """Turn Phred+33 ASCII-encoded quality"""
    return chr(int(Q) + 33)
    

def phred33ToQ(qual):
    return ord(qual)-33


def createHist(filename):
    qualities=readFastq(filename)[1]
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist
#h = createHist(quals)
#print(h)


def barHist(filename):
    h=createHist(filename)
    plt.bar(range(len(h)),h)

    fwrite_name='/home/zen/workspace/python-dev/django_web/ZenRuan/read_process/static/read_process/barHist.png'

    plt.savefig(fwrite_name)

    fname='read_process/barHist.png'

    return fname