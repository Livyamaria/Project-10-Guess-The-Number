from random import*
from art import logo
def guess_checking(computer_chosen,count):
 while count !=0:

  user_chosen=int(input("Make a guess  :"))
  if computer_chosen ==user_chosen:
    print("Lucky!..Guess is correct,You got it!!")
  elif computer_chosen<user_chosen:
    print("Guess is too high")
    count -=1
    print(f"--------You have {count} attempts remaining to guess the number--------")
  elif computer_chosen > user_chosen:
    print("Guess is too low")
    count -=1
    print(f"--------You ave {count} attempts remaining to guess the number--------")
print("*******You have run out of the guess ,You lose*******")

easy_count=5
difficult_count=10
computer_chosen=randint(0,100)
print(logo)
count=input("select the Easy or Difficult challenge ,e for easy and d for difficult :")
if "e"==count:
    count=easy_count
elif "d" ==count:
    count=difficult_count

guess_checking(computer_chosen,count)