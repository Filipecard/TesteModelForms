
from django.contrib import admin
from django.urls import path
from meuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('list_pintores/',views.list_pintores,name='list_pintores'),
    path('list_quadros/',views.list_quadros,name='list_quadros'),
    path('add_pintor/',views.add_pintor,name='add_pintor'),
    path('add_quadro/',views.add_quadro,name='add_quadro'),
    path('list_pessoas/',views.list_pessoas,name='list_pessoas'),
    path('list_comidas/',views.list_comidas,name='list_comidas'),
    path('add_pessoa/',views.add_pessoa,name='add_pessoa'),
    path('add_comida/',views.add_comida,name='add_comida'),
]
