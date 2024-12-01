def ask_question(question, options, correct_answer):

    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    try:
        user_answer = int(input("Choose the correct answer (1, 2, 3, or 4): "))
        if user_answer == correct_answer:
            print("Correct!\n")
            return 1
        else:
            print("Incorrect.\n")
            return 0
    except ValueError:
        print("Invalid input. Please choose a number between 1 and 4.\n")
        return 0


def main():
    # List of questions, options, and the correct answer (index starts from 1)
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": 2
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
            "correct_answer": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_answer": 4
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
            "correct_answer": 2
        }
    ]

    score = 0

    # Loop through each question and ask it
    for question_data in questions:
        score += ask_question(question_data["question"], question_data["options"], question_data["correct_answer"])

    print(f"Your final score is: {score}/{len(questions)}")

    # Show a message based on the score
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score >= len(questions) // 2:
        print("Good job! You answered more than half correctly.")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
