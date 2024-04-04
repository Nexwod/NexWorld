from django.db import models

# Create your models here.
class Estate(models.Model):
    title= models.CharField(max_length = 100)
    location= models.CharField(max_length = 400)
    documents = models.CharField(max_length = 400)
    landmarks= models.CharField(max_length = 400)
    features= models.TextField(blank=True)
    price= models.IntegerField()
    size= models.IntegerField(null=True, default="465")
    discounted_price = models.DecimalField(max_digits=100, decimal_places = 0, blank=True, null = True)
    image = models.ImageField(default='\image\pexels-pixabay-280221.jpg', upload_to='image/', blank=True, null=True)
    subscription_form = models.FileField(upload_to='subscription/', blank=True, null=True, default='\image\pexels-pixabay-280221.jpg')
    c_of_o = models.CharField(null=True, max_length=100, blank=True)
    google_map = models.TextField(blank=True)

class Branch(models.Model):
    address = models.CharField(max_length = 400)
    team_lead = models.CharField(max_length = 400)
    contact = models.CharField(max_length = 400)
    google_map = models.TextField()

class Purchase(models.Model):
    name = models.CharField(max_length = 400)
    email = models.CharField(max_length = 400)
    contact = models.CharField(max_length = 400)
    address = models.TextField()
    paid = models.BooleanField(default=False)
    state = models.CharField(max_length = 400)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    estate_name = models.CharField(max_length = 400, null=True)
    


STATES_CHOICE = (
        ('AB', 'Abia'),
        ('AD', 'Adamawa'),
        ('AK', 'Akwa Ibom'),
        ('AN', 'Anambra'),
        ('BA', 'Bauchi'),
        ('BY', 'Bayelsa'),
        ('BE', 'Benue'),
        ('BO', 'Borno'),
        ('CR', 'Cross River'),
        ('DE', 'Delta'),
        ('EB', 'Ebonyi'),
        ('ED', 'Edo'),
        ('EK', 'Ekiti'),
        ('EN', 'Enugu'),
        ('GO', 'Gombe'),
        ('IM', 'Imo'),
        ('JI', 'Jigawa'),
        ('KD', 'Kaduna'),
        ('KN', 'Kano'),
        ('KT', 'Katsina'),
        ('KE', 'Kebbi'),
        ('KO', 'Kogi'),
        ('KW', 'Kwara'),
        ('LA', 'Lagos'),
        ('NA', 'Nasarawa'),
        ('NI', 'Niger'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('OS', 'Osun'),
        ('OY', 'Oyo'),
        ('PL', 'Plateau'),
        ('RI', 'Rivers'),
        ('SO', 'Sokoto'),
        ('TA', 'Taraba'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
        ('FC', 'Federal Capital Territory'),
    )
GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
class Realtor(models.Model):
    name= models.CharField(max_length = 100)
    address= models.CharField(max_length = 400)
    contact= models.CharField(max_length = 100)
    gender = models.CharField(choices=GENDER, max_length=10)
    email= models.EmailField(max_length = 100)
    state= models.CharField(choices = STATES_CHOICE, max_length=100)
    profile_picture= models.ImageField(upload_to='profile_image', default="default.png", blank=True)
    occupation = models.CharField(max_length = 100, blank = True, null=True)
    invite= models.CharField(max_length = 100, blank = True)
    invite_contact= models.CharField(max_length = 100, blank = True, null=True)
    account_number= models.CharField(max_length = 100)
    account_name= models.CharField(max_length = 100)
    bank_name= models.CharField(max_length = 100)
    verified = models.BooleanField(null=True, default=False)
    receipt = models.ImageField(upload_to='receipt', blank=True)

