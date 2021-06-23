from django.http import HttpResponse
from django.shortcuts import render
import operator

# def home(request):
#     return HttpResponse('hello world')

def home (request):
    return render(request, 'index.html')

# def counter(request):
#     text =request.GET['text']
#     total = len(text.split())
#     return render(request, 'counter.html', {'total':total, 'text':text})


def counter(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1 
        sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'counter.html', {'fulltext' : fulltext, 'counter':len(wordlist), 'sortedword':sortedword})


