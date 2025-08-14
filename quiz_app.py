import random
from quiz_data import quiz_questions # type: ignore

def run_quiz():
    score = 0
    questions = quiz_questions.copy()
    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}.")

    print(f"\n🎯 Final Score: {score}/{len(questions)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    run_quiz()
