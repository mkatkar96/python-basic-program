#Q.1 check passwd authentication.

'''def passwdcheck():
    while True:
        print('enter your name')
        name = input()
        if name != 'joe':
            continue
        print("hello joe whats the passwoed")

        password = input()
        if password == 'sordfish':
            print('acess granted')
            break
passwdcheck()'''


#Q.2addition of 1 to 100

'''total = 0
for i in range(101):
    total = total +  i
print(total)'''


#Q.3 print random numbers

'''import random
for i in range(10):
    print(random.randint(1,100))'''


#4.    guessing game

'''import random
def guessing_game():
    print("i am thinking a number between 1 to 30")
    thinked = random.randint(1,30)
    for guess1 in range(1,30):

        print("take a guess")

        guess = int(input())
        if guess == thinked:
            print("your guess is correct  and guessed in"+str(guess1)+ " attempt")
            break
        elif guess > thinked:
            print("higer than thinked")
            continue
        elif guess < thinked:
            print("less than thinked")
            continue

guessing_game()'''


#4.rock paper seciors game

'''import random
def game():
    print('rock,paper,secior')
    win = 0
    lose = 0
    tied = 0
    while True:
        print("%s win, %s lose ,%s tied"%(win,lose,tied))
        while True:
            print("select one of the (r)ock,(p)aper,(s)ecior")
            playermove =input()
            if playermove == 'q':
                break
            if playermove == 'r' or playermove == 'p' or playermove == 's':
                break
            print("type one of r,p,s,q")

        if playermove == 'r':
            print("rock vs ")
        elif playermove == 'p':
            print("paper vs ")
        elif playermove == 's':
            print("secior vs ")

        randomnumber = random.randint(1,3)
        if  randomnumber == 1:
            computermove = 'r'
            print('rock')
        elif  randomnumber == 2:
            computermove = 'p'
            print("paper")
        elif  randomnumber == 3:
            computermove = 's'
            print("secior")

        if playermove == computermove:
             print("tied")
             tied = tied +1
        elif playermove == 'r' and computermove == 'p':
            print("cpu win")
            lose = lose +1
        elif playermove == 'r' and computermove == 's':
            print("you win")
            win = win +1
        elif playermove == 'p' and computermove == 'r':
            print("you win")
            win = win +1
        elif playermove == 'p' and computermove == 's':
            print("cpu win")
            lose = lose +1
        elif playermove == 's' and computermove == 'r':
            print("cpu win")
            lose = lose +1
        elif playermove == 's' and computermove == 'p':
            print("you win")
            win = win +1
game()'''


#Q.9 from chapter2 in book

'''import random
def greeting():

    while True:

        randomnumber = random.randint(1,5)
        if randomnumber == 1 :
            spam = 'hello'
            print("hello")
            break

        elif randomnumber == 2 :
            spam = 2
            print("howdy")
            break

        else:
            print("good moring")
            exit()
greeting()'''


#CHAPTER 3
#Q.
