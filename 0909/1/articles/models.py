from django.db import models
from imagekit.models import ProcessedImageField,  ImageSpecField
from imagekit.processors import Thumbnail
from imagekit.specs import ImageSpec
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    image=models.ImageField(blank=True,upload_to='images/%Y/%m/%d/')
    image_thumbnail=ImageSpecField(
        source='image', #원본 이미지 필드명 
        processors=[Thumbnail(200,200)],
        format='JPEG',
        options={'quality':90},
    )
    # image_thumb=ProcessedImageField(
    #     blank=True,
    #     processors=[Thumbnail(200,200)],
    #     format='JPEG',
    #     options={'quality':90},)
        #썸네일 이미지를 만듬! 원본이미지를 가공하여 넣기때문에 원본은 저장하지 않는다 /썸네일만 저장함 

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title