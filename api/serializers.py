from rest_framework import serializers
from api.models import Product





class ProductSerializer(serializers.ModelSerializer):

    # Product_name = serializers.CharField(max_length=20)
    # category = serializers.CharField(max_length=30)
    # Price = serializers.FloatField()
    # brand = serializers.CharField(max_length=30)
    # Description = serializers.TextField()
    # image = serializers.FileField(upload_to="product/", max_length=None)
    class Meta:
        model = Product
        # fields = "__all__"
                # OR
        fields = ('id', 'Product_name','category','Price','brand','Description','image')