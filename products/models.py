from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length = 100)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return f'{self.city}'


class Brand(models.Model):
    title = models.CharField(max_length = 70)
    image = models.ImageField(blank= True, upload_to='brand-img')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
    
class Category(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'
    
class Product(models.Model):
    title = models.CharField(max_length = 70)
    description = models.TextField(blank = True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(blank = True, upload_to='product-img')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank = True)
    is_bestseller = models.BooleanField(default=False)
    suggestions = models.ManyToManyField('self')

    def __str__(self) -> str:
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)


