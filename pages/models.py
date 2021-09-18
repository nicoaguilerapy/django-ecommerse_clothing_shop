from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Page(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100, blank = False, null = False)
    content = RichTextField(default = '')
    order = models.SmallIntegerField(default = 0, null = False, blank = False)
    slug = models.SlugField(blank = True, null = True)
    status = models.BooleanField('Visible/Invisible', default = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['order', 'title']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title