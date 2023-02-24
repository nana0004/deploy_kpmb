from django.shortcuts import render
from Registration.models import Course, Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#### course
def index(request) :
    return render (request, "index.html")

#POST
def new_course(request) :
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data=Course(code=c_code, description=c_desc)      #mcm buat dekat cmd
        data.save()
        dict = {
            'message':'Data Saved'
        }
    else:
        dict = {
            'message':''
        }

    return render (request , "new_course.html", dict)

def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse': allcourse        #jadikan dictionary, apa2 data send to html must in dict
    }
    return render (request, 'course.html', dict)

#GET
def search_course(request):
    if request.method == 'GET':
        # nk filter by course
        data = Course.objects.filter(code = request.GET.get('c_code'))
        dict = {
            'data': data
        }
        return render (request, "search_course.html", dict)
    else:
        return render (request, "search_course.html")

#GET/PUT
def update_course(request,code):      #terima code dari course.html
    data=Course.objects.get(code=code)
    dict = {
        'data' : data
    }

    return render (request , "update_course.html", dict)

#POST
def save_update_course(request,code):
    c_description= request.POST['description']
    data=Course.objects.get(code=code)
    data.description = c_description
    data.save()
    return HttpResponseRedirect(reverse("course"))

#GET
def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))
    
    
#### student

#POST
def new_student(request):
    allcourse=Course.objects.all()
    if request.method=='POST':
        s_id = request.POST['s_id']
        s_name = request.POST['s_name']
        s_address = request.POST['s_address']
        s_phone = request.POST['s_phone']
        s_course = request.POST['s_course']

        #get foreign key data from reference table
        s_code= Course.objects.get(code=s_course)
        data= Student(stud_ID=s_id, name=s_name, address=s_address, phone_No=s_phone, course_code=s_code)
        data.save()
        dict={
            'allcourse': allcourse,
            'message': "Data saved"
        }

    else:
        dict={
            'allcourse': allcourse
        }

    return render (request, 'new_student.html', dict)

#GET
def search_by_course(request):
    allcourse = Course.objects.all()
    if request.method=='GET':
        data = Student.objects.filter(course_code=request.GET.get('courseCode'))
        num_stud = len(data)
        dict = {
            'data': data,
            'student': data,
            'allcourse': allcourse,
            'course': request.GET.get('courseCode'),
            'num_stud': num_stud,
        }
    else:
        dict = {
            'allcourse': allcourse
        }
    return render (request, 'search_by_course.html', dict)
