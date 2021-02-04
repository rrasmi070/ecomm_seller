from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# web: gunicorn ecomm_seller.wsgi --log-file -
# from seller.views import Register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('seller.urls')),
    path('product/', include('api.urls')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
