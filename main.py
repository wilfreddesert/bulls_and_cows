from random import sample

CRED = "\033[91m"
CGREEN = "\33[32m"
CVIOLET = "\33[35m"
CYELLOW = "\33[33m"
CBLUE = "\33[34m"

BRIEF_RULES = """
Your guess must be a sequence of 4 unique digits. The sequence can start with 0. 
If you guess the digit and its position -- it's a bull. 
If only the digit, but not the position is correct -- it's a cow. 
Note that what is counted as a bull does not increment the cow count.  

"""

MAX_STEPS = 10
SEQUENCE_LENGTH = 4


def random_combination(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = sample(range(n), r)
    return tuple(pool[i] for i in indices)


def create_number(length):
    digits = list(range(10))
    random_item = random_combination(digits, length)
    return "".join(str(item) for item in random_item)


def check_guess(correct, guess):
    bulls, cows = 0, 0
    for i, g in enumerate(guess):
        if g in correct:
            if correct[i] == g:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def is_valid_guess(guess, length):
    return (
        len(guess) == length
        and len(guess) == len(set(guess))
        and all(char.isnumeric() for char in guess)
    )


def start_game(length):
    number = create_number(length)
    print(f"{CBLUE}{BRIEF_RULES}")
    step = 0
    while True:
        if step == MAX_STEPS:
            print(
                f"{CRED}You did not make it in {MAX_STEPS} steps. The number was {number}"
            )
            break
        guess = input(f"{CVIOLET}Enter your guess. \n")
        if not is_valid_guess(guess, length):
            print(f"{CRED}Your guess violates the rules!\n")
            continue
        step += 1
        bulls, cows = check_guess(number, guess)
        if bulls == length:
            print(f"{CGREEN}You won at step {step}!")
            break
        print(f"{CYELLOW}You've got {bulls} bulls and {cows} cows at step {step}\n")


if __name__ == "__main__":
    start_game(SEQUENCE_LENGTH)
