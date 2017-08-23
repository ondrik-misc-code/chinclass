from django.contrib import admin

# from .models import Test
# from .models import FillInTask
# from .models import MCTask
# from .models import MCQuestion
# from .models import MCQuestionChoice
from .models import *

admin.site.register(Test)
admin.site.register(FillInTask)
admin.site.register(MCTask)
admin.site.register(MCQuestion)
admin.site.register(MCQuestionChoice)
admin.site.register(SubmTest)
