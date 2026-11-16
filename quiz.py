class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def display(self):
        print(self.question)
        number = 1
        for choice in self.choices:
            print(str(number) + ". " + choice)
            number = number + 1

    def check_answer(self, user_answer):
        return user_answer == self.answer