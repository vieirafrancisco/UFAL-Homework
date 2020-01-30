from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Topic(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    # tag - ManyToManyField
    title = models.CharField(max_length=100)
    description = models.CharField(max_lenght=200)
    state = models.BooleanField(null=False)

    def __str__(self):
        return self.title

    def get_author_name(self):
        return manager.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

# create Tag model