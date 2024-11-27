from django.urls import path

from apps.views import hello_world_view

urlpatterns = [
    path('hello/', hello_world_view, name='hello-world'),

]
