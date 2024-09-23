import random
guesses = 0

secret_number = random.randint(1 ,10)

guess = int(input("\nI am Thinking of a number between 1 and 10. Can you guess it? "))

guesses += 1

if guess == secret_number:
            print(f"\nCongratulations you have guessed correctlly in {guesses} guesses!!")

elif guess > 10:
            print("\nYou have entered a number greater than 10.")

elif guess < 1:
            print("\nYou have entered a number less 1")
        
elif guess > secret_number:
            print(f"\nYou have guessed a bit high by {guess - secret_number}. Please try again!!")
          
elif guess < secret_number:
            print(f"\nYou have guessed a bit low by {secret_number - guess}. Please Try again!!!")

else:
            print("\nInvalid Input")

while guess != secret_number:
        guess = int(input("\nI am Thinking of a number between 1 and 10. Can you guess it? "))
        guesses += 1

        if guess == secret_number:
            print(f"\nCongratulations you have guessed correctlly in {guesses} guesses!!")

        elif guess > 10:
            print("\nYou have entered a number greater than 10.")

        elif guess < 1:
            print("\nYou have entered a number less 1")
        
        elif guess > secret_number:
            print(f"\nYou have guessed a bit high by {guess - secret_number}. Please try again!!")
          
        elif guess < secret_number:
            print(f"\nYou have guessed a bit low by {secret_number - guess}. Please Try again!!!")

        else:
            print("\nInvalid Input")
        break

while guess == secret_number:

        play_again = input("\nDo you want to  play again? (yes/no): ")

        while play_again == "yes":

                import random
                guesses = 0

                secret_number = random.randint(1 ,10)


                guess = int(input("\nI am Thinking of a number between 1 and 10. Can you guess it? "))

                guesses += 1

                if guess == secret_number:
                        print(f"\nCongratulations you have guessed correctlly in {guesses} guesses!!")

                elif guess > 10:
                        print("\nYou have entered a number greater than 10.")

                elif guess < 1:
                        print("\nYou have entered a number less 1")
        
                elif guess > secret_number:
                        print(f"\nYou have guessed a bit high by {guess - secret_number}. Please try again!!")
          
                elif guess < secret_number:
                        print(f"\nYou have guessed a bit low by {secret_number - guess}. Please Try again!!!")

                else:
                        print("\nInvalid Input")

                while guess != secret_number:
                        guess = int(input("\nI am Thinking of a number between 1 and 10. Can you guess it? "))
                        guesses += 1

                        if guess == secret_number:
                                print(f"\nCongratulations you have guessed correctlly in {guesses} guesses!!")

                        elif guess > 10:
                                print("\nYou have entered a number greater than 10.")

                        elif guess < 1:
                                print("\nYou have entered a number less 1")
        
                        elif guess > secret_number:
                                print(f"\nYou have guessed a bit high by {guess - secret_number}. Please try again!!")
          
                        elif guess < secret_number:
                                print(f"\nYou have guessed a bit low by {secret_number - guess}. Please Try again!!!")

                        else:
                                print("\nInvalid Input")
                break
         
        else:
                print("\nThank you for playing my guessing game!!")
        