from django.contrib import admin
from . import models


admin.site.register(models.BasePaper)
admin.site.register(models.PaperRecord)
admin.site.register(models.Question)
admin.site.register(models.AnswerRecord)
admin.site.register(models.Answer)
