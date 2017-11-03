from . import models
from arya.service import sites
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.shortcuts import redirect, render
import copy


class Detail(sites.AryaConfig):
    def detail_url(self, pk):
        base_url = reverse('{0}:{1}_{2}_detail'.format(self.site.namespace, self.app_label, self.model_name),
                           args=(pk,))
        return base_url

    def get_questions_html(self, questions, obj):
        html_list = []
        for q in questions:
            q_title_tpl = '<label>{0}</label>'.format(q.title)
            tpl = []
            if q.kind == 1:
                a_list = []
                ar = q.answerrecord_set.filter(paper=obj).first()
                if ar:
                    for a in ar.answer.all():
                        op_tpl = '<option>{0}</option>'.format(a.content)
                        a_list.append(op_tpl)
                tpl = '<select>{0}</select>'.format(''.join(a_list))
            elif q.kind == 2:
                a_list = []
                ar = q.answerrecord_set.filter(paper=obj).first()
                if ar:
                    for a in ar.answer.all():
                        op_tpl = '<option>{0}</option>'.format(a.content)
                        a_list.append(op_tpl)
                tpl = '<select multiple="multiple">{0}</select>'.format(''.join(a_list))
            else:
                a = q.answerrecord_set.filter(paper=obj).first()
                tpl = '<p>{0}</p>'.format(a.answer.all().first().content if a else '')
            html_list.append(q_title_tpl)
            html_list.append(tpl)
        return '<br>'.join(html_list)

    def detail_view(self, request, pk, *args, **kwargs):
        obj = self.model_class.objects.filter(pk=pk).first()
        class_name = self.model_class._meta.model_name
        html = ''
        if class_name == 'basepaper':
            title_html = '<h1>{0}</h1>'.format(obj.title)
            questions = obj.question.all()
            html = title_html + '<br>'.join([q.title for q in questions])
        elif class_name == 'paperrecord':
            title_html = '<h1>{0}</h1>'.format(obj.base.title)
            questions = obj.base.question.all()
            html = title_html + self.get_questions_html(questions, obj)
        return render(request, 'arya/detail.html', {'html': mark_safe(html)})

    def list_display_show(self, obj=None, is_header=False):
        if is_header:
            return '查看'
        else:
            tpl = "<a href='{0}'>详细</a>".format(self.detail_url(obj.pk))
            return mark_safe(tpl)


class BasePaperConfig(Detail):
    def get_question(self, obj=None, is_header=False):
        if is_header:
            return '问题概略'
        else:
            li=[]
            for question in obj.question.all():
                li.append('<span style="border:1px solid #ddd;margin:2px;">{0}</span>'.format(question.title))
            return  mark_safe(''.join(li))

    list_display = ['title', get_question, Detail.list_display_show]


sites.site.register(models.BasePaper, BasePaperConfig)


class PaperRecordConfig(Detail):
    def get_PR_obj(self, obj=None, is_header=False):
        if is_header:
            return '问卷标题'
        else:
            return obj

    def is_pre(self, cl_obj, option):
        return sites.FilterRow(option, cl_obj, ((0, '用户模板'), (1, '模板')), self.request.GET, is_choice=True)

    def is_std(self, cl_obj, option):
        return sites.FilterRow(option, cl_obj, ((0, '用户答案'), (1, '标准答案')), self.request.GET, is_choice=True)
    list_display = [get_PR_obj, Detail.list_display_show, 'is_pre', 'is_std']
    list_filter = [sites.FilterOption(is_pre, False),
                   sites.FilterOption(is_std, False), ]


sites.site.register(models.PaperRecord, PaperRecordConfig)


class QuestionConfig(Detail):
    def get_kind(self, obj=None, is_header=False):
        if is_header:
            return '问题类型'
        else:
            return obj.get_kind_display()
    list_display = ['title','description',get_kind]
sites.site.register(models.Question,QuestionConfig)


class AnswerRecordConfig(Detail):
    def get_answers(self, obj=None, is_header=False):
        if is_header:
            return '内容'
        else:
            tpl_list = []
            for a in obj.answer.all():
                tpl_list.append('<span style="border:1px solid #ddd;margin:2px;">{0}</span>'.format(a))
            return mark_safe(''.join(tpl_list))

    list_display = [get_answers, 'question', 'paper']


sites.site.register(models.AnswerRecord, AnswerRecordConfig)


class AnswerConfig(Detail):
    pass
sites.site.register(models.Answer,AnswerConfig)