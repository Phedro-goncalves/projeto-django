from django.urls import path
from recipes.views import Home,contato,sobre




urlpatterns = [
    path('', Home), #home
    path('sobre/', sobre), #sobre
    path('contato/', contato), #contato

]