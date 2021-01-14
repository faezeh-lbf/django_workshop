from django.db import models

# Create your models here.
class BlogPost(models.Model):
    photo = models.ImageField(upload_to='blog/', null=True, blank=True, help_text="برای نمایش بهتر در سایت، باید نسبت ابعاد تصویر بین ۰.۸ تا ۱.۲ باشد.")
    title = models.CharField(max_length=70, null=False, blank=False)
    summary = models.TextField(max_length=100, null=False, blank=False)
    publish_date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False)
    author_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    publish_time = models.DateTimeField()
    show = models.BooleanField(null=False, blank=False, default=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return 'post number' + str(self.post.id) + ' -  ' + str(self.id)

