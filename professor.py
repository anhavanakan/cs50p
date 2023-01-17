import random


def main():
    level = get_level()
    # we will add 1s to score and question's count
    score = 0
    questions = 0

    # user will recive 10 questions
    while questions < 10:
        # each question is addition of 2 random number with 'level' digiths each
        x = generate_integer(level)
        y = generate_integer(level)
        # storing users answer while printing it
        answer = print_answer(x, y)
        # if answer was right user gets 1 score otherwise nothing happens
        if answer == x + y:
            score += 1
        # and after each question we add count up to 10
        questions += 1
    # after all this we need to print also score
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    elif level == 3:
        number = random.randint(100, 999)
    return number


def print_answer(x, y):
    sum = x + y
    # how many times user has answered for 1 question
    answer_count = 0
    # to not be equal to sum in future comparison
    answer = -1
    while True:
        # if answer is correct break the loop and return it(in the end)
        if answer == sum:
            break
        # if it is 3, that means user typed wrong 3 times we should break the loop and return right answer
        if answer_count == 3:
            print(f"{x} + {y} = {x + y}")
            break
        try:
            # try to get answer
            answer = int(input(f"{x} + {y} = "))

            # if user gave you less than 3 answers keep asking
            while answer_count < 3:
                # it its not correct, print 'EEE', add to count and break the loop to ask again
                if answer != sum:
                    print("EEE")
                    answer_count += 1
                    break
                # if answer is correct break the loop, then we will break the main loop and return the answer
                else:
                    break
        except:
            # if any exception was found add to count and break the loop
            answer_count += 1
            continue
    # after all this hustle and bustle return users last answer
    return answer


if __name__ == "__main__":
    main()
