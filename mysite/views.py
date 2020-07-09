from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Participant


# Create your views here.
import datetime
def rules(request):
    return render(request, 'mysite/rules.html')

def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname') #w nawiasie jest nazwa zmiennej z htmla index
        lname = request.POST.get('lname')
        gname = request.POST.get('gname')
        email = request.POST.get('email')
        year = request.POST.get('year')

        #wysyłanie do bazy danych wartości pod zmiennymi:
        u = Participant(firstname=fname,lastname=lname, groupname=gname, email=email, year=year)
        u.save()
    return render(request, 'mysite/index.html')

def form(request):
    if request.method == 'POST':
        fname = request.POST.get('fname') #w nawiasie jest nazwa zmiennej z htmla index
        lname = request.POST.get('lname')
        gname = request.POST.get('gname')
        email = request.POST.get('email')
        year = request.POST.get('year')

        #wysyłanie do bazy danych wartości pod zmiennymi:
        u = Participant(firstname=fname,lastname=lname, groupname=gname, email=email, year=year)
        u.save()
    return render(request, 'mysite/form.html')