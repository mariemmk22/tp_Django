from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import FournisseurForm, ProduitForm 
from django.shortcuts import redirect, render 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categorie
from magasin.serializers import *
from rest_framework import viewsets

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
   def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
                queryset = queryset.filter(categorie_id=category_id)
        return queryset

@login_required
def index(request):
    if request.method == "POST" :
          form = ProduitForm(request.POST,request.FILES) 
          if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect('/magasin')
    else : 
            form = ProduitForm()
            list=Produit.objects.all() 
            
    return render(request,'magasin/majProduits.html',{'form':form ,'list':list})

@login_required
def nouveauFournisseur(request):
    if request.method == "POST" :
        forms = FournisseurForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/magasin')
    else :
        forms = FournisseurForm()
    listfr=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'forms':forms , 'listfr':listfr})

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
        return redirect('/login')
    else :
        form = UserCreationForm()
        return render(request,'registration/register.html',{'form' : form})
def login(request):
    if request.method == "POST":
        form = authenticate(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("../mesProduits")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = authenticate()
    return render(request, "login.html", {"login_form": form})


def logout(request):
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")


