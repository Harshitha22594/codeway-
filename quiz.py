import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Rules: Answer each question to the best of your ability.")
        print("Let's get started!\n")

    def present_question(self, question):
        print(question["question"])
        for i, choice in enumerate(question["choices"], 1):
            print(f"{i}. {choice}")
        user_answer = input("Your answer: ")
        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == "yes"

    def display_final_results(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        print("Thanks for playing!")

    def play_game(self):
        self.welcome_message()

        for question in self.questions:
            user_answer = self.present_question(question)
            self.evaluate_answer(user_answer, question["correct_answer"])

        self.display_final_results()

if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["Berlin", "Paris", "Rome", "Madrid"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["Mars", "Jupiter", "Venus", "Saturn"],
            "correct_answer": "Mars"
        },
        {
            "question": "What is the largest mammal in the world?",
            "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_answer": "Blue Whale"
        }
        # Add more questions as needed
    ]

    while True:
        game = QuizGame(quiz_questions)
        game.play_game()

        if not game.play_again():
            break

