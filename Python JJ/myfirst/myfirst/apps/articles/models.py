from django.db import models

class User(models.Model):
    username_title = models.CharField('Имя', max_length = 200)
    phone_text = models.TextField('Номер телефона')
    email_text = models.TextField('Емейл')
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
