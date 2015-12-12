from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    #returns a user object or None
    #only checks whether username and password are correct or not

    if user is not None: 
        auth.login(request,user) #actual login
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request) #logout the current user
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST': #check if data is posted or not
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        balance = request.POST.get('balance')
        user = UserDetails(username=username,password=password,email=email,balance=balance)
        form = MyRegistrationForm(instance=user) #pass all values in the POST dictionary to MyRegistrationForm

        if form.is_valid():
            form.save() #save details for new user
            return HttpResponseRedirect('/accounts/register_success')

    #what will be shown first time ie when data is not posted yet
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm() #blank form, no POST information in it
    return render_to_response('register.html',args)


def register_success(request):
    return render_to_response('register_success.html')
