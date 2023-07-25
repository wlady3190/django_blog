from django.forms.models import BaseModelForm
from django.shortcuts import render

from django.http import HttpResponse

# Luego de agregar datos por la shell
from .models import Post

# modificar posts
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Autenficación en clases
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# posts = [
#     {
#         'author': 'Wlady',
#         'title': 'Blog Post 1',
#         'content': 'Primer contenido',
#         'date_posted': 'Agosto 27, 2000'
#     },
#      {
#         'author': 'Lili',
#         'title': 'Blog Post 2',
#         'content': 'Segundo contenido',
#         'date_posted': 'Julio 27, 2000'
#     }

# ]
# Modificando posts


def home(request):
    context = {
        # Luego de importar .models, se asigna los registros con Post.objects.all()
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_viewtype.html
    context_object_name = 'posts'  # el contexto es el mismo de def home() de arriba
    ordering = ['-date_posted']  # - RECIENTE PRIMERO
    #paginacion
    paginate_by=2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # override de form_valid

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # override de form_valid

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # eviar que editen publicaciones ajenas
    def test_func(self):
        post = self.get_object()
        # Para ver si el que quiere editar es el autor
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #Por defecto, reconoce a la plantilla terminada en _confirm_delete.html
    #para cambiar: template_name: 'plantilla.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # Para ver si el que quiere editar es el autor
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
