from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

choices = Category.objects.all().values_list('category_name', 'category_name')
choice_list = []
for cho in choices:
    # print(cho)
    choice_list.append(cho)
# print(choice_list)


class Product(models.Model):
    Product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50, choices=choice_list)
    Price = models.FloatField()
    brand = models.CharField(max_length=30)
    Description = models.TextField()
    image = models.FileField(upload_to="product/", max_length=None)

    def __str__(self):
        return self.Product_name 