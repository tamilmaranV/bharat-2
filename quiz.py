import time

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.text}")
            for j, option in enumerate(question.options, 1):
                print(f"{j}. {option}")

            user_answer = int(input("Your answer (enter the option number): "))
            if question.is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question.correct_option}: {question.options[question.correct_option - 1]}\n")

            time.sleep(1)  # Add a brief pause between questions

        print(f"Quiz complete! Your score: {self.score}/{len(self.questions)}")


# Sample questions
# Sample questions
questions = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 3),
    Question("Which programming language is this app written in?", ["Java", "Python", "C++", "JavaScript"], 2),
    Question("What is the largest planet in our solar system?", ["Mars", "Jupiter", "Venus", "Saturn"], 2),
    Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
    Question("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Endoplasmic reticulum", "Ribosome"], 2),
]


# Create and start the quiz
quiz = Quiz(questions)
quiz.start_quiz()
