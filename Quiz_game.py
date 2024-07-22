import random

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions on a specific topic.")
    print("For each correct answer, you will earn points. Try to get the highest score!")
    print("Let's get started!\n")

def load_quiz_questions():
    questions = [
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "C"
        },
        {
            "question": "Who developed the theory of relativity?",
            "choices": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "choices": ["A. Au", "B. Ag", "C. Fe", "D. Pb"],
            "answer": "A"
        },
        {
            "question": "Which element is said to keep bones strong?",
            "choices": ["A. Iron", "B. Calcium", "C. Sodium", "D. Potassium"],
            "answer": "B"
        },
        {
            "question": "What is the capital city of Japan?",
            "choices": ["A. Beijing", "B. Seoul", "C. Bangkok", "D. Tokyo"],
            "answer": "D"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "choices": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"],
            "answer": "C"
        },
        {
            "question": "Who is known as the father of computers?",
            "choices": ["A. Charles Babbage", "B. Alan Turing", "C. John von Neumann", "D. Bill Gates"],
            "answer": "A"
        },
        {
            "question": "What is the main gas found in the air we breathe?",
            "choices": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "B"
        },
        {
            "question": "Which ocean is the largest in the world?",
            "choices": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            "answer": "D"
        }
    ]
    random.shuffle(questions)
    return questions

def present_quiz_questions(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for choice in question["choices"]:
            print(choice)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_choice = question["choices"][ord(question["answer"]) - 65]
            print(f"Incorrect. The correct answer was: {correct_choice}\n")

    return score

def display_final_results(score, total_questions):
    print(f"Your final score is {score} out of {total_questions}.")
    if score == total_questions:
        print("Excellent! You got all the questions correct!")
    elif score > total_questions // 2:
        print("Good job! You got more than half of the questions right.")
    else:
        print("Better luck next time. Try to improve your score!")

def play_again():
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input in ("yes", "no"):
            return play_again_input == "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    display_welcome_message()
    while True:
        questions = load_quiz_questions()
        score = present_quiz_questions(questions)
        display_final_results(score, len(questions))
        
        if not play_again():
            print("Thank you for playing the Quiz Game!")
            break

if __name__ == "__main__":
    main()
