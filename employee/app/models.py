from django.db import models

# Create your models here.
class department(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50,default = '')
    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"

    def __str__(self):
        return self.name

    

class employee(models.Model):
    id = models.IntegerField(primary_key = True)
    name= models.CharField(verbose_name = 'Employee_Name', max_length=50)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    salary = models.IntegerField()
    date = models.DateField( auto_now=False)
    
    
    def __str__(self):
        return self.name
    