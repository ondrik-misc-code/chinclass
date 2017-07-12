from django.contrib import admin

from .models import Test
from .models import FillInTask
from .models import MultipleChoiceTask
from .models import MCQuestion
from .models import MCQuestionChoice

admin.site.register(Test)
admin.site.register(FillInTask)
admin.site.register(MultipleChoiceTask)
admin.site.register(MCQuestion)
admin.site.register(MCQuestionChoice)
