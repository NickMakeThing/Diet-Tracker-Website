from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, WeightChange
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import hashlib
import json

class Index(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        stats={}
        weight_changes = WeightChange.objects.all().prefetch_related('product').order_by('product__code','date_time')
        product = None
        for i in weight_changes:
            if i.product.code not in stats:
                stats[i.product.code] = {
                    'name':i.product.name, 
                    'energy':i.product.energy,
                    'protein':i.product.protein,
                    'fat':i.product.fat,
                    'carbs':i.product.carbs,
                    'events':[[i.date_time, i.weight_change]] 
                    }
            else:
                stats[i.product.code]['events'].append([i.date_time, i.weight_change])
        context = super().get_context_data()
        context['stats'] = json.dumps(stats)
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

class ReceiveProductInformation(CreateAPIView):
    #lacks validation 
    #need control to only accept only from rpi. maybe use password from env variable.
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        data = request.data
        product_code = hash_product(data)
        product = Product.objects.filter(code=product_code) #returns as a queryset. [0] gets the actual object
        if product.exists(): #count() if exists doesnt work
            if data['weight'] >= product[0].current_weight + 10:#need to do something here to compensate for the possibility of current_weight going into negatives
                product.update(current_weight=data['weight'])
            elif data['weight'] <= product[0].current_weight - 10:
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
                carbs = data['carbs'],
                sugars = data['sugars'],
            )
        return Response('hey')
        

def hash_product(data):
    data = str(data['energy']) + str(data['protein']) + str(data['fat']) + str(data['carbs'])
    byte_dict = bytes(str(data),'utf-8')
    return hashlib.md5(byte_dict).hexdigest()

"""
var xhr = new XMLHttpRequest();  
xhr.open("POST", "/api/");
xhr.setRequestHeader("Content-Type", "application/json;");
xhr.send(JSON.stringify({ 
    "weight": 100,
    "energy":500,
    "protein":5,
    "fat":2,
    "carbs":3,
    "sugars":1
}));
"""
