questions = {
    "what is the color": 'A',
    "How many days make a week": "C",
    "What is the capital of Nigeria": "D",
    "How many days in a year": "B"
}
options = [["A. Red", "B. Blue", "C. Green", "D. Yellow"], ["A. 3", "B. 6", "C. 7", "D. 9"],
           ["A. Oyo", "B. Abia", "C. Lagos", "D. Abuja"], ["A. 200", "B. 365", "C. 390", "D. 900"]]

def check_answer(answers):
    i = 0
    score = 0

    for key, value in questions.items():
        if value == answers[i]:
            score += 1
        i += 1

    return score

def new_game():
    while True:
        answers = []
        question_index = 0
        for question in questions:
            print("-------------------------------------------")
            print(question)
            for option in options[question_index]:
                print(option)
            answer = (input("A, B, C, or D? ")).upper()
            answers.append(answer)
            question_index += 1
        score = check_answer(answers)
        print("Final score: " + str(score) + "/" + str(len(questions)))

        response = (input("Do you want to play again Yes/No? ")).lower()
        if response == 'no':
            print("Thank you for playing")
            break

new_game()
