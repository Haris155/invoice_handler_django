from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def loginPage(request):
    return render(request, 'accounts/loginpage.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out, Successfully')
    # return render(request, 'accounts/loginpage.html')
    return redirect('loginpage')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{username}, You are Logged In, Successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Wrong Credentials, UserName or Password is InCorrect!!!!')
            return redirect('loginpage')
    return render(request, 'userlogin/loginpage.html')


