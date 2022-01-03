from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=40)
    courseNumber = models.IntegerField(null=False)
    instructorName = models.CharField(max_length=40)
    duration = models.DecimalField(default=0.00, max_digits=10000)

    objects = models.Manager()

    def __str__(self):
        return self.title


