from django.contrib import admin
from django.urls import path
from game.views import hello_views, jokes_views, main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_views),
    path("jokes/", jokes_views),
    path("", main_views)
]
