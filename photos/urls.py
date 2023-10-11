from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('login_user', views.login_user, name='login-user'),
    path('register_user', views.register_user, name='register-user'),
    path('logout_user', views.logout_user, name='logout-user'),
    path('album/<id>', views.album_by_id, name='album-by-id'),
    path('albums', views.albums, name='albums'),
    path('create_album', views.create_album, name='create-album'),
    path('upload_photo', views.upload_photo, name='upload-photo'),
]