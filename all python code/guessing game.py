#Basic guessing game

secret_word = "python"
guess = ""
attempt = 0
attempt_limt = 3
game_over = False

while guess != secret_word and not(game_over):
    if attempt < attempt_limt:
        guess = input("enter guess:")
        attempt +=1
    else:
        game_over = True
if game_over:
    print ("lost the game")
else:
    print ("you win.....")