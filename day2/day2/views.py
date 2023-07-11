from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def changer(request):
    return render(request, 'changer.html')

def analysis(request):
    data = request.GET.get('mytext', 'default')
    chak = request.GET.get('chak', 'off')
    if data == "":
        error = "Please enter your data"
        pramiter = {"error": error}
        return render(request, 'index.html', pramiter)
    elif chak == 'rmvp':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        my_str = data
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char
        par = {'data': no_punct}
        return render(request, 'analysis.html', par)
    elif chak == 'Capital':
        my_str = data
        no_punct = ""
        for char in my_str:
            if char in my_str:
                no_punct = no_punct + char.upper()
        par = {'data': no_punct}
        return render(request, 'analysis.html', par)
    elif chak == 'lower':
        my_str = data
        no_punct = ""
        for char in my_str:
            if char in my_str:
                no_punct = no_punct + char.lower()
        par = {'data': no_punct}
        return render(request, 'analysis.html', par)
    elif chak == 'countchar':
        my_str = data
        my_str = my_str.replace(" ", "")
        no_punct = len(my_str)
        par = {'data': no_punct}
        return render(request, 'analysis.html', par)
    elif chak == 'countspace':
        my_str = data
        no_punct = my_str.count(" ")
        par = {'data': no_punct}
        return render(request, 'analysis.html', par)
    else:
        error = "Please select a option"
        pramiter = {"error": error, 'textvalue': data}
        return render(request, 'index.html', pramiter)


def wordchanger(request):
   sentance=request.GET.get('sentance',"defualt")
   target=request.GET.get('target',"target")
   Change=request.GET.get('Change',"Change")
   if len(sentance)==0 or len(target)==0 or len(Change)==0:
       error="Enter all inputs please"
       parametar={'sentance':sentance,'target':target,'Change':Change,'error':error}
       return render(request, 'changer.html',parametar)
   else:
       if target in sentance:
           sentance=sentance.replace(target,Change)
           par = {'data': sentance}
           return render(request, 'analysis.html', par)
       else:
           error = "Target Word not found"
           parametar = {'sentance': sentance, 'target': target, 'Change': Change, 'error': error}
           return render(request, 'changer.html', parametar)