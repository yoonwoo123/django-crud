from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10) # 몇 글자를 최대로할지 인자로 넘겨줘야함 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 추가
    updated_at = models.DateTimeField(auto_now=True)