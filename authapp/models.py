from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return self.email

class Enrollment(models.Model):
    CHOICE_FIELD = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    )
    FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=1,choices=CHOICE_FIELD)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.DateField(max_length=8)
    SelectMembershipplan = models.ForeignKey("MembershipPlan", on_delete=models.CASCADE)
    SelectTrainer = models.ForeignKey("Trainer",on_delete=models.CASCADE)
    Address = models.TextField()
    PaymentStatus = models.CharField(max_length=55,null=True,blank=True)
    Price = models.IntegerField(max_length=55, null=True,blank=True)
    DueDate = models.DateField(null=True,blank=True)
    TimeStamp = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.FullName
    

class Trainer(models.Model):
    CHOICE_FIELD = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    )
    Name = models.CharField(max_length=55)
    Gender = models.CharField(max_length=1,choices=CHOICE_FIELD)
    PhoneNumber = models.CharField(max_length=12)
    #Salary = models.IntegerField(max_length=25)

    def __str__(self):
        return self.Name
    
    
class MembershipPlan(models.Model):
    Plan = models.CharField(max_length=185)
    Price = models.IntegerField(max_length=55)

    def __str__(self):
        return "%s Rs.%s"%(self.Plan,self.Price)
    
class Gallery(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media/gallery')
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    