from django.shortcuts import redirect, render
from studentdetail.models import tbl_student1
from accounts.models import tbl_user
# Create your views here.
def home(request):
    active_username = request.session['username']
    students = tbl_student1.objects.filter(username=active_username)
    return render(request, 'divdetail.html', {'students': students, 'username': active_username})



def user_records(request):
    try:
        active_username = request.session['username']

        if request.method=='POST':
            active_username = request.session['username']

            user_name = request.POST['user_name']
            students = tbl_student1.objects.filter(username=user_name).values()
            print(students)
            return render(request, 'search_user.html', {'students': students, 'username': active_username})

    except:
            return redirect('login')
    return render(request, 'search_user.html', {'username': active_username})

def base(request):
    try:
        active_username = request.session['username']
        return render(request, 'base.html', {'username': active_username})
    except:
        pass

    return render(request, 'base.html')
