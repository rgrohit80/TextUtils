# i have created
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('text')
    purpose = []
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if request.POST.get('removepunc'):
        analysed = ""
        purpose.append('Remove_punc')
        for char in text:
            if char not in punc:
                analysed += char
        text = analysed
    if request.POST.get('capitalize'):
        text = text.upper()
        purpose.append('Capitalize')

    if request.POST.get('extraspaceremover'):
        analyzed = ""
        purpose.append('Extra_Space_Remover')
        for index, char in enumerate(text):
            if text[index] == ' ' and text[index + 1] == ' ':
                pass
            else:
                analyzed += char
        text = analyzed
    params = {'purpose': purpose, 'analyzed_text': text}
    return render(request, 'analyze.html', params)


def exe(request):
    return render(request, 'exe.html')


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')
