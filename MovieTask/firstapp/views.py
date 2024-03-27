from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from firstapp.forms import FilmForm,TopicForm

from firstapp.models import Film, Topic


# Create your views here.

def base(request):
   return render(request,'base.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        pasword=request.POST['password']
        user=auth.authenticate(username=username,password=pasword)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            # messages.info('invalid user')
            return redirect('/')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/register/')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect('/')
                messages.info(request,'user created')
        else:
            messages.info(request,'password not matched')
            return  redirect('/')
            alert('registered succesfuly')
        return  redirect('/')
    return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def start(request):
    obj=Film.objects.all()
    return render(request,'home.html',{'final':obj})


def add(request):

    if request.method == 'POST':
        title=request.POST.get('title',)
        desc = request.POST.get('desc',)
        date = request.POST.get('date',)
        actors = request.POST.get('actors', )
        category=Topic.objects.get(id=1)
        url = request.POST.get('url', )
        review=request.POST.get('review',)
        rating=request.POST.get('rating',)
        img = request.FILES['img']
        movies=Film(title=title,desc=desc,date=date,actors=actors,url=url,category=category,review=review,rating=rating,img=img)

        movies.save();
        # films.save();
        return redirect('/')
    return render(request,'add.html')



def details(request,movie_id):
    obj1=Film.objects.get(id=movie_id)
    # return HttpResponse('this is no %s' % movie_id)
    return render(request,'details.html',{'result':obj1})


def update(request,id):
    movie=Film.objects.get(id=id)
    form=FilmForm(request.POST or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie=Film.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

