from django.urls import path,include
from . import views

app_name='aluno'

urlpatterns=[
    path('', views.home, name='home'),
    path('signup/', views.signup, name ='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name = 'secret'),
    ]
