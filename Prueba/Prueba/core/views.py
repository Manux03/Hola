from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin, FormularioUsuario, FormularioModifica, ItemForm,TipoItemForm
from django.views.generic import TemplateView, CreateView
from .models import Usuario, items, Tipoitems


class Inicio(TemplateView):
    template_name = 'index.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'registro.html'
    success_url = reverse_lazy('login')

def modifica(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FormularioUsuario()
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioModifica(instance=usuario)
        return render(request, "modifica.html", {'form': form})
    else:
        if id == 0:
            form = FormularioModifica(request.POST)
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioModifica(request.POST,instance= usuario)
        if form.is_valid():
            form.save()
        return redirect('lista')

def eliminar(request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('lista')

def lista (request):
    contexto = {'usuarioslista': Usuario.objects.all()}
    return render(request, 'lista.html',contexto)

def Modificaimagen(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ItemForm()
        else:
            Items = items.objects.get(pk=id)
            form = ItemForm(instance=Items)
        return render(request, "modificaitem.html", {'form': form})
    else:
        if id == 0:
            form = ItemForm(request.POST)
        else:
            Items = items.objects.get(pk=id)
            form = ItemForm(request.POST or None,request.FILES or None, instance = Items)
        if form.is_valid():
            form.save()
        return redirect('imagenp')


def Agregarimagen(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, "agregaritem.html", {'form': form})
    else:
        form = ItemForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('imagenp')


def imagenp(request):
    listaitems = {'listaitems': items.objects.all()}
    return render(request, 'itemslista.html',listaitems)

def eliminarimagen(request,id):
    Items = items.objects.get(pk=id)
    Items.delete()
    return redirect('imagenp')


def agregarcategoriaitem(request):
    if request.method == "GET":
        form = TipoItemForm()
        return render (request,"agregarcategoriaitem.html",{'form':form})
    else:
        form = TipoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('listaitems'))