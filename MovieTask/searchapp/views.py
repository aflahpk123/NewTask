from django.shortcuts import render
from  firstapp.models import Film
from  django.db.models import Q
# Create your views here.

def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Film.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query))
        return render(request,'search.html',{'query':query,'products':products})

