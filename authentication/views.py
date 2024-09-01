# from django.shortcuts import render
# from .models import User
# from rest_framework import response
# from django.http import HttpRequest


# def products_view(req: HttpRequest):
#     if req.method == 'GET':
#         products = Product.objects.all()
#         if len(products) == 0:
#             return JsonResponse({"message": "no products found"})
#         return JsonResponse(products, safe=False)

#     elif req.method == 'POST':
#         name = req.data.get('name')
#         price = req.data.get('price')
#         description = req.data.get('description')
        
#         product = Product(name=name, price=price, description=description)
#         product.save()
#         return JsonResponse(product)

# def AddUser(r: HttpRequest):
#     if r.method == 'POST':
#         # Username = 
#         pass
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class AddUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Allows unauthenticated users to access this view
