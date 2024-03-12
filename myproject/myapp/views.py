from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
       'name': 'patrick',
       'age' : 23,
       'nationality': 'bristish'
     
   }
    return render(request, 'index.html', context)



def signup(request):
    return render(request, 'signup.html')


def counter(request):
    word =request.POST['text']
    text = word
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_of_words})