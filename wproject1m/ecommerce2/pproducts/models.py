import random
import os
from django.db import models
from django.urls import reverse

# Create your models here.
from django.db.models.signals import pre_save, post_save
from ecommerce.utils import unique_slug_generator

def get_filename_ext(filename):
    base_name=os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename=random.randint(1,39321457854)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "pproducts/{new_filename}/{final_filename}".format(new_filename=filename, final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter()
    def featured(self):
        return self.filter()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # def all(self):
    #     return self.get_queryset().active()
    #
    # def featured(self):
    #     return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

class P_Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    Charging = models.TextField(default="good speakers")
    Torch = models.TextField(default="2GB")
    Games = models.TextField(default="8MP")
    Messaging = models.TextField(default="None")
    Browser = models.TextField(default="None")
    Audio = models.TextField(default="None")
    Data = models.TextField(default="None")
    NFC = models.TextField(default="None")
    USB = models.TextField(default="None")
    GPS = models.TextField(default="None")
    Bluetooth = models.TextField(default="None")
    Wifi = models.TextField(default="None")
    Front = models.TextField(default="None")
    Main = models.TextField(default="None")
    card = models.TextField(default="None")
    BuiltIn = models.TextField(default="None")
    Features = models.TextField(default="None")
    Protection = models.TextField(default="None")
    Resolution = models.TextField(default="None")
    Size = models.TextField(default="None")
    Technology = models.TextField(default="None")
    GPU = models.TextField(default="None")
    Chipset = models.TextField(default="None")
    CPU = models.TextField(default="None")
    FourGBand = models.TextField(default="None")
    ThreeGBand = models.TextField(default="None")
    TwoGBand = models.TextField(default="None")
    Color = models.TextField(default="None")
    SIM = models.TextField(default="None")
    Weight = models.TextField(default="None")
    Dimension = models.TextField(default="None")
    UIBuild = models.TextField(default="None")
    OperatingSystem = models.TextField(default="None")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image1 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    Review_count = models.TextField(default="None")
    Average_Rating = models.TextField(default="None")
    Reviews = models.TextField(default="None")
    Ram = models.TextField(default="None")

    # description = models.TextField()
    # featured = models.BooleanField(default=False)
    # active = models.BooleanField(default=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}".format(slug=self.slug)
        return  reverse("pproducts:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance , *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=P_Product )