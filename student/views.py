from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.views import APIView
from .models import Student,Marks
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None):
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return None
        if user is not None and user.check_password(password):
            if user.is_active:
                return user
        return None

class Students(APIView):
    @method_decorator(login_required,)
    def get(self,request):

        students = Student.objects.values('id','name','candidate_code','programme',
                                                'academic_year','mark__internal_mark',
                                                'mark__external_mark')
        context = {'students': students}

        return render(request, 'home.html',context)
    @method_decorator(login_required,)
    def post(self,request):
        stud_serilizer=StudentSerializer(data=request.data)
        if stud_serilizer.is_valid():
            stud_serilizer.save()
        return Response({'stud_id':stud_serilizer.data['id']})




def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')  # Redirect to the students list page

    


def student_detail(request):
    
    Student_obj=Student.objects.get(id=request.GET.get('stud_id'))
    stud_ser=StudentSerializer(Student_obj).data
    context = {'students': stud_ser}

    return render(request,'add_mark.html',context)  # Redirect to the students list page


@api_view(['POST'])
def add_student_marks(request):
    data = request.POST

    if Marks.objects.filter(student_id=data.get('id')).exists():
        return Response("Mark already added for student")
    student_obj = Marks(student_id=data.get('id'),internal_mark=data.get('internal_mark'),external_mark=data['external_mark'])
    student_obj.save()
    return Response("success")

@api_view(['POST'])
def update_student(request):
    data = request.POST
    try:
        student_obj = Student.objects.get(id=data.get('id'))
        student_serilizer = student_serilizer(student_obj,data=request.data,partial=True)
        if student_serilizer.is_valid():
            student_serilizer.save()
        return Response(student_serilizer.data)
    except Student.DoesNotExist:
        return Response("Student not found")


@api_view(['GET','POST'])
def get_stud_details(request,stud_id):
    if request.method == "GET":
        try:
            student_obj = Student.objects.get(id=stud_id)
            student_serilizer = StudentSerializer(student_obj)
            students = Student.objects.values('id','name','candidate_code','programme',
                                            'academic_year','mark__internal_mark',
                                            'mark__external_mark')

            context = {'student': student_serilizer.data,'students':students}

            return render(request, 'home.html',context)
        
        except Student.DoesNotExist:
            return Response("Student not found")

    else:
        data = request.POST
        try:
            student_obj = Student.objects.get(candidate_code=data.get('candidate_code'))
            student_serilizer = StudentSerializer(student_obj,data=request.data,partial=True)
            if student_serilizer.is_valid():
                student_serilizer.save()
            return redirect('student_list')  # Redirect to the students list page
        except Student.DoesNotExist:
            return Response("Student not found")


