import time
offsetTimeZone = eval(input("Enter the time zone offset to GMT : "))
today = time.time()%(24*60*60)
offsetTimeInSeconds = today + (offsetTimeZone * 60 * 60)
hours = offsetTimeInSeconds//(60*60)
minutes = (offsetTimeInSeconds%(60*60))//60
seconds = (offsetTimeInSeconds%(60*60))%60

print(int(hours % 24),":", int(minutes),":",int(seconds))
