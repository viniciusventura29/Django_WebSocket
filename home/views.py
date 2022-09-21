from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User

def index(request):
    return render(request,"index.html",{})

def room(request, room_name):
    return render(request,"chatroom.html", {
        'room_name' : room_name
    })
    
def register(request):
    if str(request.method) == 'POST':
        name = request.POST.get('nome_cad')
        email = request.POST.get('email_cad')
        nickname = request.POST.get('nickname_cad')
        first_password = request.POST.get('senha_cad1')
        second_password = request.POST.get('senha_cad2')
        
    try:
        validate_email(email)

    except:
        messages.error(request, 'Email Inválido')
        return render(request, 'register.html')

    if len(first_password)<6:
        messages.error(request, 'Senha deve ter no mínimo 6 digitos')
        return render(request, 'register.html')

    if second_password!=first_password:
        messages.error(request, 'Senhas diferentes! Tente novamente')
        return render(request, 'register.html')

    if User.objects.filter(username=nickname).exists():
        messages.error(request, 'Nome de usuário ja cadastrado! Tente novamente')
        return render(request, 'register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email ja cadastrado! Tente novamente')
        return render(request, 'register.html')
    
    

    novo_usuario = User.objects.create_user(
        username=nickname,
        first_name=name,
        email=email,
        password=first_password
        )
    
    novo_usuario.is_staff = True
    
    novo_usuario.save()
    
    return render(request,'register.html')

    
def login(request):
    if str(request.method) != 'POST':
        return render(request, 'login.html')

    else:
        username = request.POST.get('nickname_login')
        senha = request.POST.get('senha_login')

        user_login = auth.authenticate(
            username=username,
            password=senha,
        )

        if user_login:
            auth.login(request,user_login)
            return redirect('index')

        else:
            messages.warning(request,"Usuário não cadastrado!")
            return render(request, 'login.html')