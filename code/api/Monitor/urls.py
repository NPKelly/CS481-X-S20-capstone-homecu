from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
	path('creditunions/',views.creditunions,name='creditunions'),
	path('newUser/', views.newUser,name='newUser'),
        path('loanMaintenance/', views.loanMaintenance,name='loanMaintenance'),
        path('loanAppEditor/', views.loanAppEditor,name='loanAppEditor'),
        ]
