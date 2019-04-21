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
    return "TenktoTwentyk/{new_filename}/{final_filename}".format(new_filename=filename, final_filename=final_filename)

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

class TenktoTwentyk_Mobile(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    Charging = models.TextField(default="good speakers")
    Torch = models.TextField(default="Yes")
    Games = models.TextField(default="built-in + downloadable")
    Messaging = models.TextField(default=", SMS (threaded view), MMS, Email, Push Email")
    Browser = models.TextField(default="HTML5")
    Audio = models.TextField(default="3.5mm audio jack, MP4/WMV/H.264 player")
    Data = models.TextField(default="GPRS, Edge, 3G (HSPA 42.2/5.76 Mbps), 4G (LTE-A (2CA) Cat6 300/50 Mbps")
    NFC = models.TextField(default="Yes")
    USB = models.TextField(default="microUSB 2.0")
    GPS = models.TextField(default="Yes + A-GPS support & Glonass, BDS, GALILEO")
    Bluetooth = models.TextField(default="None")
    Wifi = models.TextField(default="Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot")
    Front = models.TextField(default="13 MP, f/1.9, LED flash")
    Main = models.TextField(default="8MP")
    card = models.TextField(default="Yes")
    BuiltIn = models.TextField(default="16GB Built-in")
    Features = models.TextField(default="None")
    Protection = models.TextField(default="Yes")
    Resolution = models.TextField(default="720 x 1280 Pixels (~282 PPI) ")
    Size = models.TextField(default="5.5 inches")
    Technology = models.TextField(default="None")
    GPU = models.TextField(default="Mali-T830MP2 ")
    Chipset = models.TextField(default="None")
    CPU = models.TextField(default="None")
    FourGBand = models.TextField(default="LTE")
    ThreeGBand = models.TextField(default="HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100 ")
    TwoGBand = models.TextField(default="SIM1: GSM 850 / 900 / 1800 / 1900 SIM2: GSM 850 / 900 / 1800 / 1900  ")
    Color = models.TextField(default="Silver, Space Gray, Gold")
    SIM = models.TextField(default="Single SIM (Nano-SIM)  ")
    Weight = models.TextField(default="148g")
    Dimension = models.TextField(default="146.2 x 71.3 x 8 mm")
    UIBuild = models.TextField(default="TouchWiz UI")
    OperatingSystem = models.TextField(default="Android v7.1 Nougat")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image1 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    Review_count = models.TextField(default="90")
    Average_Rating = models.TextField(default=" 4")
    Reviews = models.TextField(default="None")
    Ram = models.TextField(default="2GB")




    # description = models.TextField()
    # featured = models.BooleanField(default=False)
    # active = models.BooleanField(default=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}".format(slug=self.slug)
        return  reverse("TenktoTwentyk:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance , *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=TenktoTwentyk_Mobile)