from django.urls import path
from . views import login_page,login_view


urlpatterns = [
    path("", login_page, name='login_page'),
    path('login/', login_view, name='login'),

]
