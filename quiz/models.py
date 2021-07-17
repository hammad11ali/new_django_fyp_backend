from django.db import models

# Create your models here.


class LearningObjective(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    concept_name = models.CharField(max_length=100)
    action_verb = models.CharField(max_length=100)
    qgenerator = models.FileField(upload_to='Qgenerators/', null=True)
    txtfile=models.FileField(upload_to='Qgenerators/', null=True)
    def __str__(self):
        """String"""
        return self.name
