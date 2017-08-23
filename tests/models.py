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

    ###############################
    @property        # only getter
    def tasks(self):
        return \
            list(self.mctask_set.all()) + \
            list(self.fillintask_set.all()) + \
            list()

    ###########################################
    def score_for(self, subm_test):
        '''score_for(self, SubmTest) -> int

The total score for the test for the given submission.
'''
        acc = 0
        for task in self.tasks:
            acc += task.score_for(subm_test)

        return acc


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

    ###########################################
    def score_for(self, subm_test):
        '''score_for(self, SubmTest) -> int

Computes the total score for the given MC task for the given submission.
'''
        acc = 0
        for mcquest in self.mcquestion_set.all():
            acc += mcquest.score_for(subm_test)

        return acc


###############################
class FillInTask(Task):
    pass

###############################
class MCQuestion(models.Model):
    task = models.ForeignKey(MCTask, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    question_text = models.CharField(max_length=400)

    ############################
    def __str__(self):
        return self.question_text

    ###########################################
    def correct_answer_for(self, subm_test):
        '''correct_answer(self, SubmTest) -> bool

Determines whether the given test answer the question correctly.
'''
        answer = subm_test.submmcquestion_set.filter(mcquest=self)
        if len(answer) != 1:
            return False
        else:
            return answer.first().correct

    ###########################################
    def score_for(self, subm_test):
        '''score_for(self, SubmTest) -> int

Gives the score for the MC question for the given submission.
'''
        return self.points if self.correct_answer_for(subm_test) else 0


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

    ###########################################
    def __str__(self):
        return str(self.test) + ' - ' + self.student_name

    ###########################################
    @property                # only getter
    def score(self):
        '''score(self) -> int

The total score for the test
'''
        return self.test.score_for(self)


###########################################
class SubmMCQuestion(models.Model):
    '''Submitted answer to a multiple choice task question

TODO
'''
    subm_test = models.ForeignKey(SubmTest, on_delete=models.CASCADE)
    mcquest = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    mcquestchoice = models.ForeignKey(MCQuestionChoice, \
        on_delete=models.SET_NULL, null=True)

    ###########################################
    @property           # only getter
    def correct(self):
        if self.mcquestchoice:
            return self.mcquestchoice.correct
        else:
            return False

    ###########################################
    @property           # only getter
    def score(self):
        return self.mcquest.points if self.correct else 0

    ###########################################
    def __str__(self):
        return str((self.subm_test, self.mcquest, self.mcquestchoice))
