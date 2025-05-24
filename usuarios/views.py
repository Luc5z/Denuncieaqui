from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, Denuncia
from django.contrib import auth
import re

def is_valid_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)

    cpf_repetido = cpf == cpf[0] * len(cpf)
    if cpf_repetido:
        return False

    multiplicador = 10
    soma_total = 0
    for numero in cpf[:9]:
        soma_total += int(numero) * multiplicador
        multiplicador -= 1

    primeiro_numero = (soma_total * 10) % 11
    primeiro_numero = primeiro_numero if primeiro_numero <= 9 else 0

    # Verificar o segundo dígito do CPF
    multiplicador = 11
    soma_total = 0
    for numero in cpf[:10]:
        soma_total += int(numero) * multiplicador
        multiplicador -= 1

    segundo_numero = (soma_total * 10) % 11
    segundo_numero = segundo_numero if segundo_numero <= 9 else 0

    cpf_temp = cpf[:9] + str(primeiro_numero) + str(segundo_numero)

    return cpf_temp == cpf


def generate_username(email):
    username = email
    return username

    
def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('inicio')
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        cpf = request.POST.get('cpf')

        if not is_valid_cpf(cpf):
            messages.error(request, 'CPF inválido.')
            return redirect('/usuarios/cadastro')

        if not (nome and sobrenome and email and senha and confirmar_senha and cpf):
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('/usuarios/cadastro')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.error(request, 'A senha deve ter pelo menos 6 caracteres.')
            return redirect('/usuarios/cadastro')

        if CustomUser.objects.filter(cpf=cpf).exists():
            messages.error(request, 'Este CPF já está cadastrado.')
            return redirect('/usuarios/cadastro')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Este E-mail já está cadastrado.')
            return redirect('/usuarios/cadastro')

        username = generate_username(email)

        usuario = CustomUser.objects.create_user(
            username=username,
            first_name=nome,  
            last_name=sobrenome,
            email=email,
            password=senha,
            cpf=cpf
        )

        usuario.save()

        messages.success(request, 'Cadastro realizado com sucesso. Faça o login.')
        return redirect('usuarios:login')


def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('inicio')
        return render(request, 'login.html')
    
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=email, password=senha)
        print(request.user)
        print(senha)
        if user:
            auth.login(request, user)
            print(request.user)
            return redirect('/')
        
        messages.error(request, 'E-mail ou senha inválidos')
        return redirect('usuarios:login')
    

def denuncia(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('redirecionamento')  
        return render(request, 'denuncia.html')
    
    elif request.method == 'POST':
        tipo_denuncia = request.POST.get('tipo_denuncia')
        descricao = request.POST.get('descricao')
        localizacao = request.POST.get('local_denuncia')
        
        # Processar a imagem, se necessário
        imagem = request.FILES.get('imagem_denuncia')

        # Salvar os dados no banco de dados
        # Supondo que o usuário esteja autenticado e você tenha acesso a ele através de request.user
        denuncia = Denuncia.objects.create(
            user=request.user,
            tipo_denuncia=tipo_denuncia,
            imagem=imagem,
            descricao=descricao,
            local_denuncia=localizacao
        )

        # Redirecionar para alguma página de confirmação
        messages.success(request, 'Denúncia realizada com sucesso. Aguarde a validação.')
        return redirect('/usuarios/denuncia')


def historico(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('redirecionamento')
    
    denuncias = Denuncia.objects.filter(user=request.user)

    return render(request, 'historico.html', {'denuncias': denuncias})


def sair(request):
    if not request.user.is_authenticated:
            return redirect('inicio')  
    
    auth.logout(request)

    return redirect('/usuarios/login')


 