xAtlanta, yAtlanta = -84.360064, 33.928295
xOrlando, yOrlando = -81.508754, 28.507963
xSavannah, ySavannah = -81.0983, 32.0749
xCharlotte, yCharlotte = -80.84405, 35.22802

side1 = (((xOrlando-xAtlanta)**2)+((yOrlando-yAtlanta)**2))**0.5
side2 = (((xSavannah-xAtlanta)**2)+((ySavannah-yAtlanta)**2))**0.5
side3 = (((xOrlando-xSavannah)**2)+((yOrlando-ySavannah)**2))**0.5
sT1 = (side1+side2+side3)/2
areaT1 = (sT1*(sT1-side1)*(sT1-side2)*(sT1-side3))**0.5

side4 = (((xCharlotte-xAtlanta)**2)+((yCharlotte-yAtlanta)**2))**0.5
side5 = (((xCharlotte-xSavannah)**2)+((yCharlotte-ySavannah)**2))**0.5
sT2 = (side4+side2+side5)/2
areaT2 = (sT2*(sT2-side4)*(sT2-side2)*(sT2-side5))**0.5

totalArea = areaT1 + areaT2
print("The area enclosed is",totalArea)