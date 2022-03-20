from operator import itemgetter
from django.shortcuts import render, redirect

# imported our models
from django.core.paginator import Paginator
from . models import Song

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



def music(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"music.html",context)

def home(request):
    return render(request, "home.html", {})

def contact(request):
    return render(request, "contact.html", {})



def login(request):
    return render(request, "login.html", {})

def search_songs(request):
    if request.method == "POST":
        searched = request.POST['searched']
        songs_searched = Song.objects.filter(title__contains=searched)

        return render(request, "search_songs.html", {'searched': searched, 'songs_searched': songs_searched})
    else: 
        return render(request, "search_songs.html", {})


def show_music(request, song_id):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}

    item = Song.objects.get(id=song_id)

    return render(request, "show_music.html", {'item': item, 'page_obj': page_obj})



def signup(request):
    return render(request, "signup.html", {})


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
 