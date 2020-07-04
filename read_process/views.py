from django.shortcuts import render
from .forms import readForm
from .reads_parse import reverseComplement,readGenome,baseCounts,readFastq,QtoPhred33,phred33ToQ,createHist,barHist

# Create your views here.
def read_process(request):
    if request.method == 'POST':
        form=readForm(request.POST)
        if form.is_valid():
            keyword=request.POST['keyword']
            process=request.POST['process']
            if process=='reverseComplement':
                results='DNA process result: ', reverseComplement(keyword)
            if process=='readGenome':
                results='Genome content is: ', readGenome(keyword)
            if process=='baseCounts':
                results='Genome base counts results: ', baseCounts(keyword)
            if process=='readFastq':
                results='Fastq sequence results: ', readFastq(keyword)
            if process=='QtoPhred33':
                results='Phred33 value is: ', QtoPhred33(keyword)
            if process=='phred33ToQ':
                results='Q value is: ', phred33ToQ(keyword)
            if process=='createHist':
                results='hist  of qualities results: ', createHist(keyword)
            if process=='barHist':
                #results='hist photogram: ', f"<img src={barHist(keyword)} alt='Hist bar of qualities'>"
                results=f"""<img src='/static/{barHist(keyword)}' alt='Hist bar of qualities'>"""
                #results=f"""<img src={barHist(keyword)} alt='Hist bar of qualities'>"""
                #results=f"""<img src='{{HistBar.histGram.url}}' alt='Hist bar of qualities'>"""
            return render(request, 'read_process/read_process.html', {'form': form,'results': results, 'process':process})
    else:
        form=readForm()

    return render(request, 'read_process/read_process.html', {'form': form})