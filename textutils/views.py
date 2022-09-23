from django.http import HttpResponse
from django.shortcuts import render
import string

pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def removepun(strg):
    strd = ''
    for i in strg:
         if i not in pun: strd+=i
    return strd

def charUp(strg):
    return (strg.upper())

def remSpace(strg):
    return (strg.replace(' ',''))

def remNxt(strg):
    strd=''
    for i in range(len(strg)):
        if not(strg[i] ==' ' and strg[i+1] == ' '):strd+=strg[i]
    return strd

def remNxtLn(strg):
    strd = ''
    for i in range(len(strg)):
        if not (strg[i] == '\n' or strg[i] == '\r'): strd += strg[i]
    return strd

def index(request):
    return render(request,'index.html')

def analyse(request):
    analysed_text = in_text = request.POST.get('text', 'default')
    if (request.POST.get('rempun', 'off')=='on'):
        analysed_text = removepun(analysed_text)
    if (request.POST.get('remspc', 'off')=='on'):
        analysed_text = remSpace(analysed_text)
    if (request.POST.get('remnxt', 'off')=='on'):
        analysed_text = remNxt(analysed_text)
    if (request.POST.get('remnxtln', 'off')=='on'):
        analysed_text = remNxtLn(analysed_text)
    if (request.POST.get('charup', 'off')=='on'):
        analysed_text = charUp(analysed_text)
    data = {'text':in_text,'analysed_text':analysed_text}
    return render(request,'analyse.html', data)
