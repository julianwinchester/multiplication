import random


numbers = list(range(1, 13))

def take_two():

    n1 = random.choice(numbers)
    n2 = random.choice(numbers)
    return n1, n2


def quiz(q=10):
    score = 0
    wrong = []

    for _ in range(q):
        n1, n2 = take_two()
        while True:
            try:
                answer = int(input('{} * {} = '.format(n1, n2)))
            except ValueError:
                print('Knock it of and get back to the multiplication facts!!:|')
            else:
                if answer == (n1 * n2):
                    print('Great job!!!Keep it up!!! :)')
                    score += 1
                    break
                else:
                    print('Nice try,but no cigar!!')
                    wrong.append((n1, n2))
                    break
        print('Current score: {} out of {}'.format(score, q))
        print('')
    print('You got {} out of {} correct!!!Nice!'.format(score, q))
    print('')
    if len(wrong) > 0:
        print('Here are the questions you didn\'t get.' )
        for pair in wrong:
            print('{} * {} = {}'.format(pair[0], pair[1], (pair[0] * pair[1])   ))

quiz(50)