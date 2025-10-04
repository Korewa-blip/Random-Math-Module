import random
playing=True
number=str(random.randint(10,20))
print(number)
print("I will give you a number from 10 to 20 and you have to guess the number one digit at a time ")
print("The game ends if you guess the number")
while playing:
 guess=input("Give me your best guess! \n")
 if number==guess:
   print("You win")
   print("The number was",number)
   break
 else:
   print("Your guess wasnt right")