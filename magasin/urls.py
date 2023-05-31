from django.urls import path
from . import views
from .views import  register
from .views import CategoryAPIView
from .views import ProduitAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('register/',register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),

]