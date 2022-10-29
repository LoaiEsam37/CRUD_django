from django.db import models

class USERS(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def __len__(self):
        return len(self.firstname) + len(self.lastname)
