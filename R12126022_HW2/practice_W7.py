import random
while True:
    secret = random.randint(1,10)
    guess = 0
    while guess != secret:
        try :
            guess = int(float(input("Guess which number I thought? (1~10): ")))
        except:
            print("Error Value.")
        else:
            if guess == secret:
                print("Bingo!")
            else:
                if guess > secret:
                    print("No, Guess smaller")
                else:
                    print("No, Guess bigger")
    exit = input("Exit? (Y/N): ")
    if ((exit=="Y") or (exit=="y")):
       break 