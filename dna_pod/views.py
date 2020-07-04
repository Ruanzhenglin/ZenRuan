from django.shortcuts import render
from .forms import DNAForm
# Create your views here.
from .string_process import longestCommonPrefix,match,naive,boyer_moore

from .bm_preproc import BoyerMoore

from .index_query import Index,queryIndex

from .approximate_matching import naiveHamming,globalAlignment,editDistance

def dna_page(request):
    if request.method == 'POST':
        form=DNAForm(request.POST)
        if form.is_valid():
            s1=request.POST['patterns']
            s2=request.POST['ref_text']
            method=request.POST['method']
            if method == 'longestCommonPrefix':
                results='string process results: ' + longestCommonPrefix(s1, s2)
            if method == 'match':
                results='two strings match result: ', match(s1, s2)
            if method=='naive':
                results='results of alignment via naive function: ',naive(s2, s1)
            if method=='boyer_moore':
                results='matched offsets are: ', boyer_moore(s1, BoyerMoore(s1),s2)
            if method=='index_query':
                results='offsets results: ', queryIndex(s1, s2, Index(s2, 3))
            if method=='naiveHamming':
                results='naive Hamming results :', naiveHamming(s1, s2, 3)
            if method=='globalAlignment':
                results='globalAlignment results: ', globalAlignment(s1, s2)
            if method=='editDistance': 
                results='editDistance results: ', editDistance(s1, s2)
            return render(request, 'dna_pod/dna_page.html', {'form': form,'results': results, 'method':method})
    else:
        form=DNAForm()

    return render(request, 'dna_pod/dna_page.html', {'form': form})




    
