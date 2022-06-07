from django.urls import path
from .views import *


urlpatterns = [
    # path('allmenu',AllMenu.as_view()),
    # path('all',AllMahsulot.as_view()),
    path('mahsulot',MahsulotModel.as_view()),
    path('mahsulot/<int:pk>',MahsulotModel.as_view()),
    path('menu',MenuModel.as_view()),
    path('menu/<int:pk>',MenuModel.as_view()),
    
]
