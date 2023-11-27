def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess= input("Enter: (A, B, C, or D): ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guesses,guesses)

def check_answer(answer, guess):
    if answer==guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
def display_score(correct_guesses,guesses):
    print("----------")
    print("Results")
    print("----------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score=int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
def play_again():
    response=input("Do you want to play again? (yes or no): ")
    response=response.upper()
    if response=="YES":
        return True
    else:
        return False


questions={"What is the powerhouse of cell?: ":"A", "What is the first element in the periodic table?: ": "B",
           "What is distance over time?: ":"C", "What is zero factorial?: ": "A"}
options=[["A. Mitochondria", "B. Cytoplasm", "C. Heart","D. Cellular wall"],
         ["A. Helium", "B. Hydrogen", "C. Sodium","D. Proton"],
         ["A. Acceleration", "B. Velocity", "C. Speed","D. Gravity"],
         ["A. 1", "B. 0", "C. 10","D. 100 "]]

new_game()
while play_again():
    new_game()
print("Thank you for playing, see you next time!")