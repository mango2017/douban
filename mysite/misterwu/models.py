from django.db import models

# Create your models here.

class Teacher(models.Model):
    nickname = models.CharField(max_length=30,primary_key=True,db_index=True,verbose_name="昵称")
    introduction = models.TextField(default='这位同学很懒，木有签名的说~',verbose_name="简介")
    fans = models.PositiveIntegerField(default="0",verbose_name="粉丝数")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    class Meta:
        verbose_name = "讲师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Course(models.Model):
    title = models.CharField(max_length=100,primary_key=True,db_index=True,verbose_name="课程名")
    type = models.CharField(choices=((1,"实战课"),(2,"免费课"),(0,"其他")),max_length=1,default=0,verbose_name="课程类型")
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.get_type_display()}-{self.title}"


class Student(models.Model):
    nickname = models.CharField(max_length=30,primary_key=True,db_index=True,verbose_name="昵称")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(choices=((1,"男"),(2,"女"),(0,"保密")),max_length=1,default=0,verbose_name="性别")
    study_time = models.PositiveIntegerField(default="0",verbose_name="学习时长（h）")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        verbose_name = "学生信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname