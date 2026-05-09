import random


def main():
    print("Welcome to Number Guesser!\n")

    keepPlaying = "y"
    storedScores = []

    while keepPlaying == "y":

        lower_bound = (int)(input("Input a lower bound: "))
        upper_bound = (int)(input("Input an upper bound: "))
        target_num = random.randint(lower_bound, upper_bound)
        num = (int)(input(
            f"Take a guess at what number I'm thinking of between {lower_bound} and {upper_bound}: "))
        guess_count = 1

        while num != target_num:
            num = (int)(input("Wrong, guess again: "))
            guess_count += 1

        keepPlaying = input(
            f"Great job! It took you {guess_count} amount of tries to guess the number correctly. Play again? (y/n) ")
        storedScores.append(guess_count)

    bestScore = storedScores[0]

    for score in storedScores:
        if score < bestScore:
            bestScore = score

    print()
    print(f"Best Score: {bestScore}")


if __name__ == "__main__":
    main()
