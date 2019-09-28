from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AllDocuments(models.Model):

    docname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.docname

class Requests(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    document = models.ForeignKey(AllDocuments, on_delete = models.CASCADE)
    Additionalinfo = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username