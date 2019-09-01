from django.db import models


class Equipment(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    status_choice = [('A', 'Available'), ('B', 'Booked'), ('NA', 'Not Available')]
    status = models.CharField(choices=status_choice, max_length=1, default=None)

    def __str__(self):
        return self.item_name




