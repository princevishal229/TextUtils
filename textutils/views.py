#I have created this website-Harry
from django.http import HttpResponse
from django.shortcuts import render






def index(request):
    return render(request,'index.html')

     #return HttpResponse("Home")











def analyze(request):
    #GET THE TEXT
    djtext = request.POST.get('text','default')
    print(djtext)

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    #Check which checkbox is on

    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params ={'purpose':'Removed Punctuations','analyzed_text':
    analyzed}
        return render(request,'analyze.html',params)

    elif (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': "Changed to UpperCase", 'analyzed_text':
    analyzed}
            # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
         if char !="\n" and char!="\r":
            analyzed = analyzed + char

        params = {'purpose': "Removed NewLines", 'analyzed_text':
            analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " "  and djtext[index+1] ==""):
                 analyzed = analyzed + char

        params = {'purpose': "Removed NewLines", 'analyzed_text':
            analyzed}
        # ANALYZE THE TEXT
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")




