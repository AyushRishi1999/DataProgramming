minutes = eval(input("Enter Number of Minutes : "))

years = minutes//(365*24*60)
remainderYear = minutes%(365*24*60)
days = remainderYear//(24*60)

print(minutes,"minutes is approximately",years,"years and",days,"days")