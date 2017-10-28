from django.db import models


class Paper(models.Model):
    is_base = models.BooleanField(default=False, verbose_name='是否模板')
    title = models.CharField(max_length=32, verbose_name='问卷标题')
    question = models.ManyToManyField(to='Question', verbose_name='问题')

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name='问题标题')
    description = models.CharField(max_length=128, verbose_name='问题描述', blank=True, null=True)
    kind_choices = (
        (1, '单选'),
        (2, '多选'),
        (3, '文本')
    )
    kind = models.SmallIntegerField(choices=kind_choices, verbose_name='问题类型')

    def __str__(self):
        return self.title


class Record(models.Model):
    """回答记录"""
    paper = models.ForeignKey(to=Paper, verbose_name='所属问卷')
    question = models.ForeignKey(to=Question, verbose_name='所属问题')
    answer = models.ManyToManyField(to='Answer', verbose_name='答案')

    def __str__(self):
        return self.question.title


class Answer(models.Model):
    content = models.CharField(max_length=128, verbose_name='答案内容')

    def __str__(self):
        return self.content[:10 if len(self.content) > 9 else len(self.content)]