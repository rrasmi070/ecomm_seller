from django.urls import path
from seller import views
urlpatterns = [
    path('', views.index, name= 'seller'),
    # path('admin_login', views.admin_login, name= 'adlog'),

]
    