from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from lxyapp.models import Book
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse('hello liuxinyang')


def book_detail(request):
    book_list=Book.objects.raw('select * from lxyapp_book ')
    context={'book_list':book_list}
    return render(request,'lxyapp/book_detail.html',context)

def addBook(request):
    if request.method=='POST':
        t_name=request.POST['name']
        t_author=request.POST['author']
        t_pub_house=request.POST['pub_house']
    from django.utils import timezone
    t_book=Book(name=t_name,author=t_author,pub_house=t_pub_house,pub_date=timezone.now())
    t_book.save()

    return HttpResponseRedirect(reverse('book_detail'))

def delBook(request,book_id):
    book_id=book_id
    Book.objects.filter(id=book_id).delete()

    return HttpResponseRedirect(reverse('book_detail'))

def updateBook(request,book_id):
    book_id=book_id
    mybook=Book.objects.filter(id=book_id)
    return HttpResponseRedirect(reverse('book_detail'))

    