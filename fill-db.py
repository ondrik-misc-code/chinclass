#!/usr/bin/env python3
import os, django

MCTaskData = [
        [
            "你為什麼一直站？",
            ("你為什麼一直站著？", True),
            "你為什麼一直在站？" ],
        [
            "吃芒果很香、很甜。",
            "芒果吃來很香、很甜。",
            ("芒果吃起來很香、很甜。", True) ],
        [
            "陳月美的家離學校不很遠。",
            "陳月美的家不離學校很遠。",
            ("陳月美的家離學校很不遠。", True) ],
        [
            "馬安同喜歡一邊吃飯，一邊休息。",
            "馬安同喜歡一邊聽音樂，一邊睡覺。",
            ("馬安同喜歡一邊吃飯，一邊用手機上網。", True) ],
        [
            "田中誠一往學校門口出來從左轉去麵店吃飯。",
            ("田中誠一從學校門口出來往左轉去麵店吃飯。", True),
            "田中誠一從學校門口出來去左轉往麵店吃飯。" ]
    ]


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chinclass.settings")
    django.setup()

    from tests.models import Test
    test = Test(test_name = "第一課考試")
    test.save()
    print("Added test " + str(test.id) + ": \"" + test.test_name + "\"")

    from tests.models import TaskType
    from tests.models import MultipleChoiceTask
    mctask = MultipleChoiceTask(test=test, max_points=10, task_type=TaskType.MultipleChoice)
    mctask.save()
    print("Added multiple choice task " + str(mctask.id) + " to test " + str(mctask.test.id))

    from tests.models import MCQuestion
    from tests.models import MCQuestionChoice

    for quest in MCTaskData:
        mcquest = MCQuestion(task=mctask, points=2, question_text="哪一個是對的？")
        mcquest.save()
        print("Added multiple choice question " + str(mcquest.id) + ": \"" + mcquest.question_text + "\" to task " + str(mctask.id))

        for ch in quest:
            if isinstance(ch, tuple):
                (ch_text, correct) = ch
                ch = ch_text
            else:
                choice_text = ch
                correct = False

            choice = MCQuestionChoice(question=mcquest, choice_text=ch, correct=correct)
            choice.save()
            print("Added MC choice " + str(choice.id) + ": \"" + choice.choice_text + "\" " + ("YES" if correct else "NO") + " to question " + str(choice.question.id))
