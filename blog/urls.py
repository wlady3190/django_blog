from django.urls import path
#modiuficr post
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView,
                    PostDeleteView)

from . import views


urlpatterns =[
    # path('', views.home, name='blog-home'),
    #Modificar Post
    path('', PostListView.as_view(), name='blog-home'),
    # creando ruta de PostDetailVIew
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #Creando PostCreateVIew
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    #actualizar Post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #eliminar post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    

    path('about/', views.about, name='blog-about'),
          
]

# <app> / <model>_<viewtype>.html
