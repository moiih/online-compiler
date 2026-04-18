from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class CodeFileUpload(models.Model):

    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    codefile = models.FileField(upload_to= 'Code_Files')    
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)    

    class Meta:
        db_table = 'code_file_table'