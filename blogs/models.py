# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.text import slugify

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     slug = models.SlugField(unique=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.title)
#             slug = base_slug
#             counter = 1
#             while Post.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#             self.slug = slug
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f'{self.title} - by {self.author.username}'

#     def current_ist_time(self):
#         current_time_ist = timezone.localtime(
#             timezone.now(), timezone.pytz.timezone('Asia/Kolkata')
#         )
#         return current_time_ist.strftime("%Y-%m-%d %H:%M:%S")
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        permissions = [
            ("can_create_post", "Can create a post"),
            ("can_edit_post", "Can edit own post"),
            ("can_delete_post", "Can delete own post"),
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - by {self.author.username}'

    def current_ist_time(self):
        current_time_ist = timezone.localtime(
            timezone.now(), timezone.pytz.timezone('Asia/Kolkata')
        )
        return current_time_ist.strftime("%Y-%m-%d %H:%M:%S")
