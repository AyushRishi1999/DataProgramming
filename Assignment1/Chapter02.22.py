currentPopulation = 312032486
years = eval(input("Enter number of years : "))
totalTime = years*365*24*60*60
birth = totalTime//7
death = totalTime//13
immigrant = totalTime//45
newPopulation = currentPopulation+birth-death+immigrant
print("The US Census Bureau projected population after",years,"years is", newPopulation)