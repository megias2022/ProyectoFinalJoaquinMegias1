from django.shortcuts import render
from django.views.generic import  ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from travel_blog_app.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from travel_blog_app.forms import UsuarioForm
from travel_blog_app.models import Avatar, Post, Mensaje
from django.contrib.auth.models import User





def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "travel_blog_app/index.html", {"posts": posts})

class AboutView(TemplateView):
    template_name = 'travel_blog_app/about.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'travel_blog_app/post_list.html'   

class PostDetalle(DetailView):
    model = Post 

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/travel_blog_app/listar"
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("travel_blog_app_listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("travel_blog_app_listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('travel_blog_app_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('travel_blog_app_listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('travel_blog_app_listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('travel_blog_app_listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('travel_blog_app_listar')

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("travel_blog_appp_mensajes_crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("travel_blog_app_mensajes_listar")

