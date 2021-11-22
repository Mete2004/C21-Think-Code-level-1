print('Welcome to Mete his quiz')
answer=input('Are you ready to play my first Quiz ? (yes/no) :')
score=0
total_questions=5
 


if answer.lower()=='yes':
  
    answer=input('Question 1: What do you know about Python?')
  
    if answer.lower()=='yes':
        score += 1
        print('correct')

 
    
    answer=input('Question 2: Have you ever coded with Python, if so how often? ')
   
    if answer.lower()=='yes':
        score += 1
        print('correct')
   
 
    
    answer=input('Question 3: Do you like coding? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    
    
    
    answer=input('Question 4: What is your feedback on my first quiz? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
   
    
    answer=input('Question 5: what color is a banana? ')
    if answer.lower()=='yellow':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

 
print('Thankyou for Playing my first quiz game, im super glad you played my first quiz. you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')