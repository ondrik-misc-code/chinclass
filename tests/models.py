from django.db import models
from enum import IntEnum, unique

###############################
@unique
class TaskType(IntEnum):
    MultipleChoice = 1,
    FillIn = 2


###############################
class Test(models.Model):
    test_name = models.CharField(max_length=400)

    def __str__(self):
        return self.test_name

    @property        # only getter
    def tasks(self):
        return list(self.multiplechoicetask_set.all()) + list(self.fillintask_set.all())


###############################
class Task(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    max_points = models.IntegerField(default=0)
    task_type = models.IntegerField(default=0)

    class Meta:
        abstract = True

###############################
class MultipleChoiceTask(Task):
    pass

###############################
class FillInTask(Task):
    pass

###############################
class MCQuestion(models.Model):
    task = models.ForeignKey(MultipleChoiceTask, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    question_text = models.CharField(max_length=400)
    correct_choice = models.ForeignKey('MCQuestionChoice', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

###############################
class MCQuestionChoice(models.Model):
    question = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400)

    def __str__(self):
        return self.choice_text
