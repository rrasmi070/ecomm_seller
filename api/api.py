# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *

# class ProductList(APIView):
#     def get(self,request):
#         model = Product.objects.all()
#         serial = ProductSerializer(model, many=True)
#         return Response(serializer.data)