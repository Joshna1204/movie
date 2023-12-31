from django.shortcuts import render,redirect
from mov.models import Cards
from mov.forms import editform
# Create your views here.
def allcards(request):
    c=Cards.objects.all()
    return render(request,'cards.html',{'c':c})

def add_mov(request):
        if (request.method == "POST"):
            n = request.POST['n']
            d = request.POST['d']
            y = request.POST['y']
            img = request.FILES['img']
            c = Cards.objects.create(name=n, desc=d, year=y, img=img)
            c.save()
            return allcards(request)
        return render(request, 'movies.html')

def viewmov(request,p):
    c=Cards.objects.get(name=p)
    return render(request,'view.html',{'c':c})

def update(request,p):
    c=Cards.objects.get(name=p)
    form = editform(instance=c)
    if(request.method=="POST"):
        form = editform(request.POST,request.FILES,instance=c)
        if form.is_valid():
           form.save()
           return allcards(request)
    return render(request,'edit.html',{'form':form})

def delete(request,p):
    c=Cards.objects.get(name=p)
    c.delete()
    return allcards(request)