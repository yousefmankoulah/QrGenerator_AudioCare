from django.urls import path
from . import views


urlpatterns = [
    path('', views.signInView, name='login'),
    path('homeAcessForDashboard/', views.dashboard, name='home'),
    path('logout/', views.signoutView, name='logout'),
    path('qrcodeGenerator/', views.qr_gen, name='qr'),
    path('siteDetail/<id>/', views.siteDetail, name='detail'),
    path('search/', views.searchResult, name='search'),
    
]
