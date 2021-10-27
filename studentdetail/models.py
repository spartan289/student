from django.db import models

# Create your models here.
class tbl_student1(models.Model):

    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_college = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    degree_name = models.CharField(max_length=100)
    internship_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    student_phone = models.CharField(max_length=100)
    student_address = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=10)
    notes = models.TextField()
    username = models.CharField(max_length=100,default='ele30')