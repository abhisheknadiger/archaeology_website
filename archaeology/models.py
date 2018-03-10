from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
max1 =  100;
max2 = 500;
# Create your models here.
days = (('1','Sunday'),('2','Monday'),('3','Tuesday'),('4','Wednesday'),('5','Thursday'),('6','Friday'),('7','Saturday'))
#models for Museums
class Museum (models.Model):
    name = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    location = models.CharField(max_length=max1,null=True,blank=True)
    desc = models.CharField(max_length=max2,null=True,blank=True)
    opening_time = models.TimeField(null= True, blank =True)
    closing_time = models.TimeField(null= True, blank =True)
    holiday = models.CharField(max_length=max2,null=True,blank=True,choices=days,default=1)
    photo = models.ImageField(upload_to='museum',null=True,blank=True)
    def __str__(self):
        return self.name

class museum_feedback(models.Model):
    musuem = models.ForeignKey(Museum,on_delete=models.SET_NULL,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.CharField(max_length=max2,blank=True,null=True)

    def __str__(self):
        return self.text

class Museum_ticket(models.Model):
    adult_ticket_rate = models.IntegerField(null=True, blank=True)
    child_ticket_rate = models.IntegerField(null=True, blank=True)
    museum = models.ForeignKey(Museum, null=True, blank=True)

class Buy_museum_ticket(models.Model):
    ticket = models.ForeignKey(Museum_ticket, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    adult_no = models.IntegerField(null=True, blank=True)
    child_no = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def calculate(self):
        self.amount = self.adult_no * self.ticket.adult_ticket_rate + self.child_no * self.ticket.child_ticket_rate


    @classmethod
    def create(cls):
        Tick = cls()
        return Tick


#models for Monument
class Monument(models.Model):
    name =  models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter  name correctly"})
    location = models.CharField(max_length=max1, null=True, blank=True)
    desc = models.CharField(max_length=max2, null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    holiday = models.CharField(max_length=max2, null=True, blank=True,choices=days,default=1)
    photo = models.ImageField(upload_to='museum', null=True, blank=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    adult_ticket_rate = models.IntegerField(null=True, blank=True)
    child_ticket_rate = models.IntegerField(null=True, blank=True)
    monument = models.ForeignKey(Monument, null=True, blank=True)

class Buy_ticket(models.Model):
    ticket = models.ForeignKey(Ticket, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    adult_no = models.IntegerField(null=True, blank=True)
    child_no = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def calculate(self):
        self.amount = self.adult_no * self.ticket.adult_ticket_rate + self.child_no * self.ticket.child_ticket_rate

    @classmethod
    def create(cls):
        Ticket = cls()
        return Ticket

class feedback(models.Model):
    monument = models.ForeignKey(Monument,related_name='monument')
    user = models.ForeignKey(User,related_name='user')
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.CharField(max_length=max2,blank=True,null=True)

    def __str__(self):
        return self.text

#models for Library
class Library(models.Model):
    name = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    location = models.CharField(max_length=max1, null=True, blank=True)
    photo = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    author = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter author name correctly"})
    publisher = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter publisher name correctly"})
    desc = models.CharField(max_length=max1,null=True,blank=True)
    library = models.ForeignKey(Library,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name;

#models for artifacts
class Artifact(models.Model):
    name = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    location = models.CharField(max_length=max1,null=True,blank=True)
    desc = models.CharField(max_length=max2, null=True, blank=True)
    musuem = models.ForeignKey(Museum,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='museum', null=True, blank=True)
    def __str__(self):
        return self.name

class artifact_feedback(models.Model):
    artifact = models.ForeignKey(Artifact,on_delete=models.SET_NULL,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.CharField(max_length=max2,blank=True,null=True)
    def __str__(self):
        return self.text


#models for projects
class Projects (models.Model):
    name = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    desc = models.CharField(max_length=max2,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    working_on = models.CharField(max_length=max1,null=True,blank=True)

#models for excavation
class Excavations(models.Model):
    name =  models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    location = models.CharField(max_length=max1, null=True, blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    desc = models.CharField(max_length=max2, null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    holiday = models.CharField(max_length=max2, null=True, blank=True,choices=days,default=1)
    photo = models.ImageField(upload_to='museum', null=True, blank=True)

    def __str__(self):
        return self.name

class Excavation_ticket(models.Model):
    adult_ticket_rate = models.IntegerField(null=True, blank=True)
    child_ticket_rate = models.IntegerField(null=True, blank=True)
    excavation = models.ForeignKey(Excavations, null=True, blank=True)

class Buy_excavation_ticket(models.Model):
    ticket = models.ForeignKey(Excavation_ticket, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    adult_no = models.IntegerField(null=True, blank=True)
    child_no = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def calculate(self):
        self.amount = self.adult_no * self.ticket.adult_ticket_rate + self.child_no * self.ticket.child_ticket_rate

    @classmethod
    def create(cls):
        Tick = cls()
        return Tick

class User_profile(models.Model):
    name = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter your name"})
    email = models.EmailField(max_length=max1,null=True,blank=True)
    username = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter your name"})
    password = models.CharField(max_length=max1,null=True,blank=True,validators=[RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}')],error_messages={'invalid':"Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character"})
    user_type = models.CharField(max_length=20,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    contact_no = models.IntegerField( null=True,blank=True,validators=[RegexValidator(regex='[0-9]{10}')],error_messages={ 'invalid':"Invalid Number"})
    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def is_premium(self):
        if self.user_type == "archaeologist":
            return True
        else:
            return False

class message(models.Model):
    name = models.CharField(max_length=max1, null=True, blank=True, validators=[RegexValidator(regex='^[a-zA-Z]*$')],error_messages={'invalid': "Please enter name correctly"})
    message = models.TextField(max_length=max2)

    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length=max1, null=True, blank=True,validators=[RegexValidator(regex='^[a-zA-Z_ ]*$')],error_messages={ 'invalid':"Please enter name correctly"})
    user = models.ForeignKey(User,models.CASCADE,null=True)
    date = models.DateTimeField(null=True,blank=True)
    paper = models.FileField(null=True)
    Abstract = models.FileField(null=True)
    desc = models.CharField(null=True,max_length=max2)
    def __str__(self):
        return self.name