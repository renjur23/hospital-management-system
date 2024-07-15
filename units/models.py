from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    department_description = models.TextField()
    
    def __str__(self):
        return self.department_name
class Doctors(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_spec=models.TextField()
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors',default='default_image.jpg')

    def __str__(self):
        return 'Dr'+' '+ self.doc_name
class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name
    


class Contact(models.Model):
    name=models.CharField(max_length=200)
    mail_id=models.EmailField()
    msg=models.TextField()
  
    def __str__(self):
        return self.name
    
class Login(models.Model):
    mail=models.EmailField()
    pswd=models.CharField(max_length=128)
  
    def __str__(self):
        return self.mail
    
class Pharmacy(models.Model):
    med_name=models.CharField(max_length=200)
    med_image=models.ImageField(upload_to='medicine',default='default_image.jpg')
    med_amount = models.IntegerField()

    def __str__(self):
        return  self.med_name

