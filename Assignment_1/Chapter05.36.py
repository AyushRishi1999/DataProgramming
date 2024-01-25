import random
user=0
comp=0
while user<3 or comp<3:
    compHand = random.randint(0, 2)
    hand = eval(input("scissor (0), rock (1), paper (2) : "))
    if hand == compHand == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif hand == compHand == 1:
        print("The rock is scissor. You are rock too. It is a draw.")
    elif hand == compHand == 2:
        print("The computer is paper. You are paper too. It is a draw.")
    elif hand == 0 and compHand == 2:
        print("The computer is Paper. You are scissor. You Won.")
        user+=1
    elif hand == 1 and compHand == 0:
        print("The computer is scissor. You are Rock. You Won.")
        user += 1
    elif hand == 2 and compHand == 1:
        print("The computer is Rock. You are Paper. You Won.")
        user += 1
    elif hand == 0 and compHand == 1:
        print("The computer is Rock. You are scissor. You Lose.")
        comp+=1
    elif hand == 1 and compHand == 2:
        print("The computer is Paper. You are Rock. You Lose.")
        comp += 1
    elif hand == 2 and compHand == 0:
        print("The computer is scissor. You are Paper. You Lose.")
        comp += 1
    else: print("Wrong Choice")


