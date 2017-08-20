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
        return \
            list(self.mctask_set.all()) + \
            list(self.fillintask_set.all()) + \
            list()


###############################
class Task(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    task_type = models.IntegerField(default=0)

    class Meta:
        abstract = True

###############################
class MCTask(Task):
    ''' A multiple choice task.
'''
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
    task = models.ForeignKey(MCTask, on_delete=models.CASCADE)
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
class SubmTest(models.Model):
    '''Submitted solution of a test

TODO
'''
    student_name = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    @property        # only getter
    def tasks(self):
        return \
            list(self.submmctask_set.all()) + \
            list()

###########################################
class SubmTask(models.Model):
    '''Submitted solution of a task

'''
    subm_test = models.ForeignKey(SubmTest, on_delete=models.CASCADE)

    class Meta:
        abstract = True

###########################################
class SubmMCTask(SubmTask):
    '''Submitted solution of a multiple choice task

TODO
'''
    task = models.ForeignKey(MCTask, on_delete=models.CASCADE)
