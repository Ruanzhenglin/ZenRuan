"""
step1:build index which is a list that contains many tuples.
step2:query the index and get hits 
step3:access offsets after obtain index hits
"""
import bisect


class Index(object):
    def __init__(self, t, k):
        self.k=k
        self.index=[]
        for i in range(len(t)-k+1):
            self.index.append((t[i:i+k], i))
        self.index.sort()

            
    def query(self, p):
        kmer=p[:self.k]
        i=bisect.bisect_left(self.index, (kmer, -1))
        hits=[]
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i+=1
        return hits
        
        
def queryIndex(p, t, index):
    k=index.k
    offsets=[]
    for i in index.query(p):
        if p[k:] == t[i+k:i+len(p)]:
            offsets.append(i)
    return offsets
    
    
#p='GCTA'
#t='ACGCTATCAG'
#index = Index(t, 3)
#print(queryIndex(p, t, index))