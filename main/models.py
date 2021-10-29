from django.db import models
from django.contrib.auth.models import User

class MessageManager(models.Manager):
    def create_message(self, body, author):
        message = self.create(body=body, author=author)
        return message

class Message(models.Model):
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Sent by {self.author} at {self.created}'