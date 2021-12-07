from django.db import models
class Students5(models.Model):
        enroll=models.CharField(max_length=10,primary_key=True)
        name=models.CharField(max_length=50)
        course=models.CharField(max_length=10)
        branch=models.CharField(max_length=10)
        section=models.CharField(max_length=10)
        semester=models.IntegerField(max_length=10)
        toc=models.IntegerField(max_length=10)
        dbms=models.IntegerField(max_length=10)
        departmentalelectives=models.IntegerField(max_length=10)
        openelectives=models.IntegerField(max_length=10)
        totalmarks=models.IntegerField()
        percentage=models.IntegerField()
        
class Meta:
        db_table="StudentResult_student5"