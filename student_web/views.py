from django.shortcuts import redirect, render
from studentdetail.models import tbl_student1
from accounts.models import tbl_user
# Create your views here.
def home(request): #Displaying Records
    try:
        active_username = request.session['username']
        '''
        Taking all the records from the database and displaying the records of logged in user.

        '''
        students = tbl_student1.objects.filter(username=active_username)
        return render(request, 'divdetail.html', {'students': students, 'username': active_username})
    except:
        return redirect('login')



def user_records(request):
    '''
    Taking the username from the form and displaying all the student records of that user
    we are using session to get the active user
    '''
    try:
        active_username = request.session['username']

        if request.method=='POST':

            user_name = request.POST['user_name']
            students = tbl_student1.objects.filter(username=user_name).values()
            print(students)
            return render(request, 'search_user.html', {'students': students, 'username': active_username})

    except:
            return redirect('login')
    return render(request, 'search_user.html', {'username': active_username})

def base(request):
    '''
    Redirecting to the base page
    '''
    try:
        active_username = request.session['username']
        return render(request, 'base.html', {'username': active_username})
    except:
        pass

    return render(request, 'base.html')
