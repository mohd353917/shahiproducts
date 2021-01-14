from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    arrived_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.product.stock += self.quantity
            self.product.save()
        super().save(*args, **kwargs)


class Product(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    stock_price = models.FloatField()
    retail_price = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Shop(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    shopkeeper_name = models.CharField(max_length=50)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return f"{self.shop} - {self.product} - {self.quantity}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.product.stock -= self.quantity
            self.product.save()
        super().save(*args, **kwargs)
