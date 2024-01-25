import time
offsetTimeZone = eval(input("Enter the time zone offset to GMT : "))
seconds = time.time()
remainderHours = seconds%(24*60*60)
hours = remainderHours//(60*60)
remainderMinutes = seconds%(60*60)
minutes = remainderMinutes//60
remainderSeconds = seconds%60
''''offsetHours = offsetTimeZone//10
offsetMinutes = (offsetTimeZone%100)
if offsetMinutes+int(minutes) > 60 :
    offsetHours += 1
    offsetMinutes -= 60
'''
print(int(hours)+offsetTimeZone,":", int(minutes),":",int(remainderSeconds))