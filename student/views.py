from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
class Students(APIView):
    def get(self,request):

        students = Student.objects.values('id','name','candidate_code','programme',
                                                'academic_year','mark__internal_mark',
                                                'mark__external_mark')
        context = {'students': students}

        return render(request, 'home.html',context)
    
    def post(self,request):
        print(request.data)
        stud_serilizer=StudentSerializer(data=request.data)
        if stud_serilizer.is_valid():
            stud_serilizer.save()
            print("saved")
        students = Student.objects.values('id','name','candidate_code','programme',
                                                'academic_year','mark__internal_mark',
                                                'mark__external_mark')
        context = {'students': students}
        print(students)

        return render(request, 'home.html',context)




from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_view(request):
    # Your view code here
    return render(request, 'my_template.html')
