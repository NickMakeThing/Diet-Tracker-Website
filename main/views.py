from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, WeightChange
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import hashlib

class Index(TemplateView):
    template_name='index.html'
    #needs to render stuff from the database


#api that receives weight info from raspberry pi
#update_or_create method
class ReceiveProductInformation(CreateAPIView):
    http_method_names = ['post']
    #serialize?
    #request: {time/date, weight, energy, protein, fats, carbs, sugars}
    #https://github.com/NickMakeThing/rock-paper-scissors/blob/master/backend/rockpaperscissors/views.py
    def create(self, request, *args, **kwargs):
        data = request.data
        product_code = hash_product(data)
        product = Product.objects.filter(code=product_code) #returns as a queryset. [0] gets the actual object
        if product.exists(): #count() if exists doesnt work
            if data['weight'] >= product[0].current_weight + 40:
                product.update(current_weight=data['weight'])
            elif data['weight'] <= product[0].current_weight - 40:
                weight_change = product[0].current_weight - data['weight']
                product.update(current_weight=data['weight'])
                WeightChange.objects.create(
                    product = product[0],
                    date_time = data['date'],
                    weight_change = weight_change
                )
        else:
            Product.objects.create(
                code = product_code,
                current_weight = data['weight'],
                energy = data['energy'],
                protein = data['protein'],
                fat = data['fat'],
                carb = data['carb'],
                sugars = data['sugars'],
                date_time = data['date']
            )
        return Response('hey')
        

def hash_product(data):
    data = data['energy'] + data['protein'] + data['fat'] + data['carb']
    byte_dict = bytes(str(data),'utf-8')
    return hashlib.md5(byte_dict).hexdigest()

"""
byte_dict = bytes(str(data,'utf-8'))
hashlib.md5(byte_dict).hexdigest()


var xhr = new XMLHttpRequest();  
xhr.open("POST", "/api");
xhr.setRequestHeader("Content-Type", "application/json;");
xhr.send(JSON.stringify({ 
    "weight": 100,
    "energy":500,
    "protein":5,
    "fat":2,
    "carb":3,
    "sugars":1
}));
"""