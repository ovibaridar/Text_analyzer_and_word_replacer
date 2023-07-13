from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')
def home2(request):
    return render(request, 'index2.html')


def changer(request):
    return render(request, 'changer.html')
def changer2(request):
    return render(request, 'changer2.html')
def analysis2(request):
    return render(request, 'analysis2.html')


def analysis(request):
    data = request.POST.get('mytext', 'default')
    chak = request.POST.get('chak', 'off')
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
        par = {'data': no_punct,'name':'Remove punctuations'}
        return render(request, 'analysis2.html', par)
    elif chak == 'Capital':
        my_str = data
        no_punct = ""
        for char in my_str:
            if char in my_str:
                no_punct = no_punct + char.upper()
        par = {'data': no_punct,'name':'All  Character is Capital'}
        return render(request, 'analysis2.html', par)
    elif chak == 'Wordcounter':
        my_str = data
        no_punct = my_str.count(" ")
        no_punct=int(no_punct)+1
        par = {'data': no_punct,'name':'Word Counter'}
        return render(request, 'analysis2.html', par)
    elif chak == 'Sentance_counter':
        my_str = data
        no_punct = my_str.count(".")
        no_punct=int(no_punct)
        par = {'data': no_punct,'name':'Sentance counter'}
        return render(request, 'analysis2.html', par)
    elif chak == 'lower':
        my_str = data
        no_punct = ""
        for char in my_str:
            if char in my_str:
                no_punct = no_punct + char.lower()
        par = {'data': no_punct,'name':'All  Character is Lower'}
        return render(request, 'analysis2.html', par)
    elif chak == 'countchar':
        my_str = data
        my_str = my_str.replace(" ", "")
        no_punct = len(my_str)
        par = {'data': no_punct,'name':'Charector counter'}
        return render(request, 'analysis2.html', par)
    elif chak == 'countspace':
        my_str = data
        no_punct = my_str.count(" ")
        par = {'data': no_punct,'name':'Space counter'}
        return render(request, 'analysis2.html', par)
    else:
        error = "Please select a option"
        pramiter = {"error": error, 'textvalue': data}
        return render(request, 'index.html', pramiter)


def wordchanger(request):
    sentance = request.POST.get('sentance', "defualt")
    target = request.POST.get('target', "target")
    Change = request.POST.get('Change', "Change")
    if len(sentance) == 0 or len(target) == 0 or len(Change) == 0:
        error = "Enter all inputs please"
        parametar = {'sentance': sentance, 'target': target, 'Change': Change, 'error': error}
        return render(request, 'changer.html', parametar)
    else:
        if target in sentance:
            sentance = sentance.replace(target, Change)
            par = {'data': sentance,'name':'Word changer'}
            return render(request, 'analysis2.html', par)
        else:
            error = "Target Word not found"
            parametar = {'sentance': sentance, 'target': target, 'Change': Change, 'error': error}
            return render(request, 'changer.html', parametar)
