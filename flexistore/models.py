from django.db import models


class Uom(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.id} {self.name}'


class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    uom_id = models.ForeignKey(Uom, on_delete=models.DO_NOTHING)
    price_per_unit = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.id} {self.name} {self.uom_id} {self.price_per_unit}'


class Order(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    customer_name = models.CharField(max_length=100, null=False)
    total = models.IntegerField(null=False)
    date = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.id} {self.customer_name} {self.total}'


class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(null=False, decimal_places=2, max_digits=5)
    total = models.DecimalField(null=False, decimal_places=2, max_digits=5)

    def __str__(self):
        return f'{self.id} {self.order_id} {self.product_id} {self.quantity} {self.total}'
