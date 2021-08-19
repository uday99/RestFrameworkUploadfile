from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class UserFile(models.Model):
    User=get_user_model()

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='docs/photos/')
    resume=models.FileField(upload_to='docs/resumes/')
    idproof=models.FileField(upload_to='docs/proofs/')


class SingleUser(models.Model):
    User=get_user_model()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    docfiles=models.FileField(upload_to='singledocs/multifiles/')


