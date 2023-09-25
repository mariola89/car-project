from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car_manufacturer'


class Car(models.Model):
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    mileage = models.IntegerField
    color = models.CharField(max_length=250)
    condition = models.TextField()
    vin_num = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()

    def __str__(self):
        return f"Order #{self.pk}"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()















