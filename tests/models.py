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
    task_type = models.IntegerField(default=0)

    class Meta:
        abstract = True

###############################
class MultipleChoiceTask(Task):
    @property
    def max_points(self):
        result = 0
        for q in self.mcquestion_set.all():
            result += q.points

        return result

###############################
class FillInTask(Task):
    pass

###############################
class MCQuestion(models.Model):
    task = models.ForeignKey(MultipleChoiceTask, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    question_text = models.CharField(max_length=400)

    def __str__(self):
        return self.question_text

###############################
class MCQuestionChoice(models.Model):
    question = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

###########################################
class Submission:
    '''Submission

TODO
'''
    pass


