from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Bill(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, editable=False)

    def calculate_total_cost(self):
        # Calculate total cost
        total = self.items.aggregate(total=models.Sum('price'))['total'] or 0
        print("Total cost before:", total)  # Debug print
        self.total_cost = total
        print("Total cost after:", self.total_cost)  # Debug print
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill {self.id} - Total: ${self.total_cost}"
