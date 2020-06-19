from django.shortcuts import render
from django.http import HttpResponse
from lxyapp.models import Book
# Create your views here.

def index(request):
    return HttpResponse('hello liuxinyang')


def book_detail(request):
    book_list=Book.objects.raw('select * from lxyapp_book limit 1')
    context={'book_list':book_list}
    return render(request,'lxyapp/book_detail.html',context)