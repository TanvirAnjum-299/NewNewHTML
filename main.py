secret = 27
hearts = 5
status="ice cold","cold","warm","hot"
while hearts > 0:
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print("You win")
        status="ice cold"
        break
    hearts -= 1
    if secret > 0:
        print("You lose a heart")
        print(f"Remaining hearts: {hearts}")
        staus="warm"
        hearts=-1
    if guess>secret:
        print("You lose a heart")
        print(f"Remaining hearts: {hearts}")
        status="warm"
        hearts=-1
    if guess<0:
     print("You lose a heart")
    print(f"Remaining hearts: {hearts}")
    status="hot"
    hearts=-1
    if guess<=secret or guess>=secret:
        print("You lose a heart")
        print(f"Remaining hearts: {hearts}")
        status="cold"
        hearts-=1
    if hearts==0:
        print("You have no hearts")
        print("You have to restart")

    


