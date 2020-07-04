def longestCommonPrefix(s1, s2)->str:
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]
#longestCommonPrefix('ACCATGT','ACCAGAC')


def match(s1,s2)-> bool:
    match=True
    if len(s1)!=len(s2):
        match=False
        return match
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            match=False
            return match
    return match


def naive(t,p) -> list:
    occ=[]
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            if t[i+j] != p[j]:
                break
        else:
            occ.append(i)
    return occ
#naive('ACGCTGC', 'GC')


def boyer_moore(p, p_bm, t) -> list:
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

