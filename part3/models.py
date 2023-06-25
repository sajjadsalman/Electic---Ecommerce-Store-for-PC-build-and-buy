from django.db import models
from django.contrib.auth.models import User

class Component(models.Model):
    CATEGORY_CHOICES = [
        ('HDD', 'HDD'),
        ('RAM', 'RAM'),
        ('OS', 'OS'),
        ('GPU', 'GPU'),
        ('CPU', 'CPU'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image_url = models.URLField(default='https://lh3.googleusercontent.com/RC4BS3P3PWp7cFviCPWButk0UFAxQKu54XayyjgzOSy2PTD0D9Zll1gSLaMzClmPNW8L3lvvg-2TeD857WIcoVSxC4G-Yo2Q7kUf_5TFuT66ZE5RvKWYykoVxDqe69f32vH6rt3m5A=w20')

    def __str__(self):
        return self.name

class Computer(models.Model):
    name = models.CharField(max_length=100)
    components = models.ManyToManyField(Component)
    image_url = models.URLField(default='https://lh3.googleusercontent.com/RC4BS3P3PWp7cFviCPWButk0UFAxQKu54XayyjgzOSy2PTD0D9Zll1gSLaMzClmPNW8L3lvvg-2TeD857WIcoVSxC4G-Yo2Q7kUf_5TFuT66ZE5RvKWYykoVxDqe69f32vH6rt3m5A=w20')

    @property
    def total_price(self):
        return sum(component.price for component in self.components.all()) + 200

    def __str__(self):
        return self.name

class CartItem(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.computer.name}'
    
