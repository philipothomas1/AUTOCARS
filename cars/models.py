from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator,RegexValidator,MinLengthValidator
from autoslug import AutoSlugField

FEATURES_CHOICES=(

    ('YES','YES'),
    ('NO','NO'),

    # ('D','new'),
    # ('N','new'),

)
SPARE_PARTS_CONDITION_CHOICES=(

    ('NEW','NEW'),
    ('USED','USED'),

    # ('D','new'),
    # ('N','new'),

)

STEERING_CHOICES=(

    ('RIGHT','RIGHT'),
    ('LEFT','LEFT'),

    # ('D','new'),
    # ('N','new'),

)
SPARE_PARTS_CATEGORY_CHOICES=(

    ('BODY PARTS','BODY PARTS'),
    ('ENGINE & COMPONENTS','ENGINE & COMPONENTS'),
    ('CHASIS','CHASIS'),
    ('EXHAUST & COMPONENTS','EXHAUST & COMPONENTS'),
    ('EXTERIOR PARTS','EXTERIOR PARTS'),
    ('INTERIOR PARTS','INTERIOR PARTS'),
    ('LIGHTINGS','LIGHTINGS'),
    ('TIRES AND WHEELS','TIRES AND WHEELS'),
    ('SUSPENSION','SUSPENSION'),
    ('ELECTRONICS','ELECTRONICS'),
    ('BRAKE SYSTEMS','BRAKE SYSTEMS'),
    ('COOLING COMPONENTS','COOLING COMPONENTS'),
    ('DOOR PARTS','DOOR PARTS'),
    ('MIRRORS','MIRRORS'),
    ('OTHER PARTS','OTHER PARTS'),

    # ('D','new'),
    # ('N','new'),

)
# Create your models here.
class Make(models.Model):
	make_name=models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return self.make_name

	class Meta:
		verbose_name_plural="Make"

class Drive(models.Model):
	drivetrain=models.CharField(max_length=20, null=True)
	
	def __str__(self):
	    return self.drivetrain
	class Meta:
		verbose_name_plural='Drive'

class Trannsmission(models.Model):
	transmision=models.CharField(max_length=20, null=True)
	
	def __str__(self):
	    return self.transmision

	class Meta:
		verbose_name_plural='Trannsmission'

class FuelType(models.Model):
	fuel_type=models.CharField(max_length=20, null=True)
	
	def __str__(self):
	    return self.fuel_type

	class Meta:
		verbose_name_plural="FuelType"

class Color(models.Model):
	color_name=models.CharField(max_length=20, null=True)
	
	def __str__(self):
	    return self.color_name

class BodyType(models.Model):
	bodytype=models.CharField(max_length=20, null=True)
	
	def __str__(self):
	    return self.bodytype

	class Meta:
		verbose_name_plural="BodyType"


class Cars(models.Model):
	make=models.ForeignKey(Make, on_delete=models.CASCADE,null=True)
	car_name= models.CharField(max_length=50,help_text="Harrier 240G", null=True)
	price=models.IntegerField(null=True,validators=[MinValueValidator(1000000)])
	mileage=models.IntegerField(null=True,validators=[MinValueValidator(0)])
	drive= models.ForeignKey(Drive, on_delete=models.CASCADE,null=True)
	transmission=models.ForeignKey(Trannsmission, on_delete=models.CASCADE,null=True)
	fueltype=models.ForeignKey(FuelType, on_delete=models.CASCADE,null=True)
	color=models.ForeignKey(Color, on_delete=models.CASCADE,null=True)
	engine=models.IntegerField(help_text="Engine in CC",null=True,validators=[MinValueValidator(1000)])
	body_type=models.ForeignKey(BodyType,on_delete=models.CASCADE,null=True)
	airbag=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	navigation=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	cd=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	leather_seat=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	ac=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	fog_light=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	rear_spoiler=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	back_camera=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	alloy_wheels=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	power_window=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	power_steering=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	keyless_entry=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	spare_tyre=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	sunroof=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	AntilockBrakingSystem=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	radio=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	tv=models.CharField(choices=FEATURES_CHOICES,max_length=20, null=True)
	description= models.TextField(max_length=200, null=True)
	year=models.IntegerField(help_text="Manufactured Year",null=True,validators=[MinValueValidator(1990)])
	steering=models.CharField(choices=STEERING_CHOICES,max_length=5, null=True)
	doors=models.IntegerField(null=True,validators=[MinValueValidator(2)])
	seats=models.IntegerField(null=True,validators=[MinValueValidator(2)])
	added_on = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)
	car_main_image=models.ImageField(upload_to='media/',null=True)
	car_sub_image1=models.ImageField(upload_to='media/',null=True)
	car_sub_image2=models.ImageField(upload_to='media/',null=True)
	car_sub_image3=models.ImageField(upload_to='media/',null=True)
	car_sub_image4=models.ImageField(upload_to='media/',null=True)
	car_sub_image5=models.ImageField(upload_to='media/',null=True)
	car_sub_image6=models.ImageField(upload_to='media/',null=True)
	car_sub_image7=models.ImageField(upload_to='media/',null=True)
	car_sub_image8=models.ImageField(upload_to='media/',null=True)
	car_sub_image9=models.ImageField(upload_to='media/',null=True)
	car_sub_image10=models.ImageField(upload_to='media/',null=True)
	slug=AutoSlugField(populate_from='added_on')




	def __str__(self):
		return self.car_name

	class Meta:
		verbose_name_plural="Cars"



	def get_absolute_url(self):
	#{{ item.get_absolute_url }}
		return reverse("cars:car_detail", kwargs={'slug': self.slug})

	# def __str__(self):
	# 	return self.car_name


class AutoParts(models.Model):
	spare_parts_name= models.CharField(max_length=100,help_text="Rear Bumper", null=True)
	category=models.CharField(choices=SPARE_PARTS_CATEGORY_CHOICES,max_length=20, null=True)
	make=models.ForeignKey(Make, on_delete=models.CASCADE)
	auto_part_image=models.ImageField(upload_to='media/',null=True)
	price=models.IntegerField(null=True,validators=[MinValueValidator(1)])
	description= models.TextField(max_length=200, null=True)
	condition= models.CharField(choices=SPARE_PARTS_CONDITION_CHOICES,max_length=20, null=True)
	added_on = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)
	slug=AutoSlugField(populate_from='added_on')

	def get_absolute_url(self):
		return reverse("cars:spare_detail", kwargs={'slug': self.slug})


	def __str__(self):
		return self.spare_parts_name

	class Meta:
		verbose_name_plural="AutoParts"


my_validator = RegexValidator(r'^[-0-9]', "Your string should be ten digits.")
name_validator = RegexValidator(r'^[-a-zA-Z]', "Username should contain letters only.")
class ContactInfomation(models.Model):
	phone_number1= models.CharField(max_length=10,help_text="Phone Number", unique=True,null=True,validators=[MinLengthValidator(10),my_validator])
	phone_number2= models.CharField(max_length=10,help_text="Phone Number",null=True,validators=[MinLengthValidator(10),my_validator])
	location= models.CharField(max_length=15,help_text="City name", null=True,validators=[RegexValidator(r'^[-a-zA-Z]', "Contain letters only")])
	email= models.EmailField(max_length=30, null=True)
	street=models.CharField(max_length=30, null=True)
	bank_account_number=models.CharField(max_length=30, null=True)
	bank_account_name= models.CharField(max_length=15,help_text="Account name", null=True,validators=[RegexValidator(r'^[-a-zA-Z]', "Contain letters only")])

	
	





	def __str__(self):
		return self.location

	class Meta:
		verbose_name_plural="ContactInfomation"





class HomeBanner1(models.Model):
	first_line_words= models.CharField(max_length=15, null=True)
	second_line_words= models.CharField(max_length=14, null=True)
	third_line_words= models.CharField(max_length=10, null=True)
	fourth_line_words= models.CharField(max_length=25, null=True)
	banner_image1=models.ImageField(upload_to='media/',null=True,help_text="1920 x 772")



	def __str__(self):
		return self.first_line_words

	class Meta:
		verbose_name_plural="HomeBanner1"


class HomeBanner2(models.Model):
	first_line_words= models.CharField(max_length=15, null=True)
	second_line_words= models.CharField(max_length=14, null=True)
	third_line_words= models.CharField(max_length=10, null=True)
	fourth_line_words= models.CharField(max_length=25, null=True)
	banner_image2=models.ImageField(upload_to='media/',null=True,help_text="1920 x 772")



	def __str__(self):
		return self.first_line_words

	class Meta:
		verbose_name_plural="HomeBanner2"


class SideBanner1(models.Model):
	first_line_words= models.CharField(max_length=25, null=True)
	second_line_words= models.CharField(max_length=50, null=True)
	side_banner_image1=models.ImageField(upload_to='media/',null=True,help_text="315 x 375")



	def __str__(self):
		return self.first_line_words

	class Meta:
		verbose_name_plural="SideBanner1"


class SideBanner2(models.Model):
	first_line_words= models.CharField(max_length=25, null=True)
	second_line_words= models.CharField(max_length=50, null=True)
	side_banner_image2=models.ImageField(upload_to='media/',null=True,help_text="315 x 375")



	def __str__(self):
		return self.first_line_words

	class Meta:
		verbose_name_plural="SideBanner2"

class SideBanner3(models.Model):
	first_line_words= models.CharField(max_length=25, null=True)
	second_line_words= models.CharField(max_length=50, null=True)
	side_banner_image3=models.ImageField(upload_to='media/',null=True,help_text="315 x 375")



	def __str__(self):
		return self.first_line_words

	class Meta:
		verbose_name_plural="SideBanner3"









