from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    date_of_creation=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(null=True,blank=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title