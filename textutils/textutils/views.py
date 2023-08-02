# I have created a new file - Atul

## Code for video no. - 6

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>Hello, world. You're at the polls index. Welcome Atul!<h1> <a href= 'https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9' > Django CodeWithHarry</a> , <a href="https://chat.openai.com/"> ChatGPT</a> , <a href= 'https://www.google.com/maps' > Google Maps</a> , <a href= "https://www.sarkariresult.com/" > SarkariResult</a>''')



## Code for video no. - 7 and 11(Exercises 1)

# from django.http import HttpResponse

# def index(request):
#     nag = '''<h1>Atul Home</h1>
#       <a href="http://127.0.0.1:8000/removepunc" > REMOVE PUNC
#       </a>
#         <br>
#           <a href="http://127.0.0.1:8000/capitalizefirst" >CAP FIRST
#           </a> 
#         <br>
#           <a href="http://127.0.0.1:8000/newlineremove" >NEWLINE REMOVER
#           </a>
#         <br>
#           <a href="http://127.0.0.1:8000/spaceremove" >SPACE REMOVER
#           </a>
#         <br>
#           <a href="http://127.0.0.1:8000/charcount" >CHARCOUNT
#           </a>
#           '''
#     return HttpResponse(nag)



# def removepunc(request):
#     return HttpResponse('Atul Removepunc <br> <a href="http://127.0.0.1:8000"> BACK </a>')

# def capfirst(request):
#     return HttpResponse('Atul capitalizeFirst <br> <a href="http://127.0.0.1:8000"> BACK </a>')

# def newlineremove(request):
#     return HttpResponse('Atul newlineremover <br> <a href="http://127.0.0.1:8000"> BACK </a>')

# def spaceremove(request):
#     return HttpResponse('Atul spaceremover <br> <a href="http://127.0.0.1:8000"> BACK </a>')

# def charcount(request):
#     return HttpResponse('Atul charcount <br> <a href="http://127.0.0.1:8000"> BACK </a>')



# ## Code for video no. - 8

# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     params = {'name': 'Harry', 'place':'Mars'}
#     return render(request, 'index.html',params)



## Code for video no. - 9

# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html',)

# def removepunc(request):
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse('Atul Removepunc <br> <a href="http://127.0.0.1:8000"> BACK </a>')


## Code for video no. - 10

# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html',)

# def analyze(request):
#     djtext = request.GET.get('text','default')
#     removepunc = request.GET.get('removepunc','off')
#     print(djtext)
#     print(removepunc)
#     # analyzed = djtext
#     if removepunc == 'on':
#         punctuationslist = '''~`!@#$%^&*()_-=+{}[]|\:;"'<>,./?'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuationslist:
#                 analyzed = analyzed + char

#         params = {'purpose':"Removed Punctuations",'analyzed_text':analyzed}
#         return render(request, 'analyze.html',params)
#     else :
#         return HttpResponse('Atul Error <br> <a href="http://127.0.0.1:8000"> BACK </a>')


## Code for video no. - 12


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def analyze(request):

    # Get the text
    djtext = request.GET.get('text','default')

    # check checkbox values
    djremovepunc = request.GET.get('removepunc','off')
    djfullcaps = request.GET.get('fullcaps','off')
    djnewlineremove = request.GET.get('newlineremove','off')
    djextraspaceremove = request.GET.get('extraspaceremove','off')
    djcharcount = request.GET.get('charcount','off')

    # check which checkbox is on
    if djremovepunc == 'on':
        punctuationslist = '''~`!@#$%^&*()_-=+{}[]|\:;"'<>,./?'''
        analyzed = ""
        for char in djtext:
            if char not in punctuationslist:
                analyzed = analyzed + char

        params = {'purpose':"Removed Punctuations",'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    
    elif djfullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':"Uppercase",'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    
    elif djnewlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char

        params = {'purpose':"New Line Removed",'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    
    elif djextraspaceremove == 'on':
        analyzed = ''
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose':"Extra Space Removed",'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    
    elif djcharcount == 'on':
        analyzed = ''
        for char in djtext:
            char_length = len(djtext)
            print(char_length)
            analyzed = analyzed + str(char_length)

            params = {'purpose':"Char Count",'analyzed_text':analyzed  }
            return render(request, 'analyze.html', params )



    else :
        return HttpResponse('Atul Error <br> <a href="http://127.0.0.1:8000"> BACK </a>')





