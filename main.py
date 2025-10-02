import random

def main():
    print("Welcome to the number guessing game")
    difficulty = input("Enter the difficulty you want (Easy/Hard): ").lower()
    print("I will guess a number between 1 and 100")
    if difficulty == "easy":
        chance = 10
    elif difficulty == "hard":
        chance = 5
    else:
        print("Enter a valid option")
    print(f"You have {chance} chances to guess the correct number")
    result = game_start(chance)
    if result:
        print("Congrats you chose the right number")
    else:
        print("You lost :(")

def game_start(chance):
    count = 0
    num_to_guess = random.randint(1, 100)
    while True:
        if count >= chance:
            return False
        num_guess = int(input("Guess the number: "))
        if num_guess == num_to_guess:
            return True
        elif num_guess > num_to_guess:
            print("Too big guess again")
        elif num_guess < num_to_guess:
            print("Too small guess again")
        count += 1


if __name__ == "__main__":
    main()