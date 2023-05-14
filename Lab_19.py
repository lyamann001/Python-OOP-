
# Mini Quiz
# Question sınıf oluşturalım. parametreler, text, choices, answer
# Question sınıfının checkanswer isimli bir fonksiyonu olacak. Cevabın doğruluğunu kontrol edecek.
# Quiz bir sınıf oluşturacağız. questions diye parametresi olacak.
# GetQuestion isimli bir fonksiyonu olacak.
# displayQuesiton methodu olacak soruları ekrana basacak
# guess method sınavı yapacak kişi cevap verecek
# showScore bir method olsun
# questionIndex değeri tutalım (init'te oluştur). bu index vasıtasıyla progress  ekrana basalım
# loadExam medhodu yazalım tüm sistem burada çalışsın

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, userAnswer):
        return self.answer == userAnswer

q1 = Question('en iyi programlama dili hangisidir?', ['C#','Python','Java','Go'], 'Python')
q2 = Question('en popüler programlama dili hangisidir?', ['C#','Python','Java','Go'], 'Python')
q3 = Question('en çok kazandıran programlama dili hangisidir?', ['C#','Python','Java','Go'], 'Python')
q4 = Question('en kolay programlama dili hangisidir?', ['C#','Python','Java','Go'], 'Python')
q5 = Question('en çok sevilen programlama dili hangisidir?', ['C#','Python','Java','Go'], 'Python')
questions = [q1, q2, q3, q4, q5]


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"{self.questionIndex + 1}.Soru: {question.text}")

        for q in question.choices:
            print(' - ', q)

        answer = input("Cevap: ")
        self.quess(answer)
        self.loadQuiz()

    def quess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def showScore(self):
        print(f"Score: {self.score}")

    def loadQuiz(self):
        if len(self.questions) == self.questionIndex:
            print("Quiz Bitti..!")
            self.showScore()
        else:
            self.displayProgres()
            self.displayQuestion()

    def displayProgres(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            pass
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))

quiz = Quiz(questions)
quiz.loadQuiz()