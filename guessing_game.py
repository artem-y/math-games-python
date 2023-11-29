import random
import time

def guess_the_number():
    number = random.randint(0, 1000)
    guess_count = 0
    start_time = time.time()

    while True:
        guess = input("Guess the number between 0 and 1000: ")
        guess_count += 1

        try:
            guess = int(guess)
        except ValueError:
            # Notify user about invalid input and skip this iteration
            print("Invalid input. Expected an integer.")
            continue

        # Give user a hint if they are wrong
        if guess > number:
            print(f"Wrong! {guess} is too high.")
        elif guess < number:
            print(f"Wrong! {guess} is too low.")
        else:
            # The number was guessed correctly, break the loop and 
            print(f"Congratulations! {guess} is the right number!")
            break
    
    # Measure time and number of guesses, print results
    end_time = time.time()
    time_passed = end_time - start_time

    print(f"It took you {guess_count} guesses and {time_passed:.2f} seconds.")

if __name__ == "__main__":
    guess_the_number()
