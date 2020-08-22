from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    # for later
    # def get_absolue_url(self):
    #     pass


class Product(BaseModel):
    category = models.ForeignKey(Category,
                                 related_name="products",
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255,
                            db_index=True)
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True)
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    # for later
    # def get_absolute_url(self):
    #     pass


class Image(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    product = models.ForeignKey(Product,
                                related_name="images",
                                on_delete=models.CASCADE)
