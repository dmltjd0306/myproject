# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('todolist/', views.todolist, name='todolist'),
]
# myproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('Homepage.urls')),  # Include the myapp.urls
]
