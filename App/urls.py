from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('crops/<int:pk>', views.details, name='details'),
    path('s', views.search, name='search'),
    path('info', views.district, name='district'),
    path('rates', views.rates, name='rates'),
    path('products', views.products, name='products'),
]
