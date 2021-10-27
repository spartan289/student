from django.shortcuts import redirect, render
from accounts.models import tbl_user
from django.http import HttpResponse
from studentdetail.models import tbl_student1
from studentdetail.views import index

# Create your views here.
def register(request):
    '''
    This function is used to register the user
    Model: tbl_user
    
    '''
    if request.method=='POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user_Created = tbl_user.objects.create(username=user_name,password=pass_word)
        user_Created.save()
        return HttpResponse('User Created')
    else:
        return render(request, 'register.html')

def login(request):
    '''
    Login Function
    Validates username and password and redirects to home page, also sets session and user status to True
    '''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = tbl_user.objects.filter(username=username,password=password)
        if user:
            user.update(user_status=True)
            print(user.values())
            request.session['username'] = username
            
            id = user.values()[0]['id']
            print(id)
            if tbl_student1.objects.filter(student_id=id).exists():
                return redirect('/')

            return redirect('/index')
        else:
            return HttpResponse('Login Failed')
    else:
        return render(request, 'login.html')


def logout(request):
    '''
    Logout Function
    Sets user status to False and redirects to base page and terminates the session
    '''
    try:
        username = request.session['username']
        user = tbl_user.objects.filter(username=username)
        user.update(user_status=False)
        
        del request.session['username']
    except  KeyError:
        pass
    return redirect('base')
