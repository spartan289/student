from typing import TypeVar
from django.shortcuts import redirect, render
from studentdetail.models import tbl_student1
# Create your views here.
def index(request):
    '''
    This function is the form which is used to add the student details to the specific user which created it
    Model: tbl_student1
    

    '''
    try:
        username = request.session['username']
        if request.method=='POST':
            student_name = request.POST['student_name']
            college_name = request.POST['college_name']
            specialty = request.POST['special']
            degree = request.POST['degree']
            internship = request.POST['internship']
            phone_no = request.POST['phone_no']
            email = request.POST['email_id']
            address = request.POST['address']
            gender = request.POST['gender']
            notes = request.POST['notes']
            user_detail = tbl_student1.objects.create(
                student_name = student_name,
                student_college = college_name,
                specialization = specialty,
                degree_name = degree,
                internship_name = internship,
                student_email = email,
                student_phone = phone_no,
                student_address = address,
                student_gender = gender,
                notes = notes,
                username = username
            )
            user_detail.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {'username': username})
    except:
            return redirect('login')
    
        
