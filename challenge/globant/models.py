from django.db import models

class hired_employees(models.Model):
   #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    datetime = models.DateTimeField()
    department_id = models.IntegerField()
    job_id = models.IntegerField()

class departments(models.Model):
   # id = models.OneToOneField(hired_employees, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=255)

class jobs(models.Model):
   # id = models.OneToOneField(hired_employees, on_delete=models.CASCADE, primary_key=True)
    job= models.CharField(max_length=255)