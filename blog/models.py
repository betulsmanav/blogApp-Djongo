import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


CATEGORY = (
    (None, 'Choose...'),
    ('Technology','Technology'),
    ('Software','Software'),
    ('Business','Business'),
    ('Fashion','Fashion'),
    ('Lifestyle','Lifestyle'),
    ('Travel','Travel'),
    ('Food','Food'),
)
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.CharField(max_length=500,  default="https://images.ctfassets.net/23aumh6u8s0i/6ubUHRD1qfolOVHxiBfjZ7/4e704f48dc5b0104d0c380fec1fe9b9e/django")
    category=models.CharField(max_length=50,choices=CATEGORY, blank=True,verbose_name="category", default="category")
    publish_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(null=False, unique=True)


    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    
    def get_comment_count(self):
        comments = Comment.objects.all()
        return comments.count()

    def get_view_count(self):
        return PostView.objects.filter(post=self).count()

    def get_like_count(self):
        return Like.objects.filter(post=self).count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    
        
class Like(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title
class PostView(models.Model):
    time_stamp = models.DateTimeField(auto_now=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.user
        
