from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default='')
    sub_category=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=300)
    pub_date = models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="helloapp/images",default='')
    


    def __str__(self):
        return self.product_name

class Orders(models.Model):
    
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    amount=models.IntegerField(default=0)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111,default='')
    def __str__(self):
        return self.name

class updateOrder(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000) 
    timestap=models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.update_desc    
    


