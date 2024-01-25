weight = eval(input("Enter weight in pounds : "))
height = eval(input("Enter height in inches : "))
weightInKilo = weight * 0.45359237
heightInMetres = height * 0.0254
BMI = weightInKilo/(heightInMetres**2)
print("BMI is",round(BMI,4))