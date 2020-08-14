from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.db import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import datetime


class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    image = models.ImageField(default='images/base_image.png', upload_to='images/',
                              null=True, blank=True)
    content = RichTextUploadingField()
    published_date = models.DateTimeField(
        blank=True, null=True)

    def get_date(self):
        calendar = {1: 'января', 2: 'февраля', 3: 'марта',
                    4: 'апреля', 5: 'мая', 6: 'июня',
                    7: 'июля', 8: 'августа', 9: 'сентября',
                    10: 'октябрь', 11: 'ноября', 12: 'декабря'}
        if self.published_date:
            year = self.published_date.date().year
            month = calendar[self.published_date.date().month]
            day = self.published_date.date().day
            time = self.published_date.time().strftime('%H:%M')
            print(' '.join((str(day), month, str(year), str(time))))
            return ' '.join((str(day), month, str(year), str(time)))
        else:
            return ''
