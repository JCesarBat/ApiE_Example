
from django.urls import path
from App_api import views

urlpatterns = [
    path('vistas/',views.Company_View.as_view(),name='vistas'),
    path('vistas/<int:company_id>',views.Company_View.as_view(),name='vistas'),
     path('vista/<int:company_id>',views.one_company,name='vista')
   
]