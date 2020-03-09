import random

answer = random.choice(['rock','paper','scissors'])

while True:

    try:
        guess = input('choose your operation')
        if guess=='rock'and answer=='rock':
            print("draw match")
            print(answer)
            break
        elif guess=='rock' and answer=='paper':
            print(f'computer wins because it choose {answer}')
            break
        elif guess=='rock' and answer=='scissors':
            print(f'user wins because computer choose {answer}')
            break

        elif guess=='paper'and answer=='paper':
            print("draw match")
            break
        elif guess=='paper' and answer=='scissors':
            print(f'computer wins because it choose {answer}')
            break
        elif guess=='paper' and answer=='rock':
            print(f'user wins because computer choose {answer}')
            break

        elif guess=='scissors'and answer=='rock':
            print(f'computer wins because it choose {answer}')
            break
        elif guess=='scissors' and answer=='paper':
            print(f'user wins because computer choose {answer}')
            break
        elif guess=='scissors' and answer=='scissors':
            print("draw match")
            break
        else:
            print("invalid input")
    except ValueError:
        print('please enter number')
        continue
