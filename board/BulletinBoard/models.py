from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


class Ads(models.Model):
    CHOICE = [
        ('TANKS', 'Танки'),
        ('HEALERS', 'Хилы'),
        ('DAMAGE_DILERS', 'ДД'),
        ('MERCHANTS', 'Торговцы'),
        ('GUILDMASTER', 'Гилдмастеры'),
        ('QUESTGIVERS', 'Квестгиверы'),
        ('BLACKSMITH', 'Кузнецы'),
        ('LEATHER_WORKER', 'Кожевники'),
        ('POTION_MAKERS', 'Зельевары'),
        ('SPELL_MASTER', 'Мастера заклинаний '),
    ]
    Ads_author = models.OneToOneField(User, on_delete=models.CASCADE)
    Ads_header = models.CharField(max_length=64, default="Без темы")
    Ads_category = models.CharField(max_length=20, choices=CHOICE)
    Ads_field = tinymce_models.HTMLField()


class Comment(models.Model):
    Comment_Ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    Comment_Author = models.OneToOneField(User, on_delete=models.CASCADE)
    Comment_Text = models.TextField()
    Comment_Status = models.BooleanField(default=False)
