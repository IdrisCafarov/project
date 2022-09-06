from django.db import models
from product.helper import seo
from django.urls import reverse

# Create your models here.
class AdsSettings(models.Model):
    ad1_image=models.ImageField(verbose_name="Ad1 Image",upload_to="ads",null=True)
    link1 = models.CharField(verbose_name="Link 1",max_length=1500,null=True)
    ad2_image=models.ImageField(verbose_name="Ad2 Image",upload_to="ads",null=True)
    link2 = models.CharField(verbose_name="Link 2",max_length=1500,null=True)
    ad3_image=models.ImageField(verbose_name="Ad3 Image",upload_to="ads",null=True)
    link3 = models.CharField(verbose_name="Link 3",max_length=1500,null=True)
    ad4_image=models.ImageField(verbose_name="Ad4 Image",upload_to="ads",null=True)
    link4 = models.CharField(verbose_name="Link 4",max_length=1500,null=True)

    
    
    


    def __str__(self):
        return "AdsSettings"
    



class MainCategory(models.Model):
    name = models.CharField(verbose_name="Category Name",max_length=50)
    slug = models.SlugField(verbose_name="Slug",editable=False,unique=True)
    image = models.ImageField(verbose_name="Image",null =True,upload_to="category_img")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Category"
        verbose_name_plural ="Categories"

    def save(self, *args, **kwargs):
        super(MainCategory, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(MainCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category_detail', kwargs={'slug': self.slug})


    
class SubCategory(models.Model):
    name = models.CharField(verbose_name="Sub Category Name", max_length=50)
    slug = models.SlugField(verbose_name="Slug",editable=False,unique=True)
    category = models.ForeignKey(MainCategory,verbose_name="Choose Category",on_delete=models.CASCADE,related_name="category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Sub Category"
        verbose_name_plural ="Sub Categories"

    def save(self, *args, **kwargs):
        super(SubCategory, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category_detail', kwargs={'slug': self.slug})

    




class Product(models.Model):
    name = models.CharField(verbose_name="Product Name",max_length=50)
    description = models.TextField(verbose_name="About Product")
    price = models.FloatField(verbose_name="Price")
    category = models.ForeignKey(SubCategory,null=True,verbose_name="Sub Category",on_delete=models.CASCADE,related_name="sub_category")
    slug = models.SlugField(editable=False, verbose_name="Slug",unique=True)
    image = models.ImageField(upload_to="products_img",verbose_name="Image")
    draft = models.BooleanField(verbose_name="Shared",default=True)
    created_date = models.DateTimeField(verbose_name="Created Date",auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated_Date",auto_now=True)
    discount_percent = models.FloatField(default=0)

    @property
    def discount(self):
        if self.discount_percent > 0:
            discounted_price = self.price - self.price*self.discount_percent/100
            return discounted_price


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Product"
        verbose_name_plural ="Products"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category_detail', kwargs={'slug': self.slug})
    

