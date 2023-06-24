from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    medicines = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'disease_app'

