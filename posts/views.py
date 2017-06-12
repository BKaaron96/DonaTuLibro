from django.shortcuts import render

from posts.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.

def login(request):
    message= None
    if request.method == 'POST': #No estan enviando el formulario
        usuario_post=request.POST['usuario']
        contraseña_post=request.POST['contraseña']
        user = authenticate( usuario = usuario_post , contraseña = contraseña_post)
        if user is not None:
         login_django( request, user)
         return redirect('dona:inicio')
       else:
         message="Usuario o contraseña incorrectos"

    form=LoginForm()
    context={
    'form' : form ,
    'message' : message
    }
    return render(request,'registro/login.html',context)


@csrf_protect
def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            telefono=form.cleaned_data['telefono'],
            dni=form.cleaned_data['dni'],
            usuario=form.cleaned_data['usuario'],
            contra=form.cleaned_data['contraseña1'],
            correo=form.cleaned_data['correo']
            tipo_de_usuario=form.cleaned_data['tipodeusuario'],
            colegios=form.cleaned_data['colegio'],
            )
            return HttpResponseRedirect('/posts/registro/registroexitoso/')
    else:
        form = RegistrationForm()
    variables = {
    'form': form
    }
    template = get_template('registro/registro.html')
    return HttpResponse(template.render(variables, request))
def registroexitoso(request):
    template = get_template('registro/registroexitoso.html')
    variables = {}
    return HttpResponse(template.render(variables, request))

def logoutp(request):
    logout(request)
    return HttpResponseRedirect('/posts/login/')

def inicio(request):
    return render(request,'inicio.html')

@login_required
def inicioA(request):
    variables={
    'user': request.user
    }
    template = get_template('inicioA.html')
    return HttpResponse(template.render(variables,request))
