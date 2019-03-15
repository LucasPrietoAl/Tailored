from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    #website = models.URLField(blank = True)
    picture = models.ImageField(upload_to = "profile_images", blank = True)

    def __str__(self):
        return self.user.username

class Section(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    section = models.ForeignKey(Section)
    title = models.CharField(max_length = 128)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.title

class Item(models.Model):
    category = models.ForeignKey(Category)
    itemName = models.CharField(max_length = 128)
    price = models.IntegerField(default = 0)
 
    def __str__(self):
        return self.itemName
