
from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, add_todo, signout, delete_todo, update_todo, contact


urlpatterns = [
    path('', home, name='home'),   #initial function to run home function
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('contact/', contact),
    path('add-todo/', add_todo),
    path('delete-todo/<int:id>', delete_todo),
    path('update-todo/<int:id>/<str:status>', update_todo),
    path('logout/',signout)
]
