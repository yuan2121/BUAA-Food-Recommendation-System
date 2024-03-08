from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Tag(models.Model):
    tagName = models.CharField(max_length=32)


class Canteen(models.Model):
    name = models.CharField(max_length=32)


class Window(models.Model):
    name = models.CharField(max_length=32)
    canteen = models.ForeignKey(Canteen, on_delete=models.CASCADE)


class Dish(models.Model):
    name = models.CharField(max_length=32)
    window = models.ForeignKey(Window, on_delete=models.CASCADE)
    price = models.FloatField()
    score = models.FloatField()
    numComment = models.IntegerField()
    numPurchase = models.IntegerField()
    collectNum = models.IntegerField()
    type = models.CharField(max_length=32)
    tags = models.ManyToManyField(Tag)


class User(models.Model):
    userId = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    stuId = models.CharField(max_length=32)
    college = models.CharField(max_length=32)
    collectDishes = models.ManyToManyField(Dish, related_name='+')  # 收藏的菜
    collectWindows = models.ManyToManyField(Window, related_name='+')  # 收藏的窗口
    collectCanteens = models.ManyToManyField(Canteen, related_name='+')  # 收藏的食堂
    purchaseDishes = models.ManyToManyField(Dish, related_name='+')  # 买过的菜


class Comment(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()  # 1-5星
    likes = models.IntegerField()  # 点赞数
    time = models.CharField(max_length=32)
    replyNum = models.IntegerField()


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField()
    likes = models.IntegerField()  # 点赞数
    time = models.CharField(max_length=32)


@receiver(pre_save, sender=Reply)  # 触发器
def pre_save_reply(sender, instance, **kwargs):
    comment = instance.comment
    comment.replyNum += 1
    comment.save()
