from django.db import models

# Create your models here.


class Property(models.Model):

    place=models.CharField(max_length=100)

    price=models.PositiveIntegerField()

    CATEGORY_CHOICES=(
        ("House","House"),
        ("Villa","Villa"),
        ("Flat","Flat"),
    )

    category=models.CharField(choices=CATEGORY_CHOICES,max_length=20,default="House")

    bedroom_count=models.PositiveIntegerField()

    squarefootage=models.CharField(max_length=100)


    def __str__(self):

        return self.place