from .bm_preproc import BoyerMoore

"""Approximate matching"""


def naiveHamming(p,t,maxDistance):
    occurences = []   
    for i in range(len(t)-len(p)+1):  #loop over alignments
        nmm=0
        for j in range(len(p)):       #loop over characters  
            if t[i+j] != p[j]:        #compare charactes
                nmm+=1
                if nmm > maxDistance:
                    break
        if nmm <= maxDistance:
            occurences.append(i)
    return occurences


def boyer_moore(p, p_bm, t):
    i=0
    occurences = []
    while i < len(t)-len(p)+1:
        shift=1
        mismatch=False
        for j in range(len(p)-1, -1, -1):
            if p[j] != t[i+j]:
                skip_bc=p_bm.bad_character_rule(j, t[i+j])
                skip_gs=p_bm.good_suffix_rule(j)
                shift=max(skip_bc, skip_gs, shift)
                mismatch=True
                break
        if not mismatch:
            occurences.append(i)
            skip_gs=p_bm.match_skip()
            shift=max(skip_gs, shift)
            
        i += shift
    return occurences


def approximate_match(p,t,n):
    segment_length=int(round(len(p)/(n+1)))
    all_matches=set()
    for i in range(n+1):
        start=i*segment_length
        end=min((i+1)*segment_length, len(p))
        p_bm=BoyerMoore(p[start:end],alphabet='ACGT')
        matches=boyer_moore(p[start:end],p_bm,t)
        
        for m in matches:
            if m<start or m-start+len(p)>len(t):
                continue
        
            mismatches=0
            for j in range(0,start):
                if p[j] != t[m-start+j]:
                    mismatches+=1
                    if mismatches > n:
                        break


            for j in range(end, len(p)):
                if p[j] != t[m-start+j]:
                    mismatches+=1
                    if mismatches > n:
                        break

            
            if mismatches<= n:
                all_matches.add(m-start)
    return list(all_matches)


def editDistance(x, y):
    D = []
    for i in range(len(x)+1):
        D.append([0]* (len(y) +1))
    
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = i
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y) +1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            
            D[i][j] = min(distHor, distVer, distDiag)
    
    return D[-1][-1]


alphabet = ['A', 'C', 'G', 'T']
score = [[0, 4, 2, 4, 8], \
         [4, 0, 4, 2, 8], \
         [2, 4, 0, 4, 8], \
         [4, 2, 4, 0, 8], \
         [8, 8, 8, 8, 8]
        ]


def globalAlignment(x, y):
    D = []
    for i in range(len(x)+1):
        D.append([0]* (len(y)+1))
    
    for i in range(1, len(x)+1):
        D[i][0] = D[i-1][0] + score[alphabet.index(x[i-1])][-1]
    for i in range(1, len(y)+1):
        D[0][i] = D[0][i-1] + score[-1][alphabet.index(y[i-1])]
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + score[-1][alphabet.index(y[j-1])]
            distVer = D[i-1][j] + score[alphabet.index(x[i-1])][-1]
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
            
            D[i][j] = min(distHor, distVer, distDiag)
    
    return D[-1][-1]


