"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from final_app.views import index, PostList, PostBorrar, PostDetalle, PostActualizar, PostCrear, UserSignUp, UserLogin, UserLogout, AvatarActualizar,UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar, MensajeBorrar, AboutView
from django.contrib.admin.views.decorators import staff_member_required 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('final_app/', index, name="final_app_index"),
    path('final_app/about/', AboutView.as_view(), name="final_app_about"),
    path('final_app/<int:pk>/detalle/', PostDetalle.as_view(), name="final_app_detalle"),
    path('final_app/listar', PostList.as_view(), name="final_app_listar"),
    path('final_app/crear', PostCrear.as_view(), name="final_app_crear"),
    path('final_app/<int:pk>/borrar/', PostBorrar.as_view(), name="final_app_borrar"),
    path('final_app/<int:pk>/actualizar/', PostActualizar.as_view(), name="final_app_actualizar"),
    path('final_app/signup/', UserSignUp.as_view(), name ="final_app_signup"),
    path('final_app/login/', UserLogin.as_view(), name="final_app_login"),
    path('final_app/logout/', UserLogout.as_view(), name = "final_app_logout"),
    path('final_app/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="final_app_avatars_actualizar"),
    path('final_app/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="final_app_users_actualizar"), 
    path('final_app/mensajes/crear/', MensajeCrear.as_view(), name="final_app_mensajes_crear"),
    path('final_app/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="final_app_mensajes_borrar"),
    path('final_app/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="final_app_mensajes_detalle"),
    path('final_app/mensajes/listar/', MensajeListar.as_view(), name="final_app_mensajes_listar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
