import random
ans = random.randint(1,10)
while True:
    guess = int(input('Guess a number(1-10)?'))
    if guess==ans:
        print('right')
        break
    elif guess>ans:
        print('wrong, smaller')
    else:
        print('wrong, bigger')


