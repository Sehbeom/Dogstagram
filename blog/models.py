from django.db import models

def get_memo_image_path(instance, filename):
    return 'blog/%s/%s' % (instance.pk, filename)

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_memo_image_path, default='')

    def save(self, *args, **kwargs):
        if self.id is None:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            
            self.image = temp_image
        super().save(*args, **kwargs)
