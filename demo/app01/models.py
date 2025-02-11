from django.db import models
from account.models import User
from utils.basemodels import BaseModel

# Create your models here.
class Article(BaseModel):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'
        verbose_name = '文章信息'
        ordering = ['-publish_date']
