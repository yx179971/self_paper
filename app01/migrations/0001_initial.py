# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128, verbose_name='答案内容')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ManyToManyField(to='app01.Answer', verbose_name='答案')),
            ],
        ),
        migrations.CreateModel(
            name='BasePaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='问卷标题')),
            ],
        ),
        migrations.CreateModel(
            name='PaperRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.BasePaper')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='问题标题')),
                ('description', models.CharField(blank=True, max_length=128, null=True, verbose_name='问题描述')),
                ('kind', models.SmallIntegerField(choices=[(1, '单选'), (2, '多选'), (3, '文本')], verbose_name='问题类型')),
            ],
        ),
        migrations.AddField(
            model_name='basepaper',
            name='question',
            field=models.ManyToManyField(to='app01.Question', verbose_name='问题'),
        ),
        migrations.AddField(
            model_name='answerrecord',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.PaperRecord',
                                    verbose_name='所属问卷'),
        ),
        migrations.AddField(
            model_name='answerrecord',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Question',
                                    verbose_name='所属问题'),
        ),
    ]
