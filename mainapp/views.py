from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
from .planner import planner


# Create your views here.
@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        project_id = request.POST.get("todo-id")
        if project_id:
            project_to_delete = InFlowAIProject.objects.filter(id=project_id).first()
            if project_to_delete and (project_to_delete.user == request.user):
                project_to_delete.delete()
                messages.success(request, 'Project deleted successfully!')
                return redirect('/')
    user_todos = InFlowAIProject.objects.filter(user=request.user)
    return render(request, 'main/index.html', {'user_todos': user_todos})

def signup(request):
    logout(request)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = authenticate(username=form.data.get('username'), password=form.data.get('password1'))
                if user is None:
                    request.session['auth_token'] = otp_generator()
                    request.session['signup_data'] = form.data
                    send_otp(form.data.get('email'), request.session['auth_token'])
                    request.session.set_expiry(300)
                else:
                    messages.error(request, '''Seems like the account already exists, please go to /login.''')
                    return redirect('/signup')
                return redirect('/otp')
            except Exception as e:
                print(e)
    else:
        form = RegisterForm()
    
    # logout(request)

    return render(request, 'registration/signup.html', {"form": form})


def otp_generator():
    r1, r2, r3, r4, r5, r6 = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
    r = f'{r1}{r2}{r3}{r4}{r5}{r6}'
    return r


def send_otp(email, token):
    subject = 'Your OTP is here'
    msg = f'Here is your otp: {token}.'
    try:
        from_email = settings.EMAIL_HOST_USER
        recipients = [email]
        send_mail(subject, msg, from_email, recipients)
    except Exception as e:
        print(e)
        

def authenticate_user(userr_id):
    userr = UserProfile.objects.filter(user_id=userr_id).exists()
    
    return userr


def add_user(request):
    try:
        user = authenticate(username=request.session['email'], password=request.session['password'])
        if user is not None:
            login(request, user)
        if user is None:
            user = User.objects.create_user(username=request.session['email'], name=request.session['name'], email=request.session['email'])
            user.set_password(request.session['password'])
            user.save()
            
            custom_user = UserProfile.objects.create(user=user)
            custom_user.save()
    except Exception as e:
        print(e)


@login_required(login_url="/")
def logout_page(request):
    logout(request)
    return redirect('/')


def otp(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        try:
            if otp == request.session['auth_token']:
                data = request.session['signup_data']
                user = User.objects.create_user(first_name=data.get('first_name'), last_name=data.get('last_name'), username=data.get('username'), email=data.get('email'))
                user.set_password(data.get('password1'))
                user.save()

                custom_user = UserProfile.objects.create(userr=user, username=data.get('username'), email=data.get('email'), name=data.get('first_name'))
                custom_user.save()
                login(request, user)
                return redirect('http://127.0.0.1:8000/')
            else:
                messages.error(request, 'Invalid OTP')
        except Exception as e:
            print(e)        
    return render(request, 'registration/otp.html')


# def todo_ai_form(request):
#     if request.method == "POST":
#         prompt = request.POST.get('prompt')
#         assistant_response = planner(prompt)
#         return render(request, 'main/todo_ai_form.html', {'response': assistant_response})
#     return render(request, 'main/todo_ai_form.html')


# def save_project(request):
#     if request.method == "POST":
#         project_name = request.POST.get('project_name')
#         assistant_prompt = request.POST.get('response')
#         project_link = request.POST.get('project_link')
#         project = InFlowAIProject.objects.create(
#             user=request.user,
#             project_name=project_name,
#             assistant_prompt=assistant_prompt,
#             project_link=project_link
#         )
#         project.save()
#         messages.success(request, 'Project saved successfully!')
#         return redirect('/')
#     return redirect('/')


@login_required(login_url='/')
def project_page(request, slug):
    projects = InFlowAIProject.objects.filter(project_name=slug)
    project = get_object_or_404(projects, project_link=slug)
    return render(request, 'main/projectDashboard.html', {'project_name': project.project_name, 'prompt': project.assistant_prompt})


def todo_ai_form(request):
    if request.method == "POST":
        project_name = request.POST.get("project-name")
        project_prompt = request.POST.get("project-prompt")
        action = request.POST.get("action")  # <-- which button was pressed
        assistant_response = request.POST.get("response")

        if action == "ai":
            assistant_response = planner(project_prompt)
            project = InFlowAIProject.objects.create(
                user=request.user,
                project_name=project_name,
                assistant_prompt=assistant_response,
            )
            project.save()
            print(project_prompt, assistant_response)
            return render(request, 'main/todo_ai_form.html', {'response': assistant_response})
        elif action == "todo":
            messages.success(request, 'Project saved successfully!')
            return redirect('/')

    return render(request, "main/todo_ai_form.html")
