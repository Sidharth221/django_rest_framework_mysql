from django.db import models


class GroceryProduct(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=7, decimal_places=4)
    description=models.TextField()
    review_stars = models.IntegerField()
    
    def __str__(self):
        return self.name
