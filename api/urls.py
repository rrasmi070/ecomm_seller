from django.urls import path
from api import views
from api import api
urlpatterns = [
    path('', views.index, name= 'index'),
    path('web_api/', views.product_api, name= 'product_api'),
    # path('admin_login/', api.ProductList, name= 'adlog'),

]
    