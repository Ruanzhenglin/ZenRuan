from django.shortcuts import render
from .forms import DNAForm
# Create your views here.
def longestPrefix(s1, s2) -> str:
    if len(s1) < len(s2):
        longstr=s2
    else:
        longstr=s1
    for i in range(len(longstr)):
        if s1[i].upper() == s2[i].upper():
            i=i+1
        else:
            break
    return s1[:i]


def dna_page(request):
    if request.method == 'POST':
        form=DNAForm(request.POST)
        if form.is_valid():
            s1=request.POST['patterns']
            s2=request.POST['ref_text']
            results='DNA process results: ' + longestPrefix(s1, s2)
            return render(request, 'dna_pod/dna_page.html', {'form': form,'results': results})
    else:
        form=DNAForm()

    return render(request, 'dna_pod/dna_page.html', {'form': form})

    