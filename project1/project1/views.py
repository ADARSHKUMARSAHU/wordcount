from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hi Adarsh Kumar")
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','default')

#    ----------------------------------- # check which checkbox is on-------------------------------
    removepunc =request.POST.get('removepunc','off')
    newlineremover =request.POST.get('newlineremover','off')
    # extraspaceremover =request.POST.get('extraspaceremover','off')
    fullcaps =request.POST.get('fullcaps','off')
    charcount =request.POST.get('charcount','off')
    print(removepunc)
    print(text)
    if removepunc =="on":
        analyzed =text
        Punctuations = '''!()-[]{}:;'"\.<>./?@#$%^&*_-'''
        analyzed = ""
        txt =text
        for char in text:
            if char not in Punctuations:
                analyzed = analyzed + char

        params ={"purpose":"Removed Punctuations" , "txt":txt , "analyed_text":analyzed}
        text =analyzed
        # return render(request,"analyze.html",params)
    if(fullcaps =="on"):   
        analyzed =""
        txt =text
        for char in text:
            analyzed =analyzed + char.upper()
        params ={"purpose":"Characters in Uppercase" , "txt":txt ,"analyed_text":analyzed}
        # return render(request,"analyze.html",params)
        text =analyzed

    if(newlineremover=="on"):
        analyzed =""
        txt =text
        for char in text:
            if char !="\n" and char !="\r":
                analyzed =analyzed + char
        params ={"purpose":"New Lines Removed" , "txt":txt , "analyed_text":analyzed}
        # return render(request,"analyze.html",params)
        text =analyzed

    # if(extraspaceremover=="on"):
    #     analyzed = ""
    #     txt =text
    #     for index , char in enumerate(text):
    #         if not(text[index] == " " and text[index + 1] ==" "):
    #             analyzed = analyzed + char
    #     params ={"purpose":"Extra Space Removed" , "txt":txt , "analyed_text":analyzed}
    #     # return render(request,"analyze.html",params) 
    #     text =analyzed

    if(charcount=="on"):
        txt =text 
        list_len = len(text)
        params ={"purpose":"Removed Punctuations" ,"txt":txt, "analyed_text":list_len}
        # return render(request,"analyze.html",params) 
        text =analyzed
    # else:
    #     return HttpResponse("<script>alert('Error')</script>")

    if(removepunc !="on" and fullcaps !="on" and newlineremover!="on" and charcount !="on" and extraspaceremover=="on"):
        return HttpResponse("Please Select Any one Checkbox")
    return render(request,"analyze.html",params)
        