currentPopulation = 312032486
totalTime = 5*365*24*60*60
birth = totalTime//7
death = totalTime//13
immigrant = totalTime//45
newPopulation = currentPopulation+birth-death+immigrant
print("The US Census Bureau projected population after 5 years is", newPopulation)