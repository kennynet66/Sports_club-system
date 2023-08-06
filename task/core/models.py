from django.db import models

#This has all the details required for a member to register for the group
class Member_details(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    GUARDIAN = 'guardian'
    MOTHER = 'mother'
    FATHER = 'father'

    KIN_CHOICES = [
        (GUARDIAN, 'Guardian'),
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
    ]
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    name_of_next_of_kin = models.CharField(max_length=200)
    relationship = models.CharField(
        max_length=20,
        choices = KIN_CHOICES,
        default=None,
        )
    school_of_origin = models.CharField(max_length = 200)
    weight = models.FloatField(default=50)
    height = models.FloatField(default=50)
    special_needs = models.BooleanField(default=False, blank=True, null=True)
    specify = models.CharField(max_length=200, blank=True, null=True)
    passport = models.ImageField (upload_to="passports", blank=True, null=True)

    class Meta:
        ordering = ('firstname',) #To arrange the members in alphabetical order
        verbose_name_plural = "Member details" #Avoiding Member detailss in the admin interface

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}" #To write the actual name of the member in the admin interface
    
class Sports_details(models.Model):
    name = models.CharField(max_length=200)
    passport = models.ImageField(upload_to="sporty", blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sports details'

    def __str__(self):
        return self.name
    
class Patron(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    passport = models.ImageField(upload_to="patron_pic", blank=True, null=True)
    about = models.TextField(default="Corrupti a veniam harum unde temporibus quaerat soluta provident, earum impedit voluptates consectetur eveniet voluptatibus vitae hic assumenda delectus, debitis maxime in facere labore beatae quia? Perferendis dolorum impedit eligendi explicabo, commodi qui quia ratione possimus numquam veniam minus maxime dolorum, tempore modi ullam vel, veritatis provident dolores natus aperiam?")
    patron_to = models.ForeignKey(Sports_details, on_delete=models.CASCADE)

    class Meta:
        ordering = ("firstname",)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Store (models.Model):
    item_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="item_photo", blank=True, null=True)
    price = models.FloatField(default=0, null=True, blank=True)
    stock_available = models.IntegerField(default=0)

    class Meta:
        ordering = ("item_name",)
        verbose_name_plural = 'Store'

    def __str__(self):
        return self.item_name