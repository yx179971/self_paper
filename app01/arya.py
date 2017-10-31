from . import models
from arya.service import sites
from django.utils.safestring import mark_safe


class PaperConfig(sites.AryaConfig):
    def get_question(self, obj=None, is_header=False):
        if is_header:
            return '问题概略'
        else:
            li=[]
            for question in obj.question.all():
                li.append('<span style="border:1px solid #ddd;margin:2px;">{0}</span>'.format(question.title))
            return  mark_safe(''.join(li))

    def get_is_base(self, obj=None, is_header=False):
        if is_header:
            return '是否模板'
        else:
            if obj.is_base:
                return '模板'
            else:
                return ''
    list_display = ['title',get_question,get_is_base]
sites.site.register(models.Paper,PaperConfig)


class QuestionConfig(sites.AryaConfig):
    def get_kind(self, obj=None, is_header=False):
        if is_header:
            return '问题类型'
        else:
            return obj.get_kind_display()
    list_display = ['title','description',get_kind]
sites.site.register(models.Question,QuestionConfig)


class RecordConfig(sites.AryaConfig):
    pass
sites.site.register(models.Record,RecordConfig)


class AnswerConfig(sites.AryaConfig):
    pass
sites.site.register(models.Answer,AnswerConfig)