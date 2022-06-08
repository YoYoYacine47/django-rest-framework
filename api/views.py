from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.


'''
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

    return JsonResponse(data)
'''
# using modle_to_dict
'''
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])

    return JsonResponse(data)
'''
# using django rest framework
'''
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])

    return Response(data)
'''
# using serializer
'''
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().first()
    data = {}
    serialize = ProductSerializer(instance)
    if serialize.is_valid:
        data = serialize.data

    return Response(data)
'''
# POST ---> valid the post requst and save it


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    data = request.data
    print(data)
    serialize = ProductSerializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
        instance = serialize.save()
        data = serialize.data
        print(data)
        print(instance)
        return Response(data)
