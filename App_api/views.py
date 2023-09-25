from typing import Any
from django import http
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json



def one_company(request,company_id):

    company =  Company.objects.filter(id=company_id).values()

    if len(company) >=1 :
        lista_C=list(company)
    
        data= {'company':lista_C}

        return JsonResponse(data)
    
    else:
         data   = {'message':'company do not exist....'}
         return JsonResponse(data)




class Company_View(View) :
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        companies=Company.objects.values()
        lista=[]
        for company in companies :

            lista.append(company)


        if len(lista) > 0:
            data = {'message':'sucess','companies':lista}
        
        else :
            data   = {'message':'companies not faund....'}

        return JsonResponse(data)
    
    def post(self,request):
        
        datos=json.loads(request.body)
        
        company=Company()
        company.name=datos.get('name')
        company.direccion=datos.get('direccion')
        company.fundation=datos.get('fundation')
        company.save()
        data = {'message':'sucess'}

        return JsonResponse(data)
    
    def delete(self,request,company_id):
        data = {'message':'sucess'}

        company = Company.objects.filter(id=company_id)

        if len(company) == 1 :

            company.delete()

            data = {'message':'the company was deleted suscesfull'}
            return JsonResponse(data)

        else  :
            data= {'message':'the company dont exist'}
            return  JsonResponse(data)



# Create your views here.
