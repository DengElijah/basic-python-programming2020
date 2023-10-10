print("welcome to my computer quiz")

playing=input("do you want to play? ")

if playing.lower() !="yes":
    quit() 

print("okay let's play :)")
score=0

answer=input("what does the word cpu stand for: ")
if answer.lower() =="central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer=input("what does the word GPU stand for: ")
if answer.lower() =="graphic processing unit":
    print("correct!")
    score += 1 
else:
    print("incorrect!")

answer=input("what does the word PSU stand for: ")
if answer.lower() =="power supply unit":
    print("correct!")
    score +=1
else:
    print("incorrect!")

answer=input("what does the word RAM stand for: ")
if answer.lower() =="random access memmory":
    print("correct!")
    score +=1
else:
    print("incorrect!")

answer=input("what does the word ROM stand for: ")
if answer.lower() =="read only memmory":
    print("correct!")
    score +=1
else:
    print("incorrect!")


answer=input("what does the word CD stand for:  ")
if answer.lower() =="compact Disk":
    print("correct!")
    score +=1
else:
    print("incorrect!")


    print("you got "+ str(score) +" out of 6 questions correct")
    print("you got "+ str((score /6)*100) +"%")
