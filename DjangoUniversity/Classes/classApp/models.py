from django.db import models

class djangoClasses(models.Model): #defining a class
    title = models.CharField(max_length=40, default="", blank=True, null=False) #creating attributes and their requirements
    course_number = models.IntegerField(default="", blank=True, null=False) #integer attribute
    instructor_name = models.CharField(max_length=40, default="", blank=True) #character field attribute
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2) #decimal field attribute

    objects = models.Manager()

    def __str__(self): #This is how we display an easier to understand label in the admin page
        return self.title

#creating object and assigning attribute values
Science = djangoClasses(title="Biology", course_number=100, instructor_name="Adam Sandler", duration=1.50)
Science.save()

#creating object and assigning attribute values
Math = djangoClasses(title="Calculus", course_number=200, instructor_name="Bryan Dilbert", duration=1.25)
Math.save()

#creating object and assigning attribute values
History = djangoClasses(title="The Great Depression", course_number=300, instructor_name="Athena Wilson", duration=1.50)
History.save()