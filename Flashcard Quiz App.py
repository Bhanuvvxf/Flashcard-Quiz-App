import random

#Flashcard Quiz App

print("Welcome to the Flashcard Quiz App!")
print("You have 5 questions to answer.")
print("")

#questions 
questions = ["What is the capital of France?","What is the square root of 16?","Who wrote 'Romeo and Juliet'?","What is the chemical symbol for Water?","How many continents are there?"]

#answers
answers = ["Paris","4","William Shakespeare","H2O","7"] 

#random question 

random_question = random.randint(0,len(questions)-1)
#score 
score = 0
y = 1

question_number = 0
while True:
    
        x = questions.pop(random_question)
        a = answers.pop(random_question)
        print()
        print(f"Flashcard {y}:",x)
        y+=1
        answer =  input("Your answer: ")
        if answer == a :
            score += 1 
            print("Correct! Your score: ",score)
            print()
        else:
            print("wrong ! Your score: ",score)
            print()
        
        if len(questions) == 0 or len(answers) == 0 :
             print(f"Congratulations! You scored {score} out of 5!")
             break
        
        
