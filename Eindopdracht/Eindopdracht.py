# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("GOED!")
        return 1
    else:
        print("FOUT!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("Resultaten")
    print("-------------------------")

    print("Antwoorden: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("raad: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Je score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Wil je opnieuw spelen? (JA of NEE): ")
    response = response.upper()

    if response == "Correct":
        return True
    else:
        return False
# -------------------------


questions = {
 "Wat is mijn naam?: ": "D",
 "Hoe oud ben ik?: ": "C",
 "Hoe lang is de Eiffeltoren?: ": "D",
 "Wie is de bedenker van de Eiffeltoren?: ": "C"
}

options = [["A. Ahmed hari", "B. Joop", "C. Mohammed", "D. Mete Sariguney"],
          ["A. 14", "B. 19", "C. 16", "D. 21"],
          ["A. 255m", "B. 300m", "C. 350m", "D. 324m"],
          ["A. Ali","B. Michael Jackson", "C. Gustavo Eiffel", "D. Ik weet het niet"]]

new_game()

while play_again():
    new_game()

print("Einde!")

# -------------------------