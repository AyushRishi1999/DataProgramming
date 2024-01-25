subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate : "))
gratuity = gratuityRate*subtotal/100
total = subtotal+gratuity
print("The gratuity is",round(gratuity,2),"and the total is",round(total,2))