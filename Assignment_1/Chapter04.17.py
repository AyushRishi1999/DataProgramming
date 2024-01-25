import random
hand = eval(input("scissor (0), rock (1), paper (2) : "))
compHand = random.randint(0,2)

if hand == compHand == 0: print("The computer is scissor. You are scissor too. It is a draw.")
elif hand == compHand == 1: print("The rock is scissor. You are rock too. It is a draw.")
elif hand == compHand == 2: print("The computer is paper. You are paper too. It is a draw.")
elif hand == 0 and compHand == 2: print("The computer is Paper. You are scissor. You Won.")
elif hand == 1 and compHand == 0: print("The computer is scissor. You are Rock. You Won.")
elif hand == 2 and compHand == 1: print("The computer is Rock. You are Paper. You Won.")
elif hand == 0 and compHand == 1: print("The computer is Rock. You are scissor. You Lose.")
elif hand == 1 and compHand == 2: print("The computer is Paper. You are Rock. You Lose.")
elif hand == 2 and compHand == 0: print("The computer is scissor. You are Paper. You Lose.")
else: print("Wrong Choice")


