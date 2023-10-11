from django.shortcuts import render, redirect
from .models import Photo, Album
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import RegisterUserForm, AlbumForm, PhotoUploadForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Home
def home(request):
    albums = Album.objects.all()
    photos = []

    for album in albums:
        alb = Photo.objects.filter(album=album.id)
        if len(alb) > 0:
            photos.append(alb)

    return render(request, 'home.html', {'albums': albums,
                                         'photos': photos})

def gallery(request):
    photos = Photo.objects.filter(album=1)
    return render(request, 'gallery.html', {'photos': photos})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There Was An Error Logging In, Try Again...'))
            return redirect('login-user')
    else:
        return render(request, 'auth/login.html', {})

def register_user(request):
    return render(request, 'auth/register.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Were Logged Out'))
    return redirect('home')

def album_by_id(request, id):
    photos = Photo.objects.filter(album=id)
    return render(request, 'album.html', {'photos': photos})

def albums(request):
    albums = Album.objects.all()
    photos = []

    for album in albums:
        alb = Photo.objects.filter(album=album.id)
        if len(alb) > 0:
            photos.append(alb)

    return render(request, 'albums.html', {'albums': albums,
                                         'photos': photos})

def create_album(request):
    submitted = False
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user.id
            album.save()

            return HttpResponseRedirect('/create_album?submitted=True')
    else:
        form = AlbumForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'create_album.html',{'form':form, 'submitted':submitted})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            files = request.FILES.getlist('file')
            # date = str(datetime.now())
            user = request.user
            # print(date)
            for file in files:
                photo = Photo.objects.create(
                    name=file.name,
                    album=form.cleaned_data['album'],
                    file=file,
                    user=user,
                )
            # photo = form.save(commit=False)
            # photos.user = request.user
            # # photos.album =
            # photos.save()
            return render(request, 'albums.html', {})
        else:
            return render(request, 'upload_photo.html', {})
    else:
        form = PhotoUploadForm()
        return render(request, 'upload_photo.html', {'form': form})
