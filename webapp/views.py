from django.shortcuts import render
from django.views import View
from webapp.models import  Product, Orders, Discount, About, Client
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.db.transaction import atomic
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm

import json
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer, OrdersSerializer, DiscountSerializer, AboutSerializer, ClientSerializer

class UsersLoginView(View):
    def get(self, request):
        return render(request, 'main/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username,
                'password': password
                }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'main/404.html')


class UsersLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing')





class UserRegisterView(View):
    def get(self, request):
        return render(request, 'main/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return redirect('register')
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')





class LandingPageView(View):
    def get(self, request):
        search = request.GET.get('search')
        products = Product.objects.all()
        clients = Client.objects.all()
        orders = Orders.objects.all()
        abouts = About.objects.all()
        context = {
            "products": products,
            "orders": orders,
            "clients": clients,
            "abouts": abouts

        }
        return render(request, "main/index.html", context)



class OrdersView(View):
    def get(self, request):
        orders = Orders.objects.all()
        context = {
            "orders": orders
        }
        return render(request, "main/services.html", context)



class RegisterApiView(APIView):
    def get(self, request):
        return render(request, "main/register.html")






class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
        if not search:
            products = Product.objects.all()
            discounts = Discount.objects.all()
            featured_products = Product.objects.all()
            context = {'products': products,
                       "discounts": discounts,
                       "featured_products": featured_products,
                       }
            return render(request, 'main/shop.html', context)
        else:
            products = Product.objects.filter(title__icontains=search)
            featured_products = Product.objects.all()
            discounts = Discount.objects.all()
            context = {'products': products,
                       "discounts": discounts,
                       "featured_products": featured_products,
                       }
            return render(request, 'main/shop.html', context)


class DiscountsView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            discounts = Discount.objects.all()
            context = {
                "discounts": discounts
            }
            return render(request, "main/blog.html", context)
        else:
            discounts = Discount.objects.filter(name__icontains=search)
            if discounts:
                context = {
                    "discounts": discounts
                }

                return render(request, 'main/blog.html', context)
            else:
                context = {
                    "discounts": discounts
                }
                return render(request, 'main/blog.html', context)



class AboutView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            about = About.objects.all()
            context = {
                "about": about
            }
            return render(request, "main/about.html", context)
        else:
            about = About.objects.filter(name__icontains=search)
            if about:
                context = {
                    "about": about
                }

                return render(request, 'main/about.html', context)
            else:
                context = {
                    "about": about
                }
                return render(request, 'main/about.html', context)



class ClientView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            client = Client.objects.all()
            context = {
                "client": client
            }
            return render(request, "main/contact.html", context)
        else:
            client = Client.objects.filter(name__icontains=search)
            if client:
                context = {
                    "client": client
                }

                return render(request, 'main/contact.html', context)
            else:
                context = {
                    "client": client
                }
                return render(request, 'main/contact.html', context)

