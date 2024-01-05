import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_craps():
    # Initial roll
    first_roll = sum(roll_dice())
    print(f"You rolled {first_roll}")

    if first_roll in (7, 11):
        print("You win!")
    elif first_roll in (2, 3, 12):
        print("You lose!")
    else:
        point = first_roll
        print(f"Point is {point}")

        # Continue rolling until 7 or the point is rolled
        while True:
            roll_sum = sum(roll_dice())
            print(f"You rolled {roll_sum}")

            if roll_sum == 7:
                print("You lose!")
                break
            elif roll_sum == point:
                print("You win!")
                break


play_craps()
