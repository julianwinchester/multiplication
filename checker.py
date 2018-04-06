with open('tables.txt', 'r') as f:
    equations = f.read().splitlines()
    eq = [x for x in equations if x]

print('')
for e in eq:
    print(e)
    answer = int(e.rsplit('=')[-1].strip())
    num1, num2 = [int(x) for x in e.rsplit('=')[0].split('x')]
    try:
        assert(num1*num2 == answer)
    except AssertionError as e:
        print('INCORRECT: {}*{}={}'.format(num1, num2, answer))
        print('The answer is: {}'.format(num1*num2))
        print('')