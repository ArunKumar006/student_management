from django.urls import path
from . import views


urlpatterns = [
    path('students',views.Students.as_view(),name="student_list"),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete-student'),
    path('students/details/', views.student_detail, name='student-details'),
    path('students/add_mark/', views.add_student_marks, name='mark-add'),
    path('students/individual/<int:stud_id>/', views.get_stud_details, name='detail-individual'),


]
