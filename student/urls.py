from django.urls import path
from . import views


urlpatterns = [
    path('students',views.Students.as_view(),name="student_list"),

]
