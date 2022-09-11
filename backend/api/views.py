
# from turtle import title
from django.http import JsonResponse
import json

from products.models import Products
# Create your views here.


# def api_home(request, *args,**kwargs):
#     body=request.body #byte string of JSON data 
#     print(body)
#     data = {}
#     try:
#         data=json.loads(body) # string of JSON data -> Python Dict
#     except:
#         pass
#     # print(data.keys()) # list of kyes
#     print(data)
#     print(request.POST)
#     #add to the JSON response data
#     # print(request.GET)
#     data['params']=dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type']= request.content_type
    
#     return JsonResponse(data)


def api_home(request, *args,**kwargs):
    model_data=Products.objects.all().order_by("?").first()
    data={}
    if model_data:
        data['id']=model_data.id
        data['title']=model_data.title
        data['content']=model_data.content

    for product in Products.objects.all():
        if product.id==1:
            print('found one')
            ProdInstance=Products.objects.all().filter(id=1)[0]
            ProdInstance.title='found him'
            ProdInstance.save()

    
    
    return JsonResponse(data)