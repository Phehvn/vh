from django.db import models
from slugify import slugify
from ckeditor.fields import RichTextField
# Create your models here.
sttChoice = ((1,'hiện'),(0,'ẩn'))
class Category(models.Model):
  cat_id = models.AutoField(primary_key = 'true')
  cat_name = models.CharField(max_length = 50,null = False)
  slug  = models.SlugField(unique=True)
  status = models.SmallIntegerField(choices = sttChoice)
  date_create = models.DateField()
  class Meta :
    db_table = 'tbl_Category'
    unique_together = ('cat_name','slug')

  def __str__(self):
    return self.cat_name
      
class Article(models.Model):
  listCategory = Category.objects.all()
  result = []
  for item in listCategory:
    result.append(
      (item.cat_id,item.cat_name)
    )
  art_id = models.AutoField(primary_key = 'true')
  art_name = models.CharField(max_length = 100,null = False)
  art_slug = models.SlugField(unique=True,max_length = 255)
  cat_id = models.IntegerField(null = False, choices = result)
  art_img = models.ImageField(max_length = 255,null = False)
  art_mo_ta = models.CharField(max_length = 150,null = False,default='mô tả ngắn gọn')
  description = RichTextField()
  status = models.SmallIntegerField(choices = sttChoice)
  date_create = models.DateField()
  class Meta:
    db_table = 'tbl_Product'
  def __str__(self):
    return self.art_name
  # def save(self, *args, **kwargs):
  #   txt = self.art_name
  #   r = slugify(txt)
  #   self.slug = r
  #   super(Article, self).save(*args, **kwargs)
