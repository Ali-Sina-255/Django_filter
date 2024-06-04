from django.db import models

# Create your models here.
class Employee(models.Model):
    class EDUCATION_STATUS(models.TextChoices):
        BACHELOR = 'B'
        MASTER = 'M'
        PHD = 'PH'
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    education = models.CharField(choices=EDUCATION_STATUS.choices, max_length=10)

    def __str__(self) -> str:
        return self.id + self.name + self.last_name