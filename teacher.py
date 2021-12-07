from django.db import models
class Teachers6(models.Model):
       
        username=models.CharField(max_length=50)
        fullname=models.CharField(max_length=50)
        psw=models.CharField(max_length=10)
        oldpsw=models.CharField(max_length=10)
        newpsw=models.CharField(max_length=10)
        pswrepeat=models.CharField(max_length=10)
        designation=models.CharField(max_length=50)
        gender=models.CharField(max_length=50)
        phone=models.IntegerField(max_length=10)
        address=models.CharField(max_length=50)
        email=models.CharField(max_length=50)
        question=models.CharField(max_length=100)
        answer=models.CharField(max_length=100)
        
        
class Meta:
        db_table="StudentResult_teacher6"