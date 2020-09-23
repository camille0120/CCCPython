import random
ans = random.randint(1,10)
t=0
while t<5:
    guess = int(input('Guess a number(1-10)?'))
    if (guess>10) or (guess<1):
        print('輸入錯誤！')
       
    else:
         t=t+1
         if guess==ans:
            print('right,','共猜了',t,'次')
            break
           
         elif guess>ans:
            print('wrong, smaller')
           
         else:
            print('wrong, bigger')
          


