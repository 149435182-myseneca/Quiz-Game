def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        choose = ["A", "B", "C", "D"]
        guess = None
        while guess not in choose:
            guess = input("Enter answer : ").upper()
            guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#----------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Fucking Correct")
        return 1
    else:
        print("WRONG !")
        return 0

#----------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("Results : ")
    print("------------------------------")
    print("Answers : ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses : ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = (correct_guesses/len(questions)*100)
    print("You score is : " + str(score) + "%")
#----------------------------
def play_again():
    response = input("Do you want to play again ?")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who created Python ? : ": "A",
    "Python is tributed to which comedy group ? :": "C",
    "What year was Python created ? : ": "B",
    "Is the Earth round ? : " : "A"
}
options = [["A. Guido", "B. Elon Musk", "C. Bill", "D. Mark"],
           ["A.Lonely Island", "B. 'Smosh'", "C. Monty", "D. SNL" ],
           ["A. 1989","B. 2021", "C. 2000", "D. 2011"],
           ["A. True", "B. False", "C. Sometimes", "D. I dont know !"]]

new_game()

while play_again():
    new_game()
print("Bye, thank you !")