from django.db import models
from django.conf import settings

# Create your models here.
class News(models.Model):
    title = models.TextField()
    text_czech = models.TextField()
    text_english = models.TextField()
    text_chinese = models.TextField()
    user_added = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_created = models.DateTimeField(auto_now_add=True)

    ###########################################
    def __str__(self):
        return str((self.title, self.text, self.user_added, self.date_created))
